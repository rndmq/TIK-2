import math
import sys
import time

def print_lama(teks, jeda_biasa=0.011, jeda_titik=0.1):
# bonus visual cerita ajah.
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        
        if karakter == ".":
            time.sleep(jeda_titik)
        else:
            time.sleep(jeda_biasa)
    print()

print_lama("Program menghitung luas oleh Sultanto\n\nMenu:\n1. Menghitung luas persegi\n2. Menghitung luas lingkaran")

def nomor():
    while True:
        try:
            nomor_menu = int(input("Masukkan nomor menu: "))

            if nomor_menu > 2 or nomor_menu < 1:
                print_lama("Nomor yang anda masukkan salah.")
                print_lama("Tolong coba lagi.")
                continue
            else:
                break

        except ValueError:
            print_lama("Input harus berupa angka.")

    return nomor_menu

nomor_menu = nomor()

def lingkaran():
    while True:
        try:
            satuan_nanya = int(input(
                "Masukkan jenis satuan\n"
                "1 = km\n"
                "2 = m\n"
                "3 = cm\n"
                "Pilihan: "
            ))

            r = float(input("Masukkan radius: "))

            if satuan_nanya == 1:
                satuan = "km²"
                luas = math.pi * r ** 2

            elif satuan_nanya == 2:
                satuan = "m²"
                luas = math.pi * r ** 2

            elif satuan_nanya == 3:
                satuan = "cm²"
                luas = math.pi * r ** 2

            else:
                print_lama("Input tidak valid, Tolong coba lagi")
                continue

            return luas, satuan

        except ValueError:
            print_lama("Input tidak valid, Tolong coba lagi")


def persegi():
    while True:
        try:
            satuan_nanya = int(input(
                "Masukkan jenis satuan\n"
                "1 = km\n"
                "2 = m\n"
                "3 = cm\n"
                "Pilihan: "
            ))

            sisi = float(input("Masukkan sisi: "))

            if satuan_nanya == 1:
                satuan = "km²"
                luas = sisi ** 2

            elif satuan_nanya == 2:
                satuan = "m²"
                luas = sisi ** 2

            elif satuan_nanya == 3:
                satuan = "cm²"
                luas = sisi ** 2

            else:
                print_lama("Input tidak valid, Tolong coba lagi")
                continue

            return luas, satuan

        except ValueError:
            print_lama("Input tidak valid, Tolong coba lagi")


if nomor_menu == 2:
  luas, satuan = lingkaran()
  print_lama(f"Luas lingkaran = {luas:.2f} {satuan}")
elif nomor_menu == 1:
  luas, satuan = persegi()
  print_lama(f"Luas persegi = {luas:.2f} {satuan}")
else:
    print_lama("An error accured")

    
