# List tempat impian (tidak berurutan abjad)
places = ["Jepang", "Swiss", "Mekkah", "Jerman", "Islandia"]

# 1. Cetak urutan asli
print("1. Urutan asli:")
print(places)

# 2. Cetak urut abjad sementara menggunakan sorted()
print("\n2. Urut abjad (sementara dengan sorted):")
print(sorted(places))

# 3. Buktikan list asli tidak berubah
print("\n3. Membuktikan list masih dalam urutan asli:")
print(places)

# 4. Cetak urut abjad terbalik sementara
print("\n4. Urut abjad terbalik (sementara dengan sorted reverse=True):")
print(sorted(places, reverse=True))

# 5. Buktikan list asli masih tidak berubah
print("\n5. Membuktikan list masih dalam urutan asli:")
print(places)

# 6. Balik urutan secara permanen dengan reverse()
places.reverse()
print("\n6. Setelah di-reverse() (urutan fisik dibalik):")
print(places)

# 7. Balik sekali lagi agar kembali ke posisi semula
places.reverse()
print("\n7. Setelah di-reverse() kedua kali (kembali normal):")
print(places)

# 8. Urutkan secara permanen sesuai abjad dengan sort()
places.sort()
print("\n8. Setelah di-sort() (berubah permanen sesuai abjad A-Z):")
print(places)

# 9. Urutkan secara permanen abjad terbalik dengan sort(reverse=True)
places.sort(reverse=True)
print("\n9. Setelah di-sort(reverse=True) (berubah permanen Z-A):")
print(places)