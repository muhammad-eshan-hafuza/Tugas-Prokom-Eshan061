rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'kapuas': 'indonesia'
}

# 1. Cetak kalimat lengkap
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

# 2. Cetak hanya nama sungainya
print("\nDaftar nama sungai:")
for river in rivers.keys():
    print(f"- {river.title()}")

# 3. Cetak hanya nama negaranya
print("\nDaftar nama negara:")
for country in rivers.values():
    print(f"- {country.title()}")