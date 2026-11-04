def make_album(artist, title, num_songs=None):
    """Membangun dictionary informasi album musik."""
    album = {
        'artist': artist,
        'title': title
    }
    # Jika user menyertakan jumlah lagu, tambahkan ke dictionary
    if num_songs:
        album['num_songs'] = num_songs
    return album

# 3 pemanggilan fungsi (salah satunya menyertakan jumlah lagu)
album_1 = make_album("Sheila on 7", "Kisah Klasik")
album_2 = make_album("Tulus", "Manusia")
album_3 = make_album("Coldplay", "Parachutes", num_songs=10)

print(album_1)
print(album_2)
print(album_3)