tools = ["Jangka Sorong", "Stopwatch Analisis Waktu", "Safety Helmet"]

# List di atas hanya memiliki indeks 0, 1, dan 2 (total 3 item).

# -------------------------------------------------------------
# CONTOH ERROR (Jika baris di bawah diaktifkan, program akan crash):
# print(tools[3]) 
# Error yang muncul di Terminal VS Code:
# IndexError: list index out of range
# -------------------------------------------------------------

# CARA MEMPERBAIKI:
# Gunakan indeks yang sah, yaitu 0, 1, atau 2 (atau -1 untuk mengambil elemen paling akhir)
print("Elemen terakhir yang benar (indeks 2):", tools[2])
print("Atau menggunakan indeks negatif (-1):", tools[-1])