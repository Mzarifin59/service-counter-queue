from structures.queue import Queue
from structures.stack import Stack
from structures.linked_list import LinkedList
from connect_db import get_connection

# State in-memory (global, di-load ulang saat app start)
antrian_queue = Queue()
riwayat_stack = Stack()
riwayat_linked_list = LinkedList()


def load_from_db():
    """
    Load data dari DB ke struktur data in-memory saat app pertama kali jalan.
    Dipanggil sekali di app.py sebelum server start.
    """
    conn = get_connection()

    # Load antrian yang masih menunggu → masuk Queue
    rows = conn.execute(
        "SELECT nomor_antrian, nama_pelanggan, waktu_daftar FROM antrian ORDER BY id ASC"
    ).fetchall()
    for row in rows:
        antrian_queue.enqueue(dict(row))

    # Load riwayat → masuk Linked List (kronologis) + Stack (LIFO, yang terakhir di atas)
    rows = conn.execute(
        "SELECT nomor_antrian, nama_pelanggan, waktu_daftar, waktu_dilayani FROM riwayat_pelayanan ORDER BY id ASC"
    ).fetchall()
    for row in rows:
        data = dict(row)
        riwayat_linked_list.append(data)
        riwayat_stack.push(data)

    conn.close()


def _generate_nomor_antrian(conn):
    """Generate nomor antrian berikutnya berdasarkan total entri yang pernah ada."""
    total_antrian = conn.execute("SELECT COUNT(*) FROM antrian").fetchone()[0]
    total_riwayat = conn.execute("SELECT COUNT(*) FROM riwayat_pelayanan").fetchone()[0]
    nomor = total_antrian + total_riwayat + 1
    return f"A{nomor:03d}"


def daftar_antrian(nama_pelanggan: str):
    """
    Daftarkan pelanggan baru:
    1. Generate nomor antrian
    2. Enqueue ke Queue in-memory
    3. INSERT ke tabel antrian
    """
    conn = get_connection()
    nomor = _generate_nomor_antrian(conn)

    data = {
        'nomor_antrian': nomor,
        'nama_pelanggan': nama_pelanggan,
        'waktu_daftar': None  # DB akan isi otomatis via DEFAULT CURRENT_TIMESTAMP
    }

    antrian_queue.enqueue(data)
    conn.execute(
        "INSERT INTO antrian (nomor_antrian, nama_pelanggan) VALUES (?, ?)",
        (nomor, nama_pelanggan)
    )
    conn.commit()
    conn.close()
    return nomor


def panggil_antrian():
    """
    Panggil pelanggan berikutnya:
    1. Dequeue dari Queue
    2. Push ke Stack (→ ditampilkan sebagai 'Sedang Dilayani')
    3. Append ke Linked List (→ riwayat kronologis)
    4. DELETE dari antrian, INSERT ke riwayat_pelayanan
    """
    if antrian_queue.is_empty():
        return None

    customer = antrian_queue.dequeue()

    riwayat_stack.push(customer)
    riwayat_linked_list.append(customer)

    conn = get_connection()
    conn.execute(
        "DELETE FROM antrian WHERE nomor_antrian = ?",
        (customer['nomor_antrian'],)
    )
    conn.execute(
        "INSERT INTO riwayat_pelayanan (nomor_antrian, nama_pelanggan, waktu_daftar) VALUES (?, ?, ?)",
        (customer['nomor_antrian'], customer['nama_pelanggan'], customer.get('waktu_daftar'))
    )
    conn.commit()
    conn.close()

    return customer


def get_state():
    """Kumpulkan semua state untuk di-render di template."""
    return {
        'antrian': antrian_queue.to_list(),
        'jumlah_antrian': antrian_queue.size(),
        'sedang_dilayani': riwayat_stack.peek(),   # Top of Stack 
        'riwayat': list(reversed(riwayat_linked_list.to_list())),  # New on Top
    }


def reset_simulasi():
    """Reset semua data (untuk keperluan simulasi / demo ulang)."""
    global antrian_queue, riwayat_stack, riwayat_linked_list
    antrian_queue = Queue()
    riwayat_stack = Stack()
    riwayat_linked_list = LinkedList()

    conn = get_connection()
    conn.execute("DELETE FROM antrian")
    conn.execute("DELETE FROM riwayat_pelayanan")
    conn.commit()
    conn.close()