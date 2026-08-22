x = 0
y = 0
jumlah_perintah = int(input("Masukkan jumlah perintah = "))
for i in range(jumlah_perintah):
    while True:
        perintah = input("Masukkan perintah = ")
        if perintah.lower() == "u":
            y += 1
            break
        elif perintah.lower() == "s":
            y -= 1
            break
        elif perintah.lower() == "t":
            x += 1
            break
        elif perintah.lower() == "b":
            x -= 1
            break
        else:
            print("Masukkan perintah dengan benar")
print(f"Meong Boss berada di {x},{y}")
