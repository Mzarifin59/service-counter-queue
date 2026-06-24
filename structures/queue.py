class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """Implementasi Queue (FIFO) menggunakan Linked Node."""

    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        """Tambah data ke belakang queue."""
        node = Node(data)
        if self.rear:
            self.rear.next = node
        self.rear = node
        if not self.front:
            self.front = node
        self._size += 1

    def dequeue(self):
        """Ambil dan hapus data dari depan queue (FIFO)."""
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self._size -= 1
        return data

    def peek(self):
        return self.front.data if self.front else None

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size

    def to_list(self):
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result