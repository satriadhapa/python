import math

# Fungsi untuk penjumlahan
def add(x, y):
   return x + y

# Fungsi untuk pengurangan
def subtract(x, y):
   return x - y

# Fungsi untuk perkalian
def multiply(x, y):
   return x * y

# Fungsi untuk pembagian
def divide(x, y):
   return x / y

# Fungsi untuk logaritma
def logarithm(x, base):
   return math.log(x, base)

print("Pilih operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
print("5.Logaritma")

# Meminta input dari pengguna
choice = input("Masukkan pilihan(1/2/3/4/5): ")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   base = int(input("Masukkan basis logaritma: "))
   print("log", num1, "base", base, "=", logarithm(num1, base))

else:
   print("Input salah")