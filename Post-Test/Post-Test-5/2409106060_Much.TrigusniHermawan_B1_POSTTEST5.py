import os

level = ("admin", "user")
pengguna = [
    # [Username, Password, Level/Role]
    ["Admin", "admin", level[0]],
    ["user", "user", level[1]]
]
guest = False
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
        guest = False
        os.system('cls || clear')

        print(f"{"="*40}")
        print(f"|| Forum Diskusi Online ||")
        print()
        print(f"{"-"*25}")
        print(f"1. Pengguna Baru? Buat Akun Baru")
        print(f"2. Sudah Punya Akun? Log In")
        print(f"3. Masuk sebagai Guest")
        print(f"{"-"*25}")
        print(f"N. Keluar dari Program")
        print()
        pilihan = input("Masukkan Pilihan Anda: ")
        print("="*40)
        
        if pilihan == "1":
            print("|| REGISTER ||")
            print()
            print(("(Ket: Kosongkan input untuk membatalkan.)"))
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
                    if (inputUsername != "" and inputPassword != ""):
                        pengguna.append([inputUsername, inputPassword, level[1]])
                        input("Pengguna Berhasil Ditambahkan...!")
                        break
                    else:
                        input("Register dibatalkan...!")
                        break
        elif pilihan == "2":
            print("|| LOG IN ||")
            print()
            print(("(Ket: Kosongkan input untuk membatalkan.)"))
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
        elif pilihan.lower() == "3":
            guest = True
            halaman = "menu utama"
            break
        elif pilihan.lower() == "n":
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Halaman Menu Utama
    while halaman == "menu utama":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)
        username = pengguna[indeksPengguna][0] if guest == False else "Guest"

        print(f"> {username} {"="*30}")
        print(f"|| Menu Utama ||")
        print()
        print(f"Selamat Datang, {username}!")
        print(f"{"-"*25}")
        print(f"> 1. Lihat Forum")
        if pengguna[indeksPengguna][2] == "admin":
            print(f"> 2. Dashboard")
            print(f"> 3. Pengguna")
        print(f"{"-"*25}")
        print(f"> {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            halaman = "forum"
            break
        if pilihan == "2" and pengguna[indeksPengguna][2] == "admin":
            halaman = "dashboard"
            break
        if pilihan == "3" and pengguna[indeksPengguna][2] == "admin":
            halaman = "pengguna"
            break
        elif (pilihan.lower() == "p" or pilihan.lower() == username) and guest == False:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "l" and guest == True:
            halaman = "login"
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
        if guest == False:
            print(f"> T. Buat Forum")
        print(f"{"-"*25}")
        for i, itemForum in enumerate(forum):
            print(f"> {i+1}. {itemForum[0]}")
        if (len(forum) < 1):
            print("Belum ada forum. Jadilah yang pertama untuk menambahkan!")
        print(f"{"-"*25}")
        print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        for i in range(len(forum)):
            if (pilihan == str(i + 1)):
                forumDipilih = i
                break

        if pilihan.lower() == "t" and guest == False:
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
                        print("Judul forum sudah ada!\n")
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
        elif (pilihan.lower() == "p" or pilihan.lower() == username) and guest == False:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "l" and guest == True:
            halaman = "login"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")

    while halaman == "dashboard" and pengguna[indeksPengguna][2] == "admin":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)

        print(f"> {username} {"="*30}")
        print("|| Dashboard ||")
        print()
        print(f"{"-"*25}")
        print(f"Total Forum = {len(forum)}")
        print(f"Total Postingan = {len(post)}")
        print(f"Total Pengguna = {len(pengguna)}")
        print(f"{"-"*25}")
        print()
        input("Kembali ke Menu Utama...!")
        pilihan = "b"
        break

    while halaman == "pengguna" and pengguna[indeksPengguna][2] == "admin":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)

        penggunaDipilih = -1

        print(f"> {username} {"="*30}")
        print("|| Pengguna ||")
        print()
        print(f"> T. Tambah Pengguna | > E. Edit Pengguna | > D. Hapus Pengguna")
        print(f"{"-"*25}")
        for i, itemPengguna in enumerate(pengguna):
            print(f"{i+1}. Username: {itemPengguna[0]}, Pass: {itemPengguna[1]}, Level: {itemPengguna[2]}")
        print(f"{"-"*25}")
        print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan.lower() == "t":
            print(f"{"="*40}")
            print("|| Tambah Pengguna ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
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
                    input("Gagal menambahkan pengguna...!")
                    break
                elif (usernameDigunakan == False):
                    inputPassword = input("Password: ")
                    if (inputPassword == ""):
                        input("Gagal menambahkan pengguna...!")
                        break
                    print("Pilih Level: ")
                    print("1. Admin")
                    print("2. User")
                    inputLevel = ""
                    pilihan = input("Pilih level: ")
                    while inputPassword != "":
                        if pilihan == "1":
                            inputLevel = level[0]
                            break
                        elif pilihan == "2":
                            inputLevel = level[1]
                            break
                        elif pilihan == "":
                            break
                        else:
                            print("Pilihan tidak valid!\n")
                            pilihan = input("Pilih level: ")
                    if inputUsername != "" and inputPassword != "" and inputLevel != "":
                        pengguna.append([inputUsername, inputPassword, inputLevel])
                        input("Pengguna Berhasil Ditambahkan...!")
                        break
                    else:
                        input("Gagal menambahkan Pengguna...!")
                        break
        elif pilihan.lower() == "e":
            print("\n(Ket: Kosongkan input untuk membatalkan.)")
            pilihan = input("Pilih pengguna yang ingin diedit: ")
            while True:
                if pilihan != "":
                    for i, itemPengguna in enumerate(pengguna):
                        if pilihan == str(i + 1):
                            penggunaDipilih = i
                            break
                    if penggunaDipilih < 0:
                        print("Pengguna tidak ditemukan!") 
                        pilihan = input("Pilih pengguna yang ingin diedit: ")
                    else:
                        break
                else:
                    input("Edit berhasil dibatalkan...!")
                    break
            
            if penggunaDipilih < 0: break
            print(f"{"="*40}")
            print(f"|| Edit Pengguna \"{pengguna[penggunaDipilih][0]}\" ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            inputUsername = input("Username: ")
            while True:
                usernameDigunakan = False
                for i, itemPengguna in enumerate(pengguna):
                    if (itemPengguna[0].lower() == inputUsername.lower() and pengguna[penggunaDipilih] != itemPengguna):
                        usernameDigunakan = True
                        print("Username telah digunakan!")
                        print()
                        inputUsername = input("Username: ")
                        break
                if (inputUsername == ""):
                    input("Edit berhasil dibatalkan...!")
                    break
                elif (usernameDigunakan == False):
                    inputPassword = input("Password: ")
                    if (inputPassword == ""):
                        input("Edit berhasil dibatalkan...!")
                        break
                    print("Pilih Level: ")
                    print("1. Admin")
                    print("2. User")
                    inputLevel = ""
                    pilihan = input("Pilih level: ")
                    while inputPassword != "":
                        if pilihan == "1":
                            inputLevel = level[0]
                            break
                        elif pilihan == "2":
                            inputLevel = level[1]
                            break
                        elif pilihan == "":
                            break
                        else:
                            print("Pilihan tidak valid!\n")
                            pilihan = input("Pilih level: ")
                    if inputUsername != "" and inputPassword != "" and inputLevel != "":
                        pengguna[penggunaDipilih][0] = inputUsername
                        pengguna[penggunaDipilih][1] = inputPassword
                        pengguna[penggunaDipilih][2] = inputLevel
                        input("Pengguna Berhasil Diedit...!")
                        break
                    else:
                        input("Gagal menambahkan Pengguna...!")
                        break
        elif pilihan.lower() == "d":
            pilihan = input("Pilih pengguna yang ingin dihapus: ")
            for i, itemPengguna in enumerate(pengguna):
                if (pilihan == str(i + 1)):
                    if (pengguna[indeksPengguna] != itemPengguna):
                        akunDihapus = pengguna.pop(i)
                        input(f"Berhasil menghapus akun \"{akunDihapus[0]}\"!")
                    else:
                        input("Tidak dapat menghapus diri sendiri!")
                    break
        elif (pilihan.lower() == "p" or pilihan.lower() == username) and guest == False:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "l" and guest == True:
            halaman = "login"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            print("Pilihan tidak valid!")

    # Halaman List Post dari Forum
    while halaman == "forum post":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)
        postForumTerfilter = []
        moderator = False

        for i, momod in enumerate(forum[forumDipilih][2]):
            if (pengguna[indeksPengguna] == momod):
                moderator = True

        print(f"> {username} {"="*30}")
        print(f"|| Forum {forum[forumDipilih][0]} ||")
        print()
        if guest == False:
            print(f"> T. Buat Postingan | {"> M. Manajemen Forum" if moderator or pengguna[indeksPengguna][2] == "admin" else ""}")
        print(f"{"-"*25}")
        print(f"Deskripsi: {forum[forumDipilih][1]}")
        print()
        print(f"Postingan:")
        nomor = 0
        for i, itemPost in enumerate(post):
            if (itemPost[3] == forum[forumDipilih]):
                nomor += 1
                print(f"> {nomor}. {itemPost[1]}: {itemPost[2]}")
                postForumTerfilter.append([nomor, i])
        if len(postForumTerfilter) < 1:
            print("Belum ada postingan. Jadilah yang pertama untuk menambahkan!" if guest == False else "Belum ada postingan.")
        print(f"{"-"*25}")
        print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        for i, itemPost in enumerate(postForumTerfilter):
            if (pilihan == str(nomor)):
                postDipilih = itemPost
                break

        if pilihan.lower() == "t" and guest == False:
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
        elif pilihan.lower() == "m" and (moderator or pengguna[indeksPengguna][2] == "admin") and guest == False:
            halaman = "manajemen forum"
            break
        elif pilihan.lower() == str(postDipilih[0] if len(postDipilih) > 1 else ""):
            halaman = "post"
            break
        elif (pilihan.lower() == "p" or pilihan.lower() == username) and guest == False:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "l" and guest == True:
            halaman = "login"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")
    
    # Halaman List Post dari Forum
    while halaman == "manajemen forum":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)
        postForumTerfilter = []
        moderator = False

        for i, momod in enumerate(forum[forumDipilih][2]):
            if (pengguna[indeksPengguna] == momod):
                moderator = True
        if moderator == False and pengguna[indeksPengguna][2] != "admin":
            halaman = "forum"
            break
        print(f"> {username} {"="*30}")
        print(f"|| Manajemen Forum \"{forum[forumDipilih][0]}\" ||")
        print()
        print(f"{"-"*25}")
        print(f"> 1. Moderator")
        print(f"> 2. Ganti Judul Forum")
        print(f"> 3. Ganti Deskripsi Forum")
        print(f"> 4. Hapus Forum")
        print(f"{"-"*25}")
        print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan.lower() == "1":
            halaman = "manajemen mod"
        elif pilihan.lower() == "2":
            print(f"{"="*40}")
            print("|| Update Judul Forum ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            judulBaru = input("Masukkan Judul Baru Forum: ")
            while True:
                forumTersedia = True
                for i, itemForum in enumerate(forum):
                    if (itemForum[0].lower() == judulBaru.lower()):
                        forumSudahAda = False
                        print("Judul forum sudah ada!\n")
                        judulBaru = input("Masukkan Judul Forum Anda: ")
                        break
                if forumTersedia:
                    forum[forumDipilih][0] = judulBaru
                    input("Judul Forum Berhasil Diperbarui...")
                    break
        elif pilihan.lower() == "3":
            print(f"{"="*40}")
            print("|| Update Deskripsi Forum ||")
            print()
            print(f"Deskripsi Saat Ini: \"{forum[forumDipilih][1]}\"")
            print(f"{"-"*25}")
            print("(Ket: Kosongkan input untuk membatalkan.)")
            deskripsiBaru = input("Deskripsi Baru: ")
            while True:
                if pilihan != "":
                    forum[forumDipilih][1] = deskripsiBaru
                    input("Deskripsi Forum Berhasil Diperbarui...!")
                    break
                else:
                    input("Perubahan Deskripsi Forum Dibatalkan...!")
                    break
        elif pilihan.lower() == "4":
            print()
            print(f"APAKAH ANDA YAKIN INGIN MENGHAPUS FORUM \"{forum[forumDipilih][0]}\"?")
            print("> Y. YA")
            print("> N. TIDAK")
            pilihan = input("TENTUKAN DENGAN BIJAK: ")
            while True:
                if pilihan != "":
                    if pilihan.lower() == "y":
                        input("TELAH DILENYAPKAN...!")
                        halaman = "forum"
                        forumDihapus = forum.pop(forumDipilih)
                        break
                    elif pilihan.lower() == "n":
                        input("TELAH DIKEMBALIKAN...!")
                        break
                    else:
                        input("RAGU-RAGU...?")
                        pilihan = input("TENTUKAN DENGAN BIJAK: ")
                else:
                    input("SUNGGUH MENARIK...")
                    break
        elif (pilihan.lower() == "p" or pilihan.lower() == username) and guest == False:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "l" and guest == True:
            halaman = "login"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")
    
    # Halaman List Post dari Forum
    while halaman == "manajemen mod":
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)
        postForumTerfilter = []
        moderator = False

        for i, momod in enumerate(forum[forumDipilih][2]):
            if (pengguna[indeksPengguna] == momod):
                moderator = True
        if moderator == False and pengguna[indeksPengguna][2] != "admin":
            halaman = "forum"
            break
        print(f"> {username} {"="*30}")
        print(f"|| Manajemen Mod {forum[forumDipilih][0]} ||")
        print()
        print(f"> T. Tambah Moderator | > D. Hapus Moderator")
        print(f"{"-"*25}")
        for i, momod in enumerate(forum[forumDipilih][2]):
            print(f"{i+1}. {momod[0]}")
        print(f"{"-"*25}")
        print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan.lower() == "t":
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            usernameMomodBaru = input("Username Moderator Baru: ")
            while True:
                if pilihan != "":
                    penggunaDitemukan = ""
                    penggunaValid = False
                    for i, itemPengguna in enumerate(pengguna):
                        if usernameMomodBaru == itemPengguna[0]:
                            penggunaDitemukan = itemPengguna[0]
                            penggunaValid = True
                            for j, momod in enumerate(forum[forumDipilih][2]):
                                print(f"{momod[0]} == {itemPengguna[0]}")
                                if momod[0] == itemPengguna[0]:
                                    penggunaValid = False
                                    break
                            break
                    if penggunaValid:
                        input(f"Berhasil menambahkan \"{penggunaDitemukan}\" sebagai Moderator!")
                        forum[forumDipilih][2].append(itemPengguna)
                        break
                    elif (penggunaDitemukan == ""):
                        input("Username tidak ditemukan!")
                        break
                    else:
                        input(f"\"{penggunaDitemukan}\" sudah menjadi Moderator!")
                        break
                else:
                    input("Tambah Moderator dibatalkan!")
                    break

        elif pilihan.lower() == "d":
            print(f"{"="*40}")
            print("|| Hapus Moderator ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            pilihan = input("Pilih pengguna yang ingin dihapus: ")
            for i, momod in enumerate(forum[forumDipilih][2]):
                if (pilihan == str(i + 1)):
                    if (i == 0):
                        input("Tidak dapat mengkudeta pemilik forum!")
                    else:
                        akunDihapus = forum[forumDipilih][2].pop(i)
                        input(f"Berhasil mengkudeta \"{akunDihapus[0]}\"!")
                    break
        elif (pilihan.lower() == "p" or pilihan.lower() == username) and guest == False:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "l" and guest == True:
            halaman = "login"
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
        if guest:
            print(f"> B. Kembali | > L. Log in | > N. Keluar dari Program")
        else:
            print(f"> K. Komentar | > B. Kembali | > P. Pengaturan | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        for i, itemKomentarPost in enumerate(komentarPostTerfilter):
            if (pilihan == str(itemKomentarPost[0])):
                komentarDipilih = itemKomentarPost
                break

        if pilihan.lower() == "k" and guest == False:
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
        elif (pilihan.lower() == "p" or pilihan.lower() == username) and guest == False:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "l" and guest == True:
            halaman = "login"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Halaman Pengaturan
    while halaman == "pengaturan":
        os.system("cls || clear")

        if (guest):
            halaman = "login"
            break
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
        
input("Program ditutup...")