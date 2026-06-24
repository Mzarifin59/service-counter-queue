class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Implementasi Stack (LIFO) — dipakai untuk melacak customer yang baru dipanggil."""

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """Tambah data ke atas stack."""
        node = Node(data)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        """Ambil dan hapus data dari atas stack."""
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        """Lihat data paling atas tanpa menghapus."""
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def to_list(self):
        """Kembalikan list dari top ke bottom."""
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result