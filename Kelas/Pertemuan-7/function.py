import os
os.system('cls || clear')

#========================================
print("======================================")
print("Deklarasi Fungsi")
print()

def hasil(nama):
    print("Nama " + nama)

hasil("Trigusni")
hasil("Hermawan")
#========================================
print("======================================")
print("Local Variable")
print()
# Variabel sementara yang hanya berlaku dalam fungsi

def LuasPersegiPanjang(panjang, lebar):
    luas = panjang * lebar
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

LuasPersegiPanjang(2, 5)
#========================================
print("======================================")
print("Default Parameter Value")
print()

def LuasPersegiPanjang(panjang, lebar = 5):
    luas = panjang * lebar
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

LuasPersegiPanjang(2)
#========================================
print("======================================")
print("Return Value")
print()

def LuasPersegiPanjang(panjang, lebar = 5):
    luas = panjang * lebar
    # print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

    return luas

luasPersegi = LuasPersegiPanjang(2)
print(f"Luas persegi panjang dengan adalah {luasPersegi}")
#========================================
print("======================================")
print("Return Value")
print()

def LuasPersegiPanjang(panjang, lebar = 5):
    luas = panjang * lebar
    # print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

    return luas

luasPersegi = LuasPersegiPanjang(2)
print(f"Luas persegi panjang dengan adalah {luasPersegi}")
#========================================
print("======================================")
print("Global and Local Variable")
print()

nama = "Trigusni"

def say_hello():
    nama = "Hermawan"
    print(nama, "dalam fungsi")

print(nama, "luar fungsi")
say_hello()

print(nama)
#========================================
print("======================================")
print("Global and Local Variable")
print()

nama = "Trigusni"

def say_hello():
    nama = "Hermawan"
    print(nama, " dalam fungsi")

print(nama, "luar fungsi")
say_hello()
#========================================
