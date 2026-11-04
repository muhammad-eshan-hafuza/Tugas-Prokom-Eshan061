prompt = "\nMasukkan topping pizza yang Anda inginkan (ketik 'quit' jika selesai): "

topping = ""
# Perulangan berjalan selama nilai topping BUKAN 'quit'
while topping != 'quit':
    topping = input(prompt)
    
    # Pastikan kata 'quit' tidak ikut dicetak sebagai topping
    if topping != 'quit':
        print(f"Saya akan menambahkan topping {topping} ke pizza Anda!")