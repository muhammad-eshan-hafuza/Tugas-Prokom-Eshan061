sandwich_orders = [
    'pastrami', 'tuna', 'ayam panggang', 
    'pastrami', 'keju telur', 'pastrami'
]
finished_sandwiches = []

# Memberi tahu bahwa bahan pastrami habis
print("PEMBERITAHUAN: Mohon maaf, kami sedang kehabisan pastrami hari ini.\n")

# Menghapus seluruh pesanan pastrami sampai tidak bersisa
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Memproses sisa pesanan yang masih ada
while sandwich_orders:
    sandwich_sedang_dibuat = sandwich_orders.pop()
    print(f"Saya sedang membuat sandwich {sandwich_sedang_dibuat} Anda.")
    finished_sandwiches.append(sandwich_sedang_dibuat)

# Menampilkan hasil akhir
print("\n--- Semua Sandwich Telah Selesai Dibuat ---")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")