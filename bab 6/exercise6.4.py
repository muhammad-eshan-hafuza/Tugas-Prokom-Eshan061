glossary = {
    'variabel': 'Wadah untuk menyimpan data atau nilai di dalam memori program.',
    'string': 'Tipe data berisi teks atau karakter yang diapit tanda petik.',
    'integer': 'Tipe data angka bilangan bulat (tanpa koma desimal).',
    'list': 'Kumpulan beberapa data terurut yang diapit tanda kurung siku [].',
    'loop': 'Perulangan yang mengeksekusi blok kode berulang kali secara otomatis.',
    # 5 istilah tambahan baru:
    'dictionary': 'Kumpulan data berupa pasangan kunci dan nilai (key-value pair).',
    'boolean': 'Tipe data logika yang hanya bernilai True (Benar) atau False (Salah).',
    'float': 'Tipe data angka bilangan desimal/berkoma.',
    'komentar': 'Catatan dalam kode yang diawali tanda # dan diabaikan oleh Python.',
    'if-statement': 'Percabangan logika untuk mengambil keputusan sesuai kondisi.'
}

# Menggunakan for loop untuk mencetak semua istilah
# .title() digunakan agar huruf pertama kata menjadi kapital
for kata, arti in glossary.items():
    print(f"{kata.title()}:\n  {arti}\n")