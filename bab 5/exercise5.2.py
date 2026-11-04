# 1. Uji teks (string)
makanan = 'Bakso'
print("1. Cek string:")
print(makanan == 'Bakso')   # True
print(makanan != 'Bakso')   # False

# 2. Uji menggunakan method .lower()
nama = 'BUDI'
print("\n2. Cek method lower():")
print(nama.lower() == 'budi')   # True
print(nama.lower() == 'BUDI')   # False

# 3. Uji numerik (angka)
tinggi = 170
print("\n3. Cek angka:")
print(tinggi == 170)   # True
print(tinggi != 170)   # False
print(tinggi > 160)    # True
print(tinggi < 160)    # False
print(tinggi >= 170)   # True
print(tinggi <= 150)   # False

# 4. Uji 'and' dan 'or'
ipk = 3.75
kehadiran = 90
print("\n4. Cek 'and' dan 'or':")
print(ipk >= 3.5 and kehadiran >= 80)  # True (keduanya benar)
print(ipk >= 3.5 and kehadiran < 80)   # False (salah satu salah)
print(ipk >= 3.5 or kehadiran < 50)    # True (salah satu sudah benar)
print(ipk < 2.0 or kehadiran < 50)     # False (dua-duanya salah)

# 5. Uji apakah item ada di dalam list ('in')
daftar_alat = ['helm', 'sepatu safety', 'sarung tangan']
print("\n5. Cek 'in' list:")
print('helm' in daftar_alat)         # True
print('kacamata' in daftar_alat)     # False

# 6. Uji apakah item TIDAK ada di dalam list ('not in')
print("\n6. Cek 'not in' list:")
print('rompi' not in daftar_alat)    # True (karena rompi memang tidak ada)
print('helm' not in daftar_alat)     # False (salah, karena helm ada di list)