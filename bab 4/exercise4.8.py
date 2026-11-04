cubes = []

# Menghitung pangkat tiga dari 1 sampai 10
for angka in range(1, 11):
    nilai_kubik = angka ** 3
    cubes.append(nilai_kubik)

# Mencetak tiap nilai kubik
for nilai in cubes:
    print(nilai)