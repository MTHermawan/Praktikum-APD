# Pengenalan List
data_1 = [1, 2, 3, 4, 5]

print(data_1)
print(type(data_1))

print("===============================================")
#===============================================

# Nested List
data_2 = [1, 2, True, [2, 3], 5, "string"]

print(data_2[3][0]) # Output: 2

print("===============================================")
#===============================================

# Menambahkan Data Baru pada List
data_3 = ["Apel", "Durian", "Jeruk"]

print(data_3)
print()

# Menambahkan Data ke paling belakang
data_3.append("Semangka")
# Menambahkan Data berdasarkan index
data_3.insert(0, "Rambutan")

print(data_3)

print("===============================================")
#===============================================

# Mengubah data dalam list
data_4 = ["Apel", "Durian", "Jeruk"]

print(data_4)
print()
data_4[0:2] = "Anggur", "Semangka"
print(data_4)

print("===============================================")
#===============================================
# Mengahapus nilai list
data_5 = ["Apel", "Durian", "Jeruk"]

print(data_5)

# Menghapus nilai array
del data_5[2]
# Menghapus nilai array dengan menyebutkan indeksnya dan menyimpannya dalam variabel
nilai_hapus_data_5_pop = data_5.pop(1)
# Menghapus nilai array dengan menyebutkan spesifik nilainya dan menyimpannya dalam variabel
nilai_hapus_data_5_remove = data_5.remove("Apel")

print(data_5)
print(nilai_hapus_data_5_pop)
print(nilai_hapus_data_5_remove)

print("===============================================")
#===============================================
# Mengahapus nilai list
data_6 = ["Apel", "Durian", "Jeruk"]

print(data_6*3)
print("="*3)

print("===============================================")
#===============================================
# Mengakses List dalam List
data_7 = [
    ["060", "Trigusni", ["APD", "ORSIKUM"]],
    ["060", "Hermawan"]
]

print(data_7[0][2][0]) # Output: "APD"

print("===============================================")
#===============================================
# Mengakses List dalam List dengan impementasi akun
data_8 = [
    ["Admin", "admin123", "admin"],
    ["user", "user123", "user"]
]

print(data_8)

print("===============================================")
#===============================================

# Menampilkan List dengan perulangan
buah = ["Apel", "Durian", "Jeruk"]

index = 1
for data in buah:
    print(f"Data ke {index}")
    print(data)
    print("="*50)
    index += 1

for index, item in enumerate(buah):
    print(f"Data ke {index}")
    print(item)
    print("="*50)

print("===============================================")
#===============================================

#
data_mahasiswa = [
    ["Admin", "admin123", "admin"],
["user", "user123", "user"]
]

for index, item in enumerate(data_mahasiswa):
    print(f"Data ke {index}")
    print(item)
    print("="*50)


