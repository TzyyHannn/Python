from collections import deque

class FireTruckQueue:
    def _init_(self):
        # Menggunakan deque untuk antrian
        self.queue = deque()

    def add_firetruck(self, truck):
        # Menambahkan mobil pemadam kebakaran ke antrian
        print(f"Mobil pemadam kebakaran {truck} datang.")
        self.queue.append(truck)

    def dispatch_firetruck(self):
        # Mengeluarkan mobil pemadam kebakaran dari antrian
        if self.is_empty():
            print("Tidak ada mobil pemadam kebakaran di antrian.")
        else:
            truck = self.queue.popleft()
            print(f"Mobil pemadam kebakaran {truck} telah dikirim ke lokasi kebakaran.")
            return truck

    def next_firetruck(self):
        # Melihat mobil pemadam kebakaran yang pertama dalam antrian
        if self.is_empty():
            print("Tidak ada mobil pemadam kebakaran di antrian.")
        else:
            print(f"Mobil pemadam kebakaran berikutnya adalah {self.queue[0]}.")

    def is_empty(self):
        # Mengecek apakah antrian kosong
        return len(self.queue) == 0

    def firetruck_count(self):
        # Menghitung jumlah mobil pemadam kebakaran dalam antrian
        return len(self.queue)

# Simulasi Penggunaan
fire_station = FireTruckQueue()

# Menambah mobil pemadam kebakaran ke antrian
fire_station.add_firetruck("A")
fire_station.add_firetruck("B")
fire_station.add_firetruck("C")

# Menampilkan mobil pemadam kebakaran berikutnya
fire_station.next_firetruck()

# Mengirim mobil pemadam kebakaran ke lokasi kebakaran
fire_station.dispatch_firetruck()

# Menampilkan mobil pemadam kebakaran berikutnya
fire_station.next_firetruck()

# Mengirim mobil pemadam kebakaran lainnya
fire_station.dispatch_firetruck()
fire_station.dispatch_firetruck()