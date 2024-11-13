def kalkulator_sederhana():
  """Fungsi untuk melakukan operasi penjumlahan, pengurangan, dan perkalian."""

  #input nilai A dari pengguna
  a = float(input("Masukkan nilai A: "))

  #input nilai B dari pengguna
  b = float(input("Masukkan nilai B: "))

  # Melakukan operasi penjumlahan, pengurangan, dan perkalian
  jumlah = a + b
  kurang = a - b
  kali = a * b

  # Menampilkan hasil operasi
  print("Hasil operasi:")
  print("A + B =", jumlah)
  print("A - B =", kurang)
  print("A * B =", kali)

# Memanggil fungsi untuk menjalankan program
kalkulator_sederhana()