skalaMatriks = 8
print("Matriks")
for baris in range(skalaMatriks):
    for kolom in range(skalaMatriks):
        print("*", end=" ")
    print()
print()


skalaSegitigaSikuSiku = 8
print("Segitiga Siku-Siku")
for baris in range(skalaSegitigaSikuSiku):
    for kolom in range(skalaSegitigaSikuSiku):
        if kolom < baris + 1:
            print("*", end=" ")
    print()
print()

print("Segitiga Sama Kaki")

skalaSegitigaSamaKaki = 8
for baris in range(skalaSegitigaSamaKaki, 0, -1):
    for kolom in range(skalaSegitigaSamaKaki):
        if kolom < baris - 1:
            print(end=" ")
        else:
            print("*", end=" ")
    print()
print()