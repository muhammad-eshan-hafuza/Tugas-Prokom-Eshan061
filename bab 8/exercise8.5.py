def describe_city(city, country="Indonesia"):
    """Menjelaskan kota dan negara tempat kota itu berada."""
    print(f"{city} berada di negara {country}.")

# Dua kota di Indonesia (menggunakan nilai default)
describe_city("Bandung")
describe_city("Surabaya")

# Satu kota di luar Indonesia (menimpa nilai default)
describe_city("Tokyo", "Jepang")