favorite_places = {
    'Andi': ['Bali', 'Lombok', 'Yogyakarta'],
    'Budi': ['Jepang'],
    'Citra': ['Bandung', 'Malang']
}

# Perulangan ganda: loop pertama untuk orang, loop kedua untuk daftar tempatnya
for name, places in favorite_places.items():
    print(f"Tempat favorit {name}:")
    for place in places:
        print(f"  - {place}")
    print()  # Baris kosong pemisah