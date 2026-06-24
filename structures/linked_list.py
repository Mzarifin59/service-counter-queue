class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Implementasi Singly Linked List — dipakai untuk mencatat riwayat pelayanan secara kronologis."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        """Tambah data ke ekor list (urutan kronologis)."""
        node = Node(data)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node
        self._size += 1

    def size(self):
        return self._size

    def to_list(self):
        """Traverse dari head ke tail → urutan pertama dilayani ke terakhir."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result