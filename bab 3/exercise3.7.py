# Melanjutkan list tamu dari latihan 3-6 (6 orang)
guests = ["Nikola Tesla", "B.J. Habibie", "Marie Curie", "Ki Hajar Dewantara", "Elon Musk", "Alan Turing"]

print("Mohon maaf yang sebesar-besarnya, meja baru tidak sampai tepat waktu. Saya hanya bisa mengundang 2 orang saja.\n")

# Mengeluarkan tamu satu per satu menggunakan pop()
# pop() mengambil dan menghapus elemen dari posisi paling belakang
popped_guest = guests.pop()
print(f"Mohon maaf {popped_guest}, meja tidak mencukupi sehingga saya belum bisa mengundang Anda makan malam.")

popped_guest = guests.pop()
print(f"Mohon maaf {popped_guest}, meja tidak mencukupi sehingga saya belum bisa mengundang Anda makan malam.")

popped_guest = guests.pop()
print(f"Mohon maaf {popped_guest}, meja tidak mencukupi sehingga saya belum bisa mengundang Anda makan malam.")

popped_guest = guests.pop()
print(f"Mohon maaf {popped_guest}, meja tidak mencukupi sehingga saya belum bisa mengundang Anda makan malam.\n")

# Menyampaikan pesan kepada 2 tamu yang masih tersisa
print(f"Kabar baik {guests[0]}, Anda masih tetap terundang ke acara makan malam.")
print(f"Kabar baik {guests[1]}, Anda masih tetap terundang ke acara makan malam.\n")

# Menghapus 2 orang terakhir menggunakan del agar list menjadi kosong
del guests[0]
del guests[0] # Setelah indeks 0 dihapus, elemen berikutnya bergeser ke indeks 0

# Memastikan list sudah kosong
print("Isi list tamu saat ini:", guests)