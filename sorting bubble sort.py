masuk = [0] * (5)

for i in range(0, 4 + 1, 1):
    print("masukkan angka : ")
    masuk[i] = int(input())
print("list awal sebelum di urutkan = {", end='', flush=True)
for i in range(0, 3 + 1, 1):
    print(str(masuk[i]) + ", ", end='', flush=True)
print(str(masuk[4]) + "}")
for a in range(0, 3 + 1, 1):
    for b in range(a + 1, 4 + 1, 1):
        if masuk[a] > masuk[b]:
            z = masuk[a]
            masuk[a] = masuk[b]
            masuk[b] = z
print("list sesudah diurutkan= [", end='', flush=True)
for i in range(0, 3 + 1, 1):
    print(str(masuk[i]) + ", ", end='', flush=True)
print(str(masuk[4]) + "]")
