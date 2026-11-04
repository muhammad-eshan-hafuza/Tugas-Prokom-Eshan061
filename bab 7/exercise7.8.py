# Daftar pesanan sandwich awal
sandwich_orders = ['tuna', 'ayam panggang', 'keju telur', 'daging sapi']

# Daftar kosong untuk menampung sandwich yang sudah jadi
finished_sandwiches = []

# Proses pembuatan: selama masih ada pesanan di sandwich_orders
while sandwich_orders:
    # Mengambil satu pesanan
    sandwich_sedang_dibuat = sandwich_orders.pop()
    
    print(f"Saya sedang membuat sandwich {sandwich_sedang_dibuat} Anda.")
    
    # Memindahkan ke daftar sandwich yang sudah selesai
    finished_sandwiches.append(sandwich_sedang_dibuat)

# Menampilkan hasil akhir
print("\n--- Semua Sandwich Telah Selesai Dibuat ---")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")