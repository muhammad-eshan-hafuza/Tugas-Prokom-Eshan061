# Cara 1: Mengimpor seluruh modul
import kalkulator
print(kalkulator.tambah(5, 3))

# Cara 2: Mengimpor fungsi spesifik
from kalkulator import tambah
print(tambah(5, 3))

# Cara 3: Mengimpor fungsi dengan nama alias/singkatan (as)
from kalkulator import tambah as t
print(t(5, 3))

# Cara 4: Mengimpor modul dengan nama alias (as)
import kalkulator as k
print(k.tambah(5, 3))

# Cara 5: Mengimpor semua fungsi yang ada di modul menggunakan bintang (*)
from kalkulator import *
print(tambah(5, 3))