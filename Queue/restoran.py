import queue
import time

class Restoran:
  def __init__(self):
    self.antrian = queue.Queue()
    self.max_antrian = 3 # Maksimal antrian yang dapat ditampung

  def masuk_antrian(self, nama_pelanggan):
      if self.antrian.qsize() < self.max_antrian:
        self.antrian.put(nama_pelanggan)
        print(f"{nama_pelanggan} telah masuk antrian.")
      else:
        print(f"Antrian penuh {nama_pelanggan} tidak dapat masuk.")
  def duduk(self):
      if not self.antrian.empty():
        nama_pelanggan = self.antrian.get()
        print(f"{nama_pelanggan} telah duduk.")
      else:
         print("Antrian kosong.")

  def tampilkan_antrian(self):
     print("Antrian saat ini:")
     while not self.antrian.empty():
        print(self.antrian.get(False), end=" ")
        self.antrian.task_done()
        print()

# Membuat objek retoran
restoran = Restoran()

# Menambahkan pelanggan ke antrian
restoran.masuk_antrian("Raihan")
restoran.masuk_antrian("Agi")
restoran.masuk_antrian("Zenal")

# Tampilkan antrian saat ini
restoran.tampilkan_antrian()

# Pelanggan duduk
restoran.duduk()

# Tampilan antrian setelah seseorang duduk
restoran.tampilkan_antrian()

# Sumulasi waktu tunggu
time.sleep(2) # simulasi waktu tunggu 2 detik

# Pelanggan lainnya duduk secara berurutan
for _ in range(restoran.max_antrian - 1):
  restoran.duduk()
  time.sleep(1) # simulasi waktu tunggu 1 detik

# tampilkan antrian akhir
restoran.tampilkan_antrian()