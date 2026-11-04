favorite_numbers = {
    'Budi': [7, 12, 45],
    'Siti': [14, 2],
    'Rian': [3],
    'Dewi': [21, 9, 99],
    'Eko': [10, 50]
}

# Mencetak semua angka favorit tiap orang
for name, numbers in favorite_numbers.items():
    print(f"Angka favorit {name} adalah:")
    for number in numbers:
        print(f"  - {number}")
    print()