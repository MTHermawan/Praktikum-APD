import os

os.system("cls || clear")
# try:
#     angka = int(input("Masukkan angka: "))
# except:
#     print("Input bukan angka!")
# else:
#     print(f"Input Anda adalah: {angka}")
# finally:
#     print("Program Selesai")

# ===============================================

# try:
#     nama = input("Masukkan nama Anda: ")
#     if (len(nama) > 5):
#         raise ValueError("Nama tidak boleh lebih dari 5 karakter!")
# except ValueError as e:
#     print(e)

# ===============================================

def InputString():
    try:
        nama = input("Masukkan nama Anda: ")
        if (not nama.strip()):
            raise ValueError("Nama tidak boleh kosong!")
        elif (not nama.isalpha()):
            raise ValueError("Nama tidak boleh angka!")
        return nama
    except ValueError as e:
        print(e)
        return InputString()

print(InputString())