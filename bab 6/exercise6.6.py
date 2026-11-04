# Data orang yang sudah mengisi polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Daftar orang yang ditargetkan ikut polling
people_to_poll = ['sarah', 'budi', 'edward', 'ani', 'phil']

# Cek apakah nama mereka sudah ada di dalam dictionary
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()} sudah mengisi polling bahasa favorit!")
    else:
        print(f"Halo {person.title()}, yuk luangkan waktu untuk ikut polling!")