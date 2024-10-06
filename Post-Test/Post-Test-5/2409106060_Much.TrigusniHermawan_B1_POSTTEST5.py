import os


level = ("admin", "user")
pengguna = [
    # [Username, Password, Level/Role]
    ["Admin", "admin", 0],
    ["user", "user", 1]
]
indeksPengguna = -1
pilihan = ""
halaman = "login"
riwayatHalaman = []
forum = ["Gaming", "Teknologi", "Kuliner", "Unmul", "Indonesia"]
forumDipilih = 0
post = [
    # Judul Postingan, Konten Postingan
    ["Pra-ISO 2024 Resmi Tamat", "Setelah 5-6 minggu derita penugasan Pra-ISO, akhirnya tidak ada kegiatan di weekend dan penugasan lagi :yahahaha:", forum[3]]
]
postDipilih = 0
balasan = [
    # IndeksUser, Isi Komen, Balasan [indeksPost, indeksKomentar]
    [1, "Halo Obrolan", [0]],
    [1, "P", [0, 0]]
]

while pilihan.lower() != "n":
    # Halaman Pengaturan
    while halaman == "login":
        os.system('cls || clear')

        print(f"{"="*40}")
        print(f"|| Forum Diskusi Online ||")
        print()
        print(f"{"-"*25}")
        print(f"1. Pengguna Baru? Buat Akun Baru")
        print(f"2. Sudah Punya Akun? Log In")
        print(f"{"-"*25}")
        print(f"N. Keluar dari Program")
        print()
        pilihan = input("Masukkan Pilihan Anda: ")
        print("="*40)
        
        if (pilihan == "1" or pilihan == "2"):
            print(("|| REGISTER ||" if pilihan == "1" else "|| LOG IN ||") + "\n")
            inputUsername = input("Username: ")
            inputPassword = input("Password: ")

            if pilihan == "1":
                pengguna.append([inputUsername, inputPassword, level[1]])
                input("Pengguna Berhasil Ditambahkan...!")
            else:
                for i, item in enumerate(pengguna): 
                    if (item[0] == inputUsername):
                        indeksPengguna = i
                        break
                if (0 <= indeksPengguna < len(pengguna)):
                    if (pengguna[indeksPengguna][1] == inputPassword):
                        input("Login Berhasil...!")
                        halaman = "menu utama"
                        break
                input("Username atau Password Salah...!")

        elif (pilihan.lower() == "n"):
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Halaman Pengaturan
    while halaman == "menu utama":
        os.system("cls || clear")
        riwayatHalaman.append(halaman)
        username = pengguna[indeksPengguna][0]

        print(f"> {username} {"="*30}")
        print(f"|| Menu Utama ||")
        print()
        print(f"Selamat Datang, {username}!")
        print(f"{"-"*25}")
        print(f"> 1. Lihat Forum")
        print(f"{"-"*25}")
        print(f"> P. Pengaturan")
        print(f"> N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            halaman = "forum"
            break
        elif pilihan.lower() == "p" or pilihan.lower() == username:
            halaman = "pengaturan"
        elif pilihan.lower() == "n":
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Halaman Pengaturan
    while halaman == "forum":
        os.system("cls || clear")
        riwayatHalaman.append(halaman)

        print(f"> {username} {"="*30}")
        print("|| Forum ||")
        print()
        print(f"> T. Buat Forum")
        print(f"{"-"*25}")
        for i, itemForum in enumerate(forum):
            print(f"> {i+1}. {itemForum}")
        if (len(itemForum) < 1):
            print("Belum ada forum. Jadilah yang pertama untuk menambahkan!")
        print(f"{"-"*25}")
        print("> B. Kembali")
        print("> P. Pengaturan")
        print("> N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        for i, itemForum in enumerate(forum):
            if (pilihan == str(i + 1)):
                forumDipilih = i
                break

        if pilihan.lower() == "t":
            print(f"{"="*40}")
            print("|| Buat Forum ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            judulForumBaru = input("Masukkan Judul Forum Anda: ")

            forumSudahAda = False
            for i, itemForum in len(forum):
                if (itemForum.lower() == judulForumBaru.lower()):
                    forumSudahAda = True

            if judulForumBaru != "" and forumSudahAda == False:
                forum.append(judulForumBaru) 
                input("Forum Berhasil Ditambahkan...!")
            else:
                input("Pembuatan Forum Dibatalkan...!")
        elif pilihan.lower() == str(forumDipilih + 1):
            halaman = "forum post"
            break
        elif pilihan.lower() == "p" or pilihan.lower() == username:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")

    while halaman == "forum post":
        os.system("cls || clear")
        riwayatHalaman.append(halaman)
        postForumDipilih = []

        print(f"> {username} {"="*30}")
        print(f"|| Forum {forum[forumDipilih]} ||")
        print()
        print(f"> T. Buat Postingan")
        print(f"{"-"*25}")
        for i, itemPost in enumerate(post):
            if (itemPost[2] == forum[forumDipilih]):
                print(f"> {i+1}. {itemPost[0]}: {itemPost[1]}")
                postForumDipilih.append(i)
        if len(postForumDipilih) < 1:
            print("Belum ada postingan. Jadilah yang pertama untuk menambahkan!")
        print(f"{"-"*25}")
        print(f"> B. Kembali")
        print(f"> N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        for i, itemPost in enumerate(postForumDipilih):
            if (pilihan == str(itemPost + 1)):
                postDipilih = itemPost
                break

        if pilihan.lower() == "t":
            print(f"{"="*40}")
            print("|| Buat Postingan ||")
            print()
        elif pilihan.lower() == str(postDipilih + 1):
            halaman = "post"
            break
        elif pilihan.lower() == "p" or pilihan.lower() == username:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")
    
    while halaman == "post":
        os.system("cls || clear")
        riwayatHalaman.append(halaman)

        print(f"> {username} {"="*30}")
        print(f"|| {post[postDipilih][0]} ||")
        print()
        print(f"{"-"*25}")
        print(post[postDipilih][1])
        print(f"{"-"*25}")
        print("Komentar:")
        for i, komentarPost in enumerate(balasan):
            if (len(komentarPost[2]) == 1 and post[komentarPost[2][0]] == post[postDipilih]):
                print(f"{pengguna[komentarPost[0]][0]}: {komentarPost[1]}")
                for j, balasanKomentar in enumerate(balasan):
                    if (len(balasanKomentar[2]) == 2 and i == balasanKomentar[2][1]):
                        print(f"+-> {pengguna[balasanKomentar[0]][0]}: {balasanKomentar[1]}")

        print(f"{"-"*25}")
        print(f"> K. Komentar")
        print(f"> B. Kembali")
        print(f"> N. Keluar dari Program")
        print(f"> N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan.lower() == "t":
            print(f"{"="*40}")
            print("|| Buat Postingan ||")
            print()
        elif pilihan.lower() == str(forumDipilih + 1):
            halaman = "forum post"
            break
        elif pilihan.lower() == "p" or pilihan.lower() == username:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Halaman Pengaturan
    while halaman == "pengaturan":
        os.system("cls || clear")
        riwayatHalaman.append(halaman)

        print(f"{"="*30}")
        print(f"|| Pengaturan ||")
        print()
        print(f"Akun: {username}")
        print(f"{"-"*25}")
        print(f"> 1. Update Username")
        print(f"> 2. Update Password")
        print(f"> 3. Log Out")
        print(f"{"-"*25}")
        print(f"> B. Kembali")
        print(f"> N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            print(f"{"="*40}")
            print("|| Update Username ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            usernameBaru = input("Masukkan Username Baru Anda: ")

            if usernameBaru != "":
                pengguna[indeksPengguna][0] = usernameBaru
                input("Username Berhasil Diperbarui...!")
            else:
                input("Perubahan Username Dibatalkan...!")
        elif pilihan == "2":
            print(f"> {username} {"="*30}")
            print("|| Update Password ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            passwordLama = input("Masukkan Password Lama Anda: ")
            if pengguna[indeksPengguna][1] == passwordLama and passwordLama != "":
                passwordBaru = input("Masukkan Password Baru Anda: ")
                if passwordBaru != "":
                    pengguna[indeksPengguna][1] == passwordBaru
                    input("Password Berhasil Diperbarui...!")
                else:
                    input("Perubahan Password Dibatalkan...!")
            elif passwordLama != "":
                input("Password Anda Salah...!")
            else:
                input("Perubahan Password Dibatalkan...!")
        elif pilihan.lower() == "3":
            halaman = "login"
            input("Berhasil Log Out...!")
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            halaman = ""
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Kembali ke halaman sebelumnya
    if pilihan.lower() == "b":
        # Perulangan 2x untuk kembali ke dua halaman terakhir (termasuk halaman saat ini)
        for i in range(2):
            if len(riwayatHalaman) > 0:
                halaman = riwayatHalaman.pop()
        pilihan = ""
            

    # for i, item in enumerate(pengguna):
    #     username = item[0]
    #     password = item[1]
    #     level = item[2]
    #     print(f"{i+1}. {username} {password} {level}")

# input("Program ditutup...")