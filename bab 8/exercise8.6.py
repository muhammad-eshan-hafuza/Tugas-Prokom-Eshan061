def city_country(city, country):
    """Mengembalikan string gabungan kota dan negara."""
    return f"{city}, {country}"

# Panggil fungsi dan print nilai kembaliannya
lokasi1 = city_country("Santiago", "Chile")
lokasi2 = city_country("Jakarta", "Indonesia")
lokasi3 = city_country("Paris", "Prancis")

print(lokasi1)
print(lokasi2)
print(lokasi3)