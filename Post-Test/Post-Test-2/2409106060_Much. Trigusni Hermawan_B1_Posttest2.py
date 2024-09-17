nama = input("Masukkan Nama Anda: ")
umur = int(input("Masukkan Umur Anda: "))
tinggiBadan = float(input("Masukkan Tinggi Badan Anda (Cm): "))
beratBadan = float(input("Masukkan Berat Badan Anda (Kg): "))
singleStatus = input("Apakah Anda Seorang Single? (y/n) ")[0].lower() == "y"

jumlahNilaiNumerik = umur + tinggiBadan + beratBadan

print(f"""
==============================================
                Bio Data Diri
==============================================
Nama                 : {nama}
Umur                 : {umur} Tahun
Berat Badan          : {beratBadan} Kg
Tinggi Badan         : {tinggiBadan} Cm
Single               : {singleStatus} 
Jumlah Nilai Numerik : {jumlahNilaiNumerik}
==============================================
"""
)