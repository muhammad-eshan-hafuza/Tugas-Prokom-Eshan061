prompt = "\nBerapa usia Anda? (Ketik 'quit' untuk berhenti): "

while True:
    usia_input = input(prompt)
    
    # Jika pengguna mengetik 'quit', hentikan perulangan
    if usia_input == 'quit':
        print("Terima kasih telah berkunjung!")
        break
    
    # Konversi input ke angka
    usia = int(usia_input)
    
    if usia < 3:
        print("Harga tiket: GRATIS!")
    elif usia <= 12:
        print("Harga tiket: $10")
    else:
        print("Harga tiket: $15")