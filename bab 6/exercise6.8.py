pet_1 = {'animal': 'kucing', 'owner': 'Rina'}
pet_2 = {'animal': 'anjing', 'owner': 'Doni'}
pet_3 = {'animal': 'kelinci', 'owner': 'Maya'}

# Menyimpan ke dalam list
pets = [pet_1, pet_2, pet_3]

# Mencetak informasi tiap hewan
for pet in pets:
    print(f"Pemilik : {pet['owner']}")
    print(f"Hewan   : {pet['animal'].title()}\n")