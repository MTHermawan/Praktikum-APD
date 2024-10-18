import os
data_mahasiswa =["Ifnu","Adi","ucup","michael"]

def clear_screen():
    os.system('cls || clear')

clear_screen()

def tampilkan_mahasiswa():
    for i in range(len(data_mahasiswa)):
        print(f"data ke {i+1}")
        print(f"Nama : {data_mahasiswa[i]}")
        print("="*10)

def tambah_data():
    print("MENU TAMBAH DATA")
    print("=" * 10)
    inputUser = input("Data yang mau ditambahkan : ")
    return inputUser

def ubah_data():
    index= int(input("masukkan index yang mau diedit : "))
    data_baru =input("masukkan nama anda :")
    return data_baru
    # data_mahasiswa[index-1]=data_baru
    # print("data berhasil diubah")

def pilih_data():
    index_user = int(input("masukkan index yang ingin dihapus: "))
    return index_user - 1
    print(f"{del_user} telah dihapus")

def menu():
    print("""
    Menu
Lihat Data  >> 1
Tambah Data >> 2
Edit Data   >> 3
Hapus Data  >> 4
Keluar      >> 5
""")

while True:
    menu()
    pilih = input("Masukan Pilihan menu >> ")
    clear_screen()
    match(pilih):
        case "1":
            print("===Lihat Data===")
            tampilkan_mahasiswa()
            input("Enter.....")
            clear_screen()
        case "2":
            mahasiswaBaru = tambah_data()
            data_mahasiswa.append(mahasiswaBaru)
            input("Enter....")
            clear_screen()
        case "3":
            print("Menu ubah data")
            tampilkan_mahasiswa()
            dataBaru = ubah_data()
            data_mahasiswa[i-1] = dataBaru
            input("Enter.....")
            clear_screen()
        case "4":
            print("Menu Hapus Data")
            tampilkan_mahasiswa()
            mahasiswa = pilih_data()
            del_user = data_mahasiswa.pop(mahasiswa)
            input("Enter......")
            clear_screen()
        case "5":
            print("Anda memilih menu 5")
            exit()
        case _:
            print(f"Menu {pilih} tidak tersedia")
            input("Enter.....")