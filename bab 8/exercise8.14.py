def make_car(manufacturer, model, **car_info):
    """Menyimpan spesifikasi mobil ke dalam dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# Contoh pemanggilan sesuai soal
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)