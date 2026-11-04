guests = ["B.J. Habibie", "Henry Ford", "Elon Musk"]

# 1. Tamu yang tidak bisa hadir (misal tamu di indeks ke-1: Henry Ford)
guest_unable = guests[1]
print(f"Kabar duka/konfirmasi: Sayangnya Bapak {guest_unable} tidak dapat menghadiri acara makan malam.\n")

# 2. Mengganti Henry Ford dengan tamu baru: Ki Hajar Dewantara
guests[1] = "Ki Hajar Dewantara"

# 3. Cetak ulang undangan
print(f"Yth. Bapak {guests[0]}, undangan makan malam tetap berlaku. Sampai jumpa!")
print(f"Yth. Bapak {guests[1]}, kami mengundang Bapak untuk hadir dalam makan malam kehormatan.")
print(f"Yth. {guests[2]}, undangan makan malam tetap berlaku. Sampai jumpa!")