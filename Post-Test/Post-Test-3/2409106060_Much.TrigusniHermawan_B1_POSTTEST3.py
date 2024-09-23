import os

os.system('cls') # Fungsi membersihkan Layar Terminal

# Deklarasi Variabel
pilihan = ""

# Mencetak Pilihan Menu Operasi Yang Tersedia
print(f"""
==========================================================
    Menu Program Menghitung Luas/Volume Bangun Ruang
==========================================================
1. Luas Balok
2. Volume Balok
N. Keluar Program
""")

pilihan = input("Masukkan nomor pilihan menu: ")

if pilihan == "1":
    print("\n======================= Luas Balok =======================\n")
    panjang = int(input("Masukkan nilai Panjang (cm): "))
    lebar = int(input("Masukkan nilai Lebar (cm): "))
    tinggi = int(input("Masukkan nilai Tinggi (cm): "))

    # Mencetak hasil dengan rumus luas balok: 2pl + 2pt + 2lt
    hasil = 2 * panjang * lebar + 2 * panjang * tinggi + 2 * lebar * tinggi
    print(f"""
Penyelesaian:
Panjang = {panjang} cm
Lebar = {lebar} cm
Tinggi = {tinggi} cm

Luas Balok = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
Luas Balok = (2 * {panjang} * {lebar}) + (2 * {panjang} * {tinggi}) + (2 * {lebar} * {tinggi})
Luas Balok = {2 * panjang * lebar} + {2 * panjang * tinggi} + {2 * lebar * tinggi}
Luas Balok = {hasil} cm³
    """)
elif pilihan == "2":
    panjang = int(input("Masukkan nilai Panjang: "))
    lebar = int(input("Masukkan nilai Lebar: "))
    tinggi = int(input("Masukkan nilai Tinggi: "))

    # Rumus Volume Balok: p x l x t
    print(panjang * lebar * tinggi)
elif pilihan.lower() == "n":
    print("\nProgram berhasil dihentikan!\n")
else:
    print("\nTidak ada pilihan menu yang cocok!")