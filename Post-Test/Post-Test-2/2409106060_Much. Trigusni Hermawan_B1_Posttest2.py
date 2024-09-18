nama = input("Masukkan Nama Anda: ")
umur = int(input("Masukkan Umur Anda: "))
beratBadan = float(input("Masukkan Berat Badan Anda (Kg): "))
tinggiBadan = float(input("Masukkan Tinggi Badan Anda (Cm): "))
singleStatus = input("Apakah Anda Seorang Single? (y/n) ")[0].lower() == "y"

jumlahNilaiNumerik = umur + tinggiBadan + beratBadan

print(f"""
==============================================
                Bio Data Anda
==============================================
Nama                 : {nama}
Umur                 : {umur} Tahun
Berat Badan          : {beratBadan} Kg
Tinggi Badan         : {tinggiBadan} Cm
Single               : {singleStatus}
Jumlah Nilai Numerik : {jumlahNilaiNumerik}
==============================================
""")