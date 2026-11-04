def send_messages(messages, sent_messages):
    """Mencetak pesan dan memindahkannya ke sent_messages."""
    while messages:
        # Mengambil pesan terdepan dan menghapusnya dari list lama
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        # Memasukkan ke list pesan terkirim
        sent_messages.append(current_message)

pesan_awal = ["Pesan 1: Halo!", "Pesan 2: Kuliah di Lab Komputer", "Pesan 3: Sampai jumpa!"]
pesan_terkirim = []

# Jalankan fungsi
send_messages(pesan_awal, pesan_terkirim)

# Cek hasil akhir list
print("\n--- HASIL AKHIR ---")
print("Pesan awal (sekarang kosong):", pesan_awal)
print("Pesan terkirim:", pesan_terkirim)