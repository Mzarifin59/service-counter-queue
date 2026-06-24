from connect_db import get_connection

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS antrian (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomor_antrian TEXT NOT NULL UNIQUE,
            nama_pelanggan TEXT NOT NULL,
            waktu_daftar DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'Menunggu'
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS riwayat_pelayanan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomor_antrian TEXT NOT NULL,
            nama_pelanggan TEXT NOT NULL,
            waktu_daftar DATETIME,
            waktu_dilayani DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database berhasil diinisialisasi.")