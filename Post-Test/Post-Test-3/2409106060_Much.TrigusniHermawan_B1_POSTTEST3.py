import os

os.system('cls') # Fungsi membersihkan Layar Terminal

# Mencetak Pilihan Menu Operasi Yang Tersedia
print("""
==========================================================
    Menu Program Menghitung Luas/Keliling Bangun Ruang
==========================================================
1. Luas Permukaan Balok
2. Keliling Balok
3. Luas Permukaan Bola
4. Luas Permukaan Limas Segi Empat (Beraturan)
N. Keluar Program
""")

pilihan = input("Masukkan nomor pilihan menu: ")

if pilihan == "1":
    print("\n================== Luas Permukaan Balok ==================\n")
    
    panjang = float(input("Masukkan nilai panjang balok (cm): "))
    lebar = float(input("Masukkan nilai lebar balok (cm): "))
    tinggi = float(input("Masukkan nilai tinggi balok (cm): "))

    hasil = 2 * panjang * lebar + 2 * panjang * tinggi + 2 * lebar * tinggi
    
    print("\n---------------------- Penyelesaian ----------------------\n")
    print(f"Panjang = {panjang} cm\nLebar = {lebar} cm\nTinggi = {tinggi} cm\n")
    print(f"Luas Balok = (2 x panjang x lebar) + (2 x panjang x tinggi) + (2 x lebar x tinggi)")
    print(f"Luas Balok = (2 x {panjang} x {lebar}) + (2 x {panjang} x {tinggi}) + (2 x {lebar} x {tinggi})")
    print(f"Luas Balok = {2 * panjang * lebar} + {2 * panjang * tinggi} + {2 * lebar * tinggi}")
    print(f"Luas Balok = {hasil} cm²\n")

elif pilihan == "2":
    print("\n===================== Keliling Balok =====================\n")
    
    panjang = float(input("Masukkan nilai panjang balok (cm): "))
    lebar = float(input("Masukkan nilai lebar balok (cm): "))
    tinggi = float(input("Masukkan nilai tinggi balok (cm): "))

    hasil = 4 * (panjang + lebar + tinggi)
    
    print("\n---------------------- Penyelesaian ----------------------\n")
    print(f"Panjang = {panjang} cm\nLebar = {lebar} cm\nTinggi = {tinggi} cm\n")
    print(f"Keliling Balok = 4 x (panjang + lebar + tinggi)")
    print(f"Keliling Balok = 4 x ({panjang} + {lebar} + {tinggi})")
    print(f"Keliling Balok = 4 x {panjang + lebar + tinggi}")
    print(f"Keliling Balok = {hasil} cm\n")

elif pilihan == "3":
    print("\n================== Luas Permukaan Bola ===================\n")
    
    radius = float(input("Masukkan nilai jari-jari/radius bola (cm): "))

    hasil = 4 * 3.14 * (radius ** 2)
    
    print("\n---------------------- Penyelesaian ----------------------\n")
    print(f"r = {radius} cm\n")
    print(f"Luas Bola = 4 x π x r²")
    print(f"Luas Bola = 4 x 3.14 x {radius}²")
    print(f"Luas Bola = {4 * 3.14} x {radius ** 2}")
    print(f"Luas Bola = {hasil} cm²\n")

    exec

elif pilihan == "4":
    print("\n====== Luas Permukaan Limas Segi Empat (Beraturan) =======\n")
    
    panjangAlas = float(input("Masukkan nilai panjang sisi alas/persegi (cm): "))
    tinggiSisiTegak = float(input("Masukkan nilai tinggi sisi tegak/segitiga (cm): "))

    hasil = (panjangAlas * panjangAlas) + (4 * panjangAlas * tinggiSisiTegak / 2) 
    
    print("\n---------------------- Penyelesaian ----------------------\n")
    print(f"Panjang Alas = {panjangAlas} cm\nTinggi Sisi Tegak = {tinggiSisiTegak} cm\n")
    print(f"Luas Limas Segi Empat = Luas Alas + (4 x panjang alas * tinggi sisi tegak)")
    print(f"Luas Limas Segi Empat = ({panjangAlas} x {panjangAlas}) + (4 x {panjangAlas} x {tinggiSisiTegak} / 2)")
    print(f"Luas Limas Segi Empat = ({panjangAlas * panjangAlas}) + ({4 * panjangAlas * tinggiSisiTegak / 2})")
    print(f"Luas Limas Segi Empat = {hasil} cm²\n")

elif pilihan.lower() == "n":
    print("\nProgram berhasil dihentikan!")

else:
    print("\nTidak ada pilihan menu yang cocok!")

print("========================== END ===========================")