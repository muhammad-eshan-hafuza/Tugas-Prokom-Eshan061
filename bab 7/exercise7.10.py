# Dictionary kosong untuk menyimpan hasil survei (Format: Nama -> Tempat)
hasil_polling = {}

# Status apakah survei masih dibuka
survei_aktif = True

while survei_aktif:
    # Meminta input nama dan tempat tujuan
    nama = input("\nSiapa nama Anda? ")
    tujuan = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")
    
    # Menyimpan jawaban ke dalam dictionary
    hasil_polling[nama] = tujuan
    
    # Menanyakan apakah masih ada responden lain
    ulang = input("Apakah ada orang lain yang ingin mengisi survei? (ya/tidak): ")
    if ulang.lower() == 'tidak':
        survei_aktif = False

# Menampilkan seluruh hasil survei
print("\n--- HASIL POLLING LIBURAN IMPIAN ---")
for nama, tujuan in hasil_polling.items():
    print(f"{nama} ingin berlibur ke {tujuan}.")