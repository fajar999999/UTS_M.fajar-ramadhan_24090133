def hitung_bmi():
  """Menghitung indeks massa tubuh (BMI)."""

  berat_badan = float(input("Masukkan berat badan (kg): "))
  tinggi_badan = float(input("Masukkan tinggi badan (m): "))

  bmi = berat_badan / (tinggi_badan ** 2)
  print(f"BMI Anda adalah: {bmi:.2f}")

  if bmi < 18.5:
    print("Anda kekurangan berat badan.")
  elif 18.5 <= bmi < 25:
    print("Berat badan Anda ideal.")
  elif 25 <= bmi < 30:
    print("Anda kelebihan berat badan.")
  else:
    print("Anda obesitas.")

hitung_bmi()