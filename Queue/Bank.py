class BankQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, customer):
        """Menambahkan pelanggan ke antrian."""
        self.queue.append(customer)
        print(f"Pelanggan {customer} telah ditambahkan ke antrian.")

    def dequeue(self):
        """Mengeluarkan pelanggan dari antrian."""
        if not self.is_empty():
            customer = self.queue.pop(0)
            print(f"Pelanggan {customer} telah diambil dari antrian.")
            return customer
        else:
            print("Antrian kosong.")
            return None

    def peek(self):
        """Melihat pelanggan di depan antrian tanpa mengeluarkannya."""
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        """Mengembalikan True jika antrian kosong."""
        return len(self.queue) == 0

    def size(self):
        """Mengembalikan jumlah pelanggan di antrian."""
        return len(self.queue)


# Contoh penggunaan
bank_queue = BankQueue()

# Menambahkan pelanggan ke antrian
bank_queue.enqueue("Agi")
bank_queue.enqueue("Raihan")
bank_queue.enqueue("Najib")

# Melihat pelanggan di depan antrian
print("Pelanggan di depan antrian:", bank_queue.peek())

# Mengeluarkan pelanggan dari antrian
bank_queue.dequeue()

# Melihat pelanggan di depan antrian setelah mengeluarkan satu pelanggan
print("Pelanggan di depan antrian setelah mengeluarkan satu pelanggan:", bank_queue.peek())

# Menghitung jumlah pelanggan di antrian
print("Jumlah pelanggan di antrian:", bank_queue.size())