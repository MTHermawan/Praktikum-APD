import os
os.system("cls")

def LihatData():
    for i, mahasiswa in enumerate(data_mahasiswa):
            nim = mahasiswa[0]
            nama = mahasiswa[1]
            print(f"{i+1}. {nim} {nama}")


data_mahasiswa = [
    ["060", "Trigusni"],
    ["061", "Hermawan"]
]

pref = "2409106"

while True:
    os.system("cls || clear")

    print("""
Menu
1. Lihat Data
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Keluar
    """)
    
    
    pilihan = input("Masukkan pilihan Anda: ")
    
    if (pilihan == "1"):
        LihatData()
    elif (pilihan == "2"):
        nim = input("Masukkan NIM Anda: ")
        nama = input("Masukkan Nama Anda: ")
        data = [nim, nama]
        data_mahasiswa.append(data)
        print("Data berhasil ditambahkan")
    elif (pilihan == "3"):
        LihatData()
        
        pilihan_mahasiswa = int(input("Pilih Mahasiswa: ")) - 1
        data_mahasiswa[pilihan_mahasiswa][0] = input("Masukkan NIM baru: ")
        data_mahasiswa[pilihan_mahasiswa][1] = input("Masukkan Nama baru: ")
    elif (pilihan == "4"):
        LihatData()
        
        pilihan_mahasiswa = int(input("Pilih Mahasiswa: ")) - 1
        mahasiswa_dihapus = data_mahasiswa.pop(pilihan_mahasiswa)
    elif (pilihan == "5"):
        break
    input("...")