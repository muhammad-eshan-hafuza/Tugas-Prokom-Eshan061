def make_shirt(size, message):
    """Mencetak ukuran kaos dan pesan sablonnya."""
    print(f"Kaos dibuat dengan ukuran {size} dan bertuliskan: '{message}'.")

# 1. Positional arguments (urutan: ukuran dulu, baru pesan)
make_shirt("L", "Anak Teknik Industri")

# 2. Keyword arguments (posisi boleh terbalik karena diberi nama)
make_shirt(message="Semangat Kuliah!", size="M")