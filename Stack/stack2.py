class TumpukanBaju:
    def __init__(self):
        self.tumpukan = []

    def tambah_baju(self, baju):
        # Menambahkan baju (push) ke tumpukan.
        self.tumpukan.append(baju)
        print(f"{baju} telah ditambahkan ke tumpukan.")

    def hapus_baju(self):
        # Menghapus baju (pop) teratas dari tumpukan.
        if not self.is_empty():
            baju = self.tumpukan.pop()
            print(f"{baju} telah dihapus dari tumpukan.")
            return baju
        else:
            print("Tumpukan baju kosong. Tidak ada baju yang dapat dihapus.")

    def lihat_baju_teratas(self):
        # Melihat baju teratas (peek) tanpa menghapusnya.
        if not self.is_empty():
            return self.tumpukan[-1]
        else:
            print("Tumpukan baju kosong.")

    def is_empty(self):
        """Memeriksa apakah tumpukan kosong."""
        return len(self.tumpukan) == 0

    def tampilkan_tumpukan(self):
        # Menampilkan semua baju dalam tumpukan.
        if not self.is_empty():
            print("Baju dalam tumpukan:")
            for baju in reversed(self.tumpukan):
                print(baju)
        else:
            print("Tumpukan baju kosong.")
    
    def size(self):
        # Mengecek ukuran tumpukan
        return len(self.tumpukan)

# Contoh penggunaan
tumpukan_baju = TumpukanBaju()

# Menambahkan baju (push)
tumpukan_baju.tambah_baju("Kaos Merah")
tumpukan_baju.tambah_baju("Kemeja Biru")
tumpukan_baju.tambah_baju("Jaket")

tumpukan_baju.tampilkan_tumpukan()

tumpukan_baju.hapus_baju()

print(f"Baju teratas: {tumpukan_baju.lihat_baju_teratas()}")
print(f"Apakah tumpukan kosong: {tumpukan_baju.is_empty()}")
print(f"Ukuran tumpukan: {tumpukan_baju.size()}")