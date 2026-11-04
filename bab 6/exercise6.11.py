cities = {
    'jakarta': {
        'country': 'Indonesia',
        'population': '10.5 juta',
        'fact': 'Pusat perekonomian terbesar di Indonesia.'
    },
    'tokyo': {
        'country': 'Jepang',
        'population': '14 juta',
        'fact': 'Memiliki jaringan stasiun kereta api tersibuk di dunia.'
    },
    'stuttgart': {
        'country': 'Jerman',
        'population': '630 ribu',
        'fact': 'Pusat industri manufaktur dan otomotif terkemuka di Eropa.'
    }
}

# Menampilkan informasi kota secara terstruktur
for city, info in cities.items():
    print(f"Kota: {city.title()}")
    print(f"  Negara   : {info['country']}")
    print(f"  Populasi : {info['population']}")
    print(f"  Fakta    : {info['fact']}\n")