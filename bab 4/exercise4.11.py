# List asli
pizzas = ['pepperoni', 'margherita', 'keju']

# Menyalin list pizza menggunakan [:]
friend_pizzas = pizzas[:]

# Menambahkan pizza berbeda ke masing-masing list
pizzas.append('jamur')
friend_pizzas.append('sosis')

# Menampilkan pizza favorit saya
print("Pizza favorit saya adalah:")
for pizza in pizzas:
    print(f"- {pizza}")

# Menampilkan pizza favorit teman
print("\nPizza favorit teman saya adalah:")
for pizza in friend_pizzas:
    print(f"- {pizza}")