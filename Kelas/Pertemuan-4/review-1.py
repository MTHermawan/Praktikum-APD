print("Matriks")
for baris in range(5):
    for kolom in range(5):
        print("*", end=" ")
    print()
print()

print("Segitiga Siku-Siku")
for baris in range(5):
    for kolom in range(5):
        if kolom < baris + 1:
            print("*", end=" ")
    print()
print()

print("Segitiga Sama Kaki")

panjangBaris = 5
panjangKolom = 5
while panjangBaris >= 0:
    for kolom in range(panjangKolom):
        if kolom < panjangBaris:
            print(end=" ")
        else:
            print("*", end=" ")
    print()
    panjangBaris -= 1
print()