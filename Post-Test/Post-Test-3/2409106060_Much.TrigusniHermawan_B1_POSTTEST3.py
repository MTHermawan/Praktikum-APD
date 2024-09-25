import os # Mengambil library untuk menggunakan fungsi tambahan

os.system('cls') # Membersihkan Layar Terminal

# Mencetak plihan menu operasi yang tersedia
print("""
==========================================================
    Menu Program Menghitung Luas/Keliling Bangun Ruang
==========================================================
1. Luas Permukaan Limas Segi Empat (Beraturan)
2. Keliling Balok
3. Luas Permukaan Balok
4. Luas Permukaan Bola
N. Keluar Program
""")

# Meminta user untuk memilih menu dan menyimpannya di variabel pilihan
pilihan = input("Masukkan nomor pilihan menu: ") 

# Percabangan yang menentukan alur program menghitung berdasarkan pilihan user
if pilihan == "1": # Jika pilihan user adalah "1", maka program akan menghitung Luas Permukaan Limas Segi Empat (Beraturan)
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

elif pilihan == "2": # Jika pilihan bukan "1", tetapi pilihan adalah "2", maka akan menghitung Keliling Balok
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

elif pilihan == "3": # Jika pilihan bukan "2", tetapi pilihan adalah "3", maka akan menghitung Luas Permukaan Balok
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

elif pilihan == "4": # Jika pilihan bukan "3", tetapi pilihan adalah "4", maka program akan menghitung Luas Permukaan Bola
    print("\n================== Luas Permukaan Bola ===================\n")
    
    radius = float(input("Masukkan nilai jari-jari/radius bola (cm): "))

    hasil = 4 * 3.14 * (radius ** 2)
    
    print("\n---------------------- Penyelesaian ----------------------\n")
    print(f"r = {radius} cm\n")
    print(f"Luas Bola = 4 x π x r²")
    print(f"Luas Bola = 4 x 3.14 x {radius}²")
    print(f"Luas Bola = {4 * 3.14} x {radius ** 2}")
    print(f"Luas Bola = {hasil} cm²\n")

elif pilihan.lower() == "n": # Jika pilihan user adalah "4", tetapi pilihan adalah "N", maka program akan keluar
    print("\nProgram berhasil dihentikan!")

else: # Jika semua pilihan di atas tidak ada yang cocok, maka akan menampilkan "Tidak ada pilihan yang cocok" 
    print("\nTidak ada pilihan yang cocok dalam menu!")

print("========================== END ===========================")