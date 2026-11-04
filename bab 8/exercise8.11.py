def send_messages(messages, sent_messages):
    """Memindahkan pesan dari list 'messages' ke 'sent_messages'."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

pesan_awal = ["Pesan 1", "Pesan 2", "Pesan 3"]
pesan_terkirim = []

# Mengirim salinan list menggunakan pesan_awal[:]
send_messages(pesan_awal[:], pesan_terkirim)

print("\n--- PEMBUKTIAN ---")
print("Pesan awal (tetap ada/utuh):", pesan_awal)
print("Pesan terkirim:", pesan_terkirim)