import os


level = ("admin", "user")
pengguna = [
    # [Username, Password, Level/Role]
    ["Admin", "admin", level[0]],
    ["user", "user", level[1]]
]
indeksPengguna = -1
pilihan = ""
halaman = "login"
riwayatHalaman = ["login"]
forum = [
    # [Judul Forum, Deskripsi, Moderator[]]
    ["Gaming", "Lorem gaming ipsum", [pengguna[0]]],
    ["Teknologi", "Yang teknologi-teknologi ajah", [pengguna[1]]],
    ["Unmul", "Sehat-sehat mahasiswa Unmul :smiling_face:", [pengguna[1]]]
]
forumDipilih = 0
post = [
    # [Author, Judul Postingan, Konten Postingan, Indeks Forum]
    [pengguna[1], "Pra-ISO 2024 Resmi Tamat", "Setelah 5-6 minggu derita penugasan Pra-ISO, akhirnya tidak ada kegiatan di weekend dan penugasan lagi :yahahaha:", forum[2]]
]
postDipilih = []
balasan = [
    # [IndeksUser, Konteks, Balasan [indeksPost, Indeks Komentar Yang Dibalas]]
    [pengguna[1], "Halo Obrolan", [post[0]]],
    [pengguna[1], "P", [post[0], 0]]
]

