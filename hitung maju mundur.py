import time

hitung = int(input("masukkan angka: "))
while hitung > 0:
    if hitung == 5:
        print("bersiap")
    print("hitung = ",hitung)
    hitung -= 1
    time.sleep(1)
print("happy new year 2022")