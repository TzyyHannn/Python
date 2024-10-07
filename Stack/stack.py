class StackBaju:
    def __init__(self):
        self.tumpukan = []
        self.baju = []

    def push(self, baju):
        # Menambahkan baju ke tumpukan
        self.tumpukan.append(baju)
        print(f'Baju {baju} ditambahkan ke tumpukan.')
    def pop(self):
        # Mengambil baju dari tumpukan
        if self.is_empty():
            print("Tumpukan kosong, tidak ada baju untuk diambil.")
            return None
        baju = self.tumpukan.pop()
        print(f'Baju {baju} diambil dari tumpukan.')
        return baju

    def peek(self):
        # Melihat baju paling atas
        if self.is_empty():
            print("Tumpukan kosong.")
            return None
        return self.tumpukan[-1]

    def is_empty(self):
        # Mengecek apakah tumpukan kosong
        return len(self.tumpukan) == 0

    def size(self):
        # Mengecek ukuran tumpukan
        return len(self.tumpukan)

# Contoh penggunaan:
tumpukan_baju = StackBaju()

tumpukan_baju.push("Kemeja")
tumpukan_baju.push("Kaos")
tumpukan_baju.push("Jaket")


tumpukan_baju.pop()
tumpukan_baju.pop()

print(f'Baju teratas: {tumpukan_baju.peek()}')
print(f'Tumpukan kosong : {tumpukan_baju.is_empty()}')
print(f'Ukuran tumpukan : {tumpukan_baju.size()}')





