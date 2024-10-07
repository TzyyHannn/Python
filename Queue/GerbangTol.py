class GerbangTol:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, plat):
        self.items.append(plat)
        print(f'kendaraan dengan plat {plat} masuk ke antrian.')

    def dequeue(self):
        if not self.is_empty():
            removed_plat = self.items.pop(0)
            print(f'Kendaraan {removed_plat} keluar dari antrian.')
            return removed_plat
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
            print('Antrian kendaraan saat ini:', ' -> '.join(self.items))
        else:
            print('Antrian kosong.')

# Fungsi utama untuk menjalankan program
def main():
    queue = GerbangTol()
    
    while True:
        print("\nMenu:")
        print("1. Tambah kendaraan ke antrian")
        print("2. Kendaraan keluar dari antrian")
        print("3. Tampilkan antrian")
        print("4. Jumlah kendaraan dalam antrian")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1-5): ")
        
        if choice == '1':
            kendaraan = input("Masukkan plat nomor kendaraan: ")
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



