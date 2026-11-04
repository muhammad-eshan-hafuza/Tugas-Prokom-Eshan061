prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"Menambahkan {topping}...")
        
        
    
        
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

# Saklar aktif
aktif = True

while aktif:
    topping = input(prompt)
    if topping == 'quit':
        aktif = False  # Mematikan saklar agar loop berhenti di putaran berikutnya
    else:
        print(f"Menambahkan {topping}...")
        
        
        
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break  # Langsung melompat keluar dari perulangan
    print(f"Menambahkan {topping}...")