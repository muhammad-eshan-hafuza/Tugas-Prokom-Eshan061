# Topik: Istilah dan alat yang sering dipelajari di Teknik Industri
topics = ["Ergonomi", "Supply Chain", "Quality Control", "Statistika", "Manufaktur"]
print("List awal:", topics)

# 1. Menambahkan elemen di akhir dengan append()
topics.append("Simulasi Sistem")
print("Setelah append:", topics)

# 2. Menambahkan elemen di posisi tertentu dengan insert()
topics.insert(1, "Otomasi Industri")
print("Setelah insert di indeks 1:", topics)

# 3. Menghapus berdasarkan posisi dengan del
del topics[0]
print("Setelah del elemen indeks 0:", topics)

# 4. Mengambil dan menghapus elemen dengan pop()
popped_topic = topics.pop()
print(f"Topik yang di-pop: {popped_topic}")
print("Setelah pop:", topics)

# 5. Menghapus berdasarkan nama nilai menggunakan remove()
topics.remove("Statistika")
print("Setelah remove 'Statistika':", topics)

# 6. Melihat jumlah elemen dengan len()
print("Jumlah elemen saat ini:", len(topics))

# 7. Mengurutkan sementara dengan sorted()
print("Urut sementara (sorted):", sorted(topics))
print("List asli tidak berubah:", topics)

# 8. Membalik urutan fisik dengan reverse()
topics.reverse()
print("Setelah reverse():", topics)

# 9. Mengurutkan permanen dengan sort()
topics.sort()
print("Setelah sort() permanen:", topics)