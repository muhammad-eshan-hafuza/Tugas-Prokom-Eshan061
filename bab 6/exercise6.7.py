# Membuat 3 dictionary data orang
person_1 = {'first_name': 'Andi', 'last_name': 'Pratama', 'age': 19, 'city': 'Bandung'}
person_2 = {'first_name': 'Budi', 'last_name': 'Santoso', 'age': 20, 'city': 'Surabaya'}
person_3 = {'first_name': 'Citra', 'last_name': 'Lestari', 'age': 18, 'city': 'Jakarta'}

# Menyimpan ketiga dictionary ke dalam sebuah list
people = [person_1, person_2, person_3]

# Menelusuri list orang satu per satu
for person in people:
    print(f"Nama Lengkap : {person['first_name']} {person['last_name']}")
    print(f"Umur         : {person['age']} tahun")
    print(f"Kota Asal    : {person['city']}")
    print("-" * 25)  # Garis pembatas