def make_album(artist, title):
    """Fungsi sederhana untuk membuat dictionary album."""
    return {'artist': artist, 'title': title}

# Perulangan while untuk menerima input pengguna
while True:
    print("\nMasukkan data album (ketik 'q' kapan saja untuk berhenti):")
    
    artist_name = input("Nama Artis: ")
    if artist_name.lower() == 'q':
        break
        
    album_title = input("Judul Album: ")
    if album_title.lower() == 'q':
        break
        
    album_info = make_album(artist_name, album_title)
    print(f"Data album tersimpan: {album_info}")

print("Program selesai. Terima kasih!")