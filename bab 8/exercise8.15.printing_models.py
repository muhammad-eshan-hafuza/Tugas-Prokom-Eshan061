# File: printing_models.py
# Mengambil fungsi dari file printing_functions.py
import printing_functions as pf

desain_belum_cetak = ['casing hp', 'liontin robot', 'kotak pensil']
desain_selesai = []

pf.print_models(desain_belum_cetak, desain_selesai)
pf.show_completed_models(desain_selesai)