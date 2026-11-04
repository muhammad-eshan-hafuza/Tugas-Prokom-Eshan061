def make_shirt(size="L", message="I love Python"):
    """Fungsi kaos dengan nilai bawaan (default)."""
    print(f"Kaos dibuat dengan ukuran {size} dan bertuliskan: '{message}'.")

# Kaos ukuran L dengan pesan default (tidak perlu isi argumen apa pun)
make_shirt()

# Kaos ukuran M dengan pesan default
make_shirt(size="M")

# Kaos ukuran S dengan pesan yang berbeda
make_shirt(size="S", message="Teknik Industri Mantap!")