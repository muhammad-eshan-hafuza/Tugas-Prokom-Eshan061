# Meminta input angka dan langsung mengubahnya menjadi integer
angka = int(input("Masukkan sebuah angka: "))

# Cek apakah sisa bagi angka dengan 10 sama dengan 0
if angka % 10 == 0:
    print(f"Angka {angka} adalah kelipatan 10.")
else:
    print(f"Angka {angka} bukan kelipatan 10.")