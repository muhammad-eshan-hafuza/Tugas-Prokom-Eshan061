# 1. Membuat tuple menu buffet (5 menu)
menu_buffet = ('nasi goreng', 'ayam bakar', 'sop buntut', 'es teh', 'puding')

print("Menu asli restoran:")
for makanan in menu_buffet:
    print(f"- {makanan}")

# 2. Coba ubah salah satu item (Hapus tanda komentar '#' di bawah untuk melihat error-nya)
# menu_buffet[0] = 'mie goreng'  # Ini akan menghasilkan TypeError

# 3. Menimpa variabel dengan menu yang baru (2 menu diganti)
menu_buffet = ('mie goreng', 'ikan bakar', 'sop buntut', 'es teh', 'puding')

print("\nMenu yang sudah direvisi:")
for makanan in menu_buffet:
    print(f"- {makanan}")