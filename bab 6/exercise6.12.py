#(Studi Kasus: Monitoring Mesin Pabrik)
factory_machines = {
    'Mesin CNC-01': {
        'tipe': 'Milling 5-Axis',
        'operator': 'Pak Joko',
        'kapasitas_per_jam': 120,
        'status': 'Beroperasi Normal'
    },
    'Mesin Press-A': {
        'tipe': 'Hydraulic Press 50 Ton',
        'operator': 'Pak Hendra',
        'kapasitas_per_jam': 300,
        'status': 'Maintenance (Perbaikan)'
    },
    'Mesin Robot-Arm': {
        'tipe': 'Welding Assembly',
        'operator': 'Siti Rahma',
        'kapasitas_per_jam': 250,
        'status': 'Beroperasi Normal'
    }
}

print("=== SISTEM INFORMASI MESIN LANTAI PRODUKSI ===")
print("=" * 46)

for mesin, data in factory_machines.items():
    print(f"ID Mesin          : {mesin}")
    print(f"  Tipe Mesin      : {data['tipe']}")
    print(f"  Nama Operator   : {data['operator']}")
    print(f"  Output Standar  : {data['kapasitas_per_jam']} unit/jam")
    print(f"  Status Operasi  : {data['status']}")
    print("-" * 46)