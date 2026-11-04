# Meminta input jumlah orang
jumlah_tamu = input("Berapa jumlah orang dalam rombongan makan Anda? ")

# Mengubah input teks menjadi angka bulat (integer)
jumlah_tamu = int(jumlah_tamu)

# Mengecek apakah tamu lebih dari 8 orang
if jumlah_tamu > 8:
    print("Maaf, meja sedang penuh. Anda harus menunggu beberapa saat.")
else:
    print("Meja Anda sudah siap, silakan masuk!")