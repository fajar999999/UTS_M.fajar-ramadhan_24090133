def hitung_total_belanja():

  """Menghitung total belanja dari beberapa barang."""

  jumlah_barang = int(input("Masukkan jumlah barang: "))

  total = 0

  for i in range(1, jumlah_barang + 1):

    harga = int(input(f"Masukkan harga barang ke-{i}: "))

    total += harga

  print(f"Total belanjaan Rp. {total}")

hitung_total_belanja()