guests = ["B.J. Habibie", "Ki Hajar Dewantara", "Elon Musk"]

# Memberitahu bahwa ada meja yang lebih besar
print("Kabar gembira! Saya menemukan meja makan yang lebih besar, jadi kita bisa mengundang 3 orang lagi.\n")

# Menambahkan tamu di awal list (indeks 0)
guests.insert(0, "Nikola Tesla")

# Menambahkan tamu di tengah list (misal di indeks 2)
guests.insert(2, "Marie Curie")

# Menambahkan tamu di akhir list
guests.append("Alan Turing")

# Cetak undangan untuk semua tamu (sekarang totalnya ada 6 orang)
print(f"Undangan 1: Halo {guests[0]}, silakan hadir di acara makan malam kami.")
print(f"Undangan 2: Halo {guests[1]}, silakan hadir di acara makan malam kami.")
print(f"Undangan 3: Halo {guests[2]}, silakan hadir di acara makan malam kami.")
print(f"Undangan 4: Halo {guests[3]}, silakan hadir di acara makan malam kami.")
print(f"Undangan 5: Halo {guests[4]}, silakan hadir di acara makan malam kami.")
print(f"Undangan 6: Halo {guests[5]}, silakan hadir di acara makan malam kami.")