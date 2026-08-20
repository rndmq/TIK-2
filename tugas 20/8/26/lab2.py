posisi_awal = (0, 0)
import sys
import time
def print_lama(teks, jeda_biasa=0.01, jeda_titik=0.6):
# bonus visual cerita ajah.
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        
        if karakter == ".":
            time.sleep(jeda_titik)
        else:
            time.sleep(jeda_biasa)
    print()
while True:
 try:
  global loop_pengulangan
  loop_pengulangan = int(input("Banyak perintah: "))
  
  if loop_pengulangan < 0:
        print_lama("Jumlah pengulangan harus lebih dari 0. Silakan coba lagi.")
        continue
  break
 except ValueError:
    print_lama("Input tidak valid. Silakan masukkan angka bulat.")         



def nama():
    print_lama("""
██    ██ ███████ ███    ███ ██ ███    ███  █████
██    ██ ██      ████  ████ ██ ████  ████ ██   ██
██    ██ █████   ██ ████ ██ ██ ██ ████ ██ ███████
 ██  ██  ██      ██  ██  ██ ██ ██  ██  ██ ██   ██
  ████   ███████ ██      ██ ██ ██      ██ ██   ██
   ██
   ██
""", jeda_biasa=0.001)

    print_lama("""
███████╗██╗   ██╗██╗  ████████╗ █████╗ ███╗   ██╗████████╗ ██████╗
██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗
███████╗██║   ██║██║     ██║   ███████║██╔██╗ ██║   ██║   ██║   ██║
╚════██║██║   ██║██║     ██║   ██╔══██║██║╚██╗██║   ██║   ██║   ██║
███████║╚██████╔╝███████╗██║   ██║  ██║██║ ╚████║   ██║   ╚██████╔╝
╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝
""", jeda_biasa=0.001)

    print_lama("""
███╗   ██╗██╗ ██████╗██╗  ██╗ ██████╗
████╗  ██║██║██╔════╝██║  ██║██╔═══██╗
██╔██╗ ██║██║██║     ███████║██║   ██║
██║╚██╗██║██║██║     ██╔══██║██║   ██║
██║ ╚████║██║╚██████╗██║  ██║╚██████╔╝
╚═╝  ╚═══╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝
""", jeda_biasa=0.001)
def langkah_kucing(arah):
    global posisi_awal
    x, y = posisi_awal
    if arah == "U":
        y += 1
    elif arah == "S":
        y -= 1
    elif arah == "T":
        x += 1
    elif arah == "B":
        x -= 1
    else:
        print_lama("Arah tidak valid. Gunakan U, S, T, atau B.")
        return

    posisi_awal = (x, y)

print_lama("Informasi arah kucing: U = atas, S = bawah, T = kanan, B = kiri, & HOME untuk berhenti")
for i in range(loop_pengulangan):
    arah = input(f"Masukkan perintah-{i + 1}: ")
    if arah == "HOME":
        break
    else:
        langkah_kucing(arah)

print_lama(f"Karakter Meong Brosss berada di koordinat {posisi_awal}")
nama()