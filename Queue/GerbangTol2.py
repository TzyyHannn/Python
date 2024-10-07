class Vehicle:
    def __init__(self, Jenis_Kendaraan, Plat_Nomor):
        self.jenis_Kendaraan = Jenis_Kendaraan
        self.plat_Nomor = Plat_Nomor

    def __str__(self):
        return f'{self.jenis_Kendaraan} ({self.plat_Nomor})'
    
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, kendaraan):
        self.items.append(kendaraan)
        print(f'Kendaraan {kendaraan} masuk ke antrian.')

    def dequeue(self):
        if not self.is_empty():
            Hapus_Kendaraan = self.items.pop(0)
            print(f'Kendaraan {Hapus_Kendaraan} keluar dari antrian.')
            return Hapus_Kendaraan
        else:
            print('Antrian kosong, tidak ada kendaraan yang bisa keluar.')

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def display(self):
        if not self.is_empty():
            print('Antrian kendaraan saat ini:')
            for kendaraan in self.items:
                print(kendaraan)
        else:
            print('Antrian kosong.')


# Fungsi utama untuk menjalankan program
def main():
    queue = Queue()
    
    while True:
        print("\nMenu:")
        print("1. Tambah kendaraan ke antrian")
        print("2. Kendaraan keluar dari antrian")
        print("3. Tampilkan antrian")
        print("4. Jumlah kendaraan dalam antrian")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1-5): ")
        
        if choice == '1':
            Tipe_Kendaraan = input("Masukkan jenis kendaraan (misal: Mobil, Motor): ")
            Plat_Nomor = input("Masukkan nomor plat kendaraan: ")
            kendaraan = Vehicle(Tipe_Kendaraan, Plat_Nomor)
            queue.enqueue(kendaraan)
        
        elif choice == '2':
            queue.dequeue()
        
        elif choice == '3':
            queue.display()
        
        elif choice == '4':
            print(f'Jumlah kendaraan dalam antrian: {queue.size()}')
        
        elif choice == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
