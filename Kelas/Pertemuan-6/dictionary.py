# Deklarasi Variabel Dictionary
daftar_buku_1 = {
    "Buku1" : "Harry Potter",
    "Buku2" : "Percy Jackson",
    "Buku3" : "Twillight",
    }

print(daftar_buku_1["Buku1"])
print(daftar_buku_1["Buku2"])
print(daftar_buku_1["Buku3"])
print()
#=======================================
# Apabila key sama, maka akan menggunakan yang terakhir (menimpa yang lama)
daftar_buku_2 = {
    "Buku1" : "Harry Potter",
    "Buku1" : "Harry",
    "Buku2" : "Percy Jackson",
    "Buku3" : "Twillight",
    }

print(daftar_buku_2)
print()
#=======================================
# Perulangan pada dictionary
biodata_1 = {
    "nama" : "Hermawan",
    "nim" : "2409106060",
    }

for i, j in biodata_1.items():
    print(f"{i} : {j}")
print()
#=======================================
# Mengubah item pada dictonary
biodata_2 = {
    "nama" : "Hermawan",
    "nim" : "2409106060",
    "asal" : "Samarinda",
    }
print(biodata_2["asal"])

biodata_2["asal"] = "Tenggarong"
print(biodata_2["asal"])

biodata_2.update({"asal":"Tegal"})
print(biodata_2["asal"])
print()
#=======================================
# Menghapus item pada dictonary
biodata_3 = {
    "nama" : "Hermawan",
    "nim" : "2409106060",
    "asal" : "Samarinda",
    }
print(biodata_3)

# Menghapus item dari dictionary tanpa jejak
del biodata_3["asal"]
print(biodata_3)

# Memanipulasi memperbarui teks key dengan pop
cache = biodata_3.pop("nim")
biodata_3["NIM"] = cache
print(biodata_3)

# Menghapus semua item dari dictionary
print(biodata_3.clear())
print()
#=======================================
# Menghitung panjang item dictionary

biodata_4 = {
    "nama" : "Hermawan",
    "nim" : "2409106060",
    "asal" : "Samarinda",
    }
print(len(biodata_4))
print()
#=======================================
# Menyalin dictionary variabel lain

biodata_5 = {
    "nama" : "Hermawan",
    "nim" : "2409106060",
    "asal" : "Samarinda",
    }
biodata_5_copy = biodata_5.copy()
print(biodata_5_copy)
print()
#=======================================
# Pengulangan yang hanya mencetak key atau value saja
biodata_6 = {
    "nama" : "Hermawan",
    "nim" : "2409106060",
    "asal" : "Samarinda",
    }

print("Keys:")
for key in biodata_6.keys():
    print(key, end=" ")
print()
print("Values:")
for value in biodata_6.values():
    print(value, end=" ")
print("\n")
#=======================================
# Kuis: Mengakses value Pak Awang dalam dictionary di bawah (Nested Dictionary)
biodata_7 = {
    "nama" : "Hermawan",
    "nim" : "2409106060",
    "asal" : "Samarinda",
    "dosen" : {
        "nama" : "Pak Awang",
        "matkul" : "APD",
    }
    }

print(f"Nama Dosen: {biodata_7['dosen']['nama']}")
print(f"Matkul: {biodata_7['dosen']['matkul']}")
print()
#=======================================
# Implementasi dalam data akun
akun = [
    {
        "nama" : "Admin",
        "role" : "admin"
    },
    {
        "nama" : "Hermawan",
        "role" : "user"
    }
]

# Mencetak nama akun pertama
print(akun[0]["nama"])