while pilihan.lower() != "n":
    # Halaman Log In
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
            print(("(Ket: Kosongkan input untuk membatalkan.)"))

            if pilihan == "1":
                inputUsername = input("Username: ")
                while True:
                    usernameDigunakan = False
                    for i, itemPengguna in enumerate(pengguna):
                        if (itemPengguna[0].lower() == inputUsername.lower()):
                            usernameDigunakan = True
                            print("Username telah digunakan!")
                            print()
                            inputUsername = input("Username: ")
                            break
                    if (inputUsername == ""):
                        input("Register dibatalkan...!")
                        break
                    elif (usernameDigunakan == False):
                        inputPassword = input("Password: ")
                        pengguna.append([inputUsername, inputPassword, level[1]])
                        input("Pengguna Berhasil Ditambahkan...!")
                        break
            elif pilihan == "2":
                inputUsername = input("Username: ")
                if (inputUsername != ""):
                    for i, item in enumerate(pengguna):
                        if (item[0] == inputUsername):
                            indeksPengguna = i
                            break
                    inputPassword = input("Password: ")
                    if (0 <= indeksPengguna < len(pengguna)):
                        if (pengguna[indeksPengguna][1] == inputPassword):
                            input("Login Berhasil...!")
                            halaman = "menu utama"
                            break
                        elif (inputPassword == ""):
                            input("Log In Dibatalkan...!")
                        else: input("Username atau Password Salah...!")
                else:
                    input("Log In Dibatalkan...!")
        elif (pilihan.lower() == "n"):
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Halaman Menu Utama
    while halaman == "menu utama":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)
        username = pengguna[indeksPengguna][0]

        print(f"> {username} {"="*30}")
        print(f"|| Menu Utama ||")
        print()
        print(f"Selamat Datang, {username}!")
        print(f"{"-"*25}")
        print(f"> 1. Lihat Forum")
        print(f"{"-"*25}")
        print(f"> P. Pengaturan | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            halaman = "forum"
            break
        elif pilihan.lower() == "p" or pilihan.lower() == username:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "n":
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Halaman Forum
    while halaman == "forum":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)

        print(f"> {username} {"="*30}")
        print("|| Forum ||")
        print()
        print(f"> T. Buat Forum")
        print(f"{"-"*25}")
        for i, itemForum in enumerate(forum):
            print(f"> {i+1}. {itemForum[0]}")
        if (len(forum) < 1):
            print("Belum ada forum. Jadilah yang pertama untuk menambahkan!")
        print(f"{"-"*25}")
        print("> B. Kembali | > P. Pengaturan | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        for i in range(len(forum)):
            if (pilihan == str(i + 1)):
                forumDipilih = i
                break

        if pilihan.lower() == "t":
            print(f"{"="*40}")
            print("|| Buat Forum ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")

            judulForumBaru = input("Masukkan Judul Forum Anda: ")

            while True:
                forumTersedia = True
                for i, itemForum in enumerate(forum):
                    if (itemForum[0].lower() == judulForumBaru.lower()):
                        forumSudahAda = False
                        judulForumBaru = input("Masukkan Judul Forum Anda: ")
                        break
                if forumTersedia:
                    break
                    
            if judulForumBaru != "":
                deskripsiForumBaru = input("Masukkan Deksripsi Forum Anda: ")
                forum.append([judulForumBaru, deskripsiForumBaru, [pengguna[indeksPengguna]]])
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

    # Halaman List Post dari Forum
    while halaman == "forum post":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)
        postForumTerfilter = []

        print(f"> {username} {"="*30}")
        print(f"|| Forum {forum[forumDipilih][0]} ||")
        print()
        print(f"> T. Buat Postingan")
        print(f"{"-"*25}")
        print(f"Postingan:")
        nomor = 0
        for i, itemPost in enumerate(post):
            if (itemPost[3] == forum[forumDipilih]):
                nomor += 1
                print(f"> {nomor}. {itemPost[1]}: {itemPost[2]}")
                postForumTerfilter.append([nomor, i])
        if len(postForumTerfilter) < 1:
            print("Belum ada postingan. Jadilah yang pertama untuk menambahkan!")
        print(f"{"-"*25}")
        print(f"> B. Kembali | > P. Pengaturan | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        for i, itemPost in enumerate(postForumTerfilter):
            if (pilihan == str(nomor)):
                postDipilih = itemPost
                break

        if pilihan.lower() == "t":
            print(f"{"="*40}")
            print("|| Buat Postingan ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            judulPostinganBaru = input("Judul Postingan: ")

            if judulPostinganBaru != "":
                kontenPostinganBaru = input("Konten: ")
                if kontenPostinganBaru != "":
                    post.append([pengguna[indeksPengguna], judulPostinganBaru, kontenPostinganBaru, forum[forumDipilih]])
                else:
                    input("Komentar Dibatalkan...!") 
            else:
                input("Komentar Dibatalkan...!")
        elif pilihan.lower() == str(postDipilih[0] if len(postDipilih) > 1 else ""):
            halaman = "post"
            break
        elif pilihan.lower() == "p" or pilihan.lower() == username:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")
    
    # Halaman Konten Suatu Post
    while halaman == "post":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)

        komentarPostTerfilter = []
        komentarDipilih = [
            # [Nomor, indeks balasan]
        ]

        print(f"> {username} {"="*30}")
        print(f"|| {post[postDipilih[1]][1]} ||")
        print()
        print(post[postDipilih[1]][2])
        print(f"{"-"*25}")
        print("Komentar:")
        nomor = 0
        for i, komentarPost in enumerate(balasan):
            if (len(komentarPost[2]) == 1 and komentarPost[2][0] == post[postDipilih[1]]):
                nomor += 1
                if nomor != 1: print()
                print(f"> {nomor}. {komentarPost[0][0]}: {komentarPost[1]}")
                komentarPostTerfilter.append([nomor, i])
                for j, balasanKomentar in enumerate(balasan):
                    if (len(balasanKomentar[2]) == 2 and i == balasanKomentar[2][1]):
                        print(f"  +--{"-"*(len(str(nomor)))}> {balasanKomentar[0][0]}: {balasanKomentar[1]}")

        print(f"{"-"*25}")
        print(f"> K. Komentar | > B. Kembali | > P. Pengaturan | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        for i, itemKomentarPost in enumerate(komentarPostTerfilter):
            if (pilihan == str(itemKomentarPost[0])):
                komentarDipilih = itemKomentarPost
                break

        if pilihan.lower() == "k":
            print(f"{"="*40}")
            print("|| Komentar ||")
            print()
            
            print(f"{"="*40}")
            print("|| Komentar ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            komentarBaru = input("Komentar: ")

            if komentarBaru != "":
                balasan.append([pengguna[indeksPengguna], komentarBaru, [post[postDipilih[1]]]])
            else:
                input("Komentar Dibatalkan...!")
        elif pilihan.lower() == str(komentarDipilih[0] if len(komentarDipilih) > 0 else ""):
            print(f"{"="*40}")
            print("|| Balasan Komentar ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            balasanKomentarBaru = input("Balasan: ")

            if balasanKomentarBaru != "":
                balasan.append([pengguna[indeksPengguna], balasanKomentarBaru, [post[postDipilih[1]], komentarDipilih[1]]])
            else:
                input("Balasan Komentar Dibatalkan...!")
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
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
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
                pengguna[indeksPengguna][0] = username = usernameBaru
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
                    pengguna[indeksPengguna][1] = passwordBaru
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

# input("Program ditutup...")