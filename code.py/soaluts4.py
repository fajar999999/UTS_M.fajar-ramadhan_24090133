def is_kabisat(tahun):
  """Mengecek apakah suatu tahun adalah tahun kabisat.

  Args:
    tahun: Tahun yang akan dicek.

  Returns:
    True jika tahun tersebut adalah tahun kabisat, False jika bukan.
  """

  if tahun % 400 == 0:
    return True
  elif tahun % 4 == 0 and tahun % 100 != 0:
    return True
  else:
    return False

# Input tahun dari pengguna
tahun = int(input("Masukkan tahun: "))

# Panggil fungsi dan cetak hasilnya
if is_kabisat(tahun):
  print(f"Tahun {tahun} merupakan TAHUN KABISAT")
else:
  print(f"Tahun {tahun} bukan TAHUN KABISAT")