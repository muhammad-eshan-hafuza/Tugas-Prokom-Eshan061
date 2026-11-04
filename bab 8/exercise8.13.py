def build_profile(first, last, **user_info):
    """Membangun dictionary berisi semua informasi tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Isi dengan profil kamu sendiri sebagai maba Teknik Industri
profil_saya = build_profile(
    "Andi",
    "Pratama",
    jurusan="Teknik Industri",
    angkatan=2024,
    kota_asal="Bandung",
    hobi="Bermain Futsal"
)

print(profil_saya)