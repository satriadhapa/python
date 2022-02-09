import math

# a = math.pi
# b = int(input("angka: "))
# c = a * b
# d = math.e

# print(d)

a = abs(-202) # fungsi abs untuk mengembalikan nilai mutlak suatu angka
b = pow(2, 8) # perhitungan perpangkatan
c = round(23.22) # membulatkan ke angka yang terdekat
d = min(20, 22, 4 , 12, 1, 0.2) # fungsi min mencari nilai terkecil dari sekumpulan angka
e = max(20, 3, 41, 53,a, b) # fungsi max mencari nilai terbesar dair sekumpulan angka

# nama = "satria\tdhapa\thamdani"
# py = str(10)
# sat = "dhapa"
# dhap = py + str(sat)

# kalimat = "mochsatriadhapahamdani"
# if "a" in kalimat:
#     print(len("a"))
#     print(True)
# else:
#     print(False)

uang = int(input("berapa uang anda : "))
hutang = 20000

if uang > hutang:
    print("hutang sudah di bayar!!")
    print("kembalian ", uang - hutang)
elif uang == hutang:
    print("uang anda pas")
    print("hutang nya sudah lunas")
else:
    print("uang tidak cukup untuk bayar hutang")