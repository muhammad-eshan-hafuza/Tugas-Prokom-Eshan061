def make_sandwich(*items):
    """Menerima berapa pun jumlah isian sandwich yang dimasukkan."""
    print("\nMembuat pesanan sandwich dengan isian:")
    for item in items:
        print(f"- {item}")
    print("Sandwich siap disajikan!")

# Panggilan 1: 2 isian
make_sandwich("keju", "daging asap")

# Panggilan 2: 3 isian
make_sandwich("telur", "selada", "tomat")

# Panggilan 3: 4 isian
make_sandwich("ayam panggang", "mayones", "keju cheddar", "saus sambal")