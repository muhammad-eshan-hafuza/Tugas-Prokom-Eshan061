current_users = ['Budi', 'Siti', 'Andi', 'Rian', 'Dewi']
new_users = ['andi', 'Farhan', 'BUDI', 'Kevin', 'Citra']

# Buat salinan current_users dalam huruf kecil semua
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

# Cek setiap user baru
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Nama '{new_user}' sudah dipakai. Silakan masukkan username lain.")
    else:
        print(f"Nama '{new_user}' masih tersedia.")