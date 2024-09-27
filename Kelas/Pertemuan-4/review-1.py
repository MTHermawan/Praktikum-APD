print("Matriks")
skalaMatriks = 8
for baris in range(skalaMatriks):
    for kolom in range(skalaMatriks):
        print("*", end=" ")
    print()
print()

#=====================================================

print("Segitiga Siku-Siku")
skalaSegitigaSikuSiku = 8
for baris in range(skalaSegitigaSikuSiku):
    for kolom in range(skalaSegitigaSikuSiku):
        if kolom < baris + 1:
            print("*", end=" ")
    print()
print()

#=====================================================

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