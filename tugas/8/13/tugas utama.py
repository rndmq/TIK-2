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

nama_siswa = "Yemima"
print_lama("program cek kategori TKA bahasa indonesia bahasa indonesia oleh: " + nama_siswa)
nilai = float(input("Masukkan nilai TKA bahasa indonesia kamu: "))
predikat = ""
predikat_istimewa = "Murid mampu mengevaluasi dan mengapresiasi isi teks, baik dengan menilai keakuratan informasi dan ketepatan penggunaan bahasa dalam teks informasi maupun menilai kesesuaian penggambaran karakter/peristiwa dalam teks fiksi, serta menilai relevansi informasi/peristiwa dalam teks informasi dan teks fiksi dengan kehidupan dunia nyata (baik kehidupan sehari-hari di sekitarnya maupun kehidupan bermasyarakat)."
predikat_baik = "Murid mampu mengintegrasikan dan/atau membandingkan hubungan antarkalimat atau antarparagraf, serta memprediksi kemungkinan peristiwa di masa mendatang berdasarkan informasi penting dalam teks informasi atau kemungkinan akhir cerita dalam teks fiksi."
predikat_memadai = "Murid mampu menyusun kerangka atau kronologis informasi/peristiwa penting, serta mulai mampu menginterpretasi/menyimpulkan informasi implisit (ide pokok, ide pendukung, konflik, nilai-nilai, dsb) dalam teks informasi dan teks fiksi."
predikat_kurang = "Murid hanya mampu mengidentifikasi makna kosakata (baik kata serapan maupun kata konotatif/kiasan), serta menyusun kerangka atau kronologis informasi/peristiwa penting dalam teks informasi dan teks fiksi."



if nilai >= 95:
    predikat = "Istimewa"
    print(f"Predikat: {predikat}")
    print_lama(f"{predikat_istimewa}")
elif nilai >= 76.67:
    predikat = "Baik"
    print(f"Predikat: {predikat}")
    print_lama(f"{predikat_baik}")
elif nilai >= 50:   
    predikat = "Memadai"
    print(f"Predikat: {predikat}")
    print_lama(f"{predikat_memadai}")
else:
    predikat = "Kurang"
    print(f"Predikat: {predikat}")
    print_lama(f"{predikat_kurang}")