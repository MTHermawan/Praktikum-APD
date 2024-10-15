import os

# Deklarasi Variabel
level = {
    0: "admin",
    1: "user"
}

pengguna = {
    "Admin": {
        "password": "admin",
        "level": level[0]
        },
    "user": {
        "password": "user",
        "level": level[1]
        }
    }

guest = False
usernamePengguna = ""
pilihan = ""
halaman = "login"
riwayatHalaman = [halaman]
forum = {
    "Gaming": {
        "deskripsi": "Lorem gaming ipsum",
        "moderator": ["Admin"]
    },
    "Teknologi": {
        "deskripsi": "Yang teknologi-teknologi ajah",
        "moderator": ["Admin"]
    },
    "Unmul": {
        "deskripsi": "Sehat-sehat mahasiswa Unmul :smiling_face:",
        "moderator": ["user"]
    }
}
forumDipilih = ""
post = {
    "Lorem Ipsum": {
        "author": "user",
        "konten": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "forum": "Teknologi"
    }
}
postDipilih = ""
balasan = {
    0 : {
        "author": "user",
        "konten": "Halo Obrolan",
        "konteks": {
            "post": "Lorem Ipsum",
        }
    },
    1 : {
        "author": "user",
        "konten": "P",
        "konteks": {
            "post": "Lorem Ipsum",
            "balasan": 0
        }
    }
}

while pilihan.lower() != "n":
    # Isi Semua Halaman Program

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
                for username, itemPengguna in pengguna.items():
                    if (username.lower() == inputUsername.lower()):
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
                        pengguna[inputUsername] = {
                            "password": inputPassword,
                            "level": level[1]
                        }
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
                for username, itemPengguna in pengguna.items():
                    if (username == inputUsername):
                        usernamePengguna = username
                        break
                inputPassword = input("Password: ")
                if (pengguna[username]["password"] == inputPassword):
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

        print(f"> {usernamePengguna} {"="*30}")
        print(f"|| Menu Utama ||")
        print()
        if guest == False:
            print(f"Selamat Datang, {usernamePengguna}!")
        print(f"{"-"*25}")
        print(f"> 1. Lihat Forum")
        if ((pengguna[usernamePengguna]["level"] == "admin") if guest == False else False):
            print(f"> 2. Dashboard")
            print(f"> 3. Pengguna")
        print(f"{"-"*25}")
        print(f"> {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            halaman = "forum"
            break
        if pilihan == "2" and ((pengguna[usernamePengguna]["level"] == "admin") if guest == False else False):
            halaman = "dashboard"
            break
        if pilihan == "3" and ((pengguna[usernamePengguna]["level"] == "admin") if guest == False else False):
            halaman = "pengguna"
            break
        elif (pilihan.lower() == "p" or pilihan.lower() == usernamePengguna) and guest == False:
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

        print(f"> {usernamePengguna} {"="*30}")
        print("|| Forum ||")
        print()
        if guest == False:
            print(f"> T. Buat Forum")
        print(f"{"-"*25}")
        i = 0
        for namaForum, itemForum in forum.items():
            print(f"> {i+1}. {namaForum}")
            i += 1
        if (len(forum) < 1):
            print("Belum ada forum. Jadilah yang pertama untuk menambahkan!")
        print(f"{"-"*25}")
        print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        indeksForum = 0
        for namaForum, itemForum in forum.items():
            indeksForum += 1
            if (pilihan == str(indeksForum)):
                forumDipilih = namaForum
                break

        if pilihan.lower() == "t" and guest == False:
            print(f"{"="*40}")
            print("|| Buat Forum ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")

            judulForumBaru = input("Masukkan Judul Forum Anda: ")

            while True:
                forumTersedia = True
                for namaForum, itemForum in forum.items():
                    if (namaForum.lower() == judulForumBaru.lower()):
                        forumSudahAda = False
                        print("Judul forum sudah ada!\n")
                        judulForumBaru = input("Masukkan Judul Forum Anda: ")
                        break
                if forumTersedia:
                    break
                    
            if judulForumBaru != "":
                deskripsiForumBaru = input("Masukkan Deksripsi Forum Anda: ")
                forum[judulForumBaru] = {
                    "deskripsi": deskripsiForumBaru,
                    "moderator": [usernamePengguna]
                }
                input("Forum Berhasil Ditambahkan...!")
            else:
                input("Pembuatan Forum Dibatalkan...!")
        elif pilihan.lower() == str(indeksForum):
            halaman = "forum post"
            break
        elif (pilihan.lower() == "p" or pilihan.lower() == usernamePengguna) and guest == False:
            halaman = "pengaturan"
            break
        elif pilihan.lower() == "l" and guest == True:
            halaman = "login"
            break
        elif pilihan.lower() == "n" or pilihan.lower() == "b":
            break
        else:
            input("Pilihan Tidak Valid...!")

    # Halaman Dashboard
    while halaman == "dashboard" and ((pengguna[usernamePengguna]["level"] == "admin") if guest == False else False):
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)

        print(f"> {usernamePengguna} {"="*30}")
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

    # Halaman Manajaemen Penggna
    while halaman == "pengguna" and ((pengguna[usernamePengguna]["level"] == "admin") if guest == False else False):
        os.system("cls || clear")
        if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
            riwayatHalaman.append(halaman)

        penggunaDipilih = ""

        print(f"> {usernamePengguna} {"="*30}")
        print("|| Pengguna ||")
        print()
        print(f"> T. Tambah Pengguna | > E. Edit Pengguna | > D. Hapus Pengguna")
        print(f"{"-"*25}")
        i = 0
        for username, itemPengguna in pengguna.items():
            print(f"{i+1}. Username: {username}, Pass: {itemPengguna.get("password")}, Level: {itemPengguna.get("level")}")
            i += 1
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
                for username, itemPengguna in pengguna.items():
                    if (username.lower() == inputUsername.lower()):
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
                        pengguna[inputUsername] = {
                            "password": inputPassword,
                            "level": inputLevel
                        }
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
                    i = -1
                    for username, itemPengguna in pengguna.items():
                        i += 1
                        if pilihan == str(i + 1):
                            penggunaDipilih = username
                            break
                    if penggunaDipilih == "":
                        print("Pengguna tidak ditemukan!") 
                        pilihan = input("Pilih pengguna yang ingin diedit: ")
                    else:
                        break
                else:
                    input("Edit berhasil dibatalkan...!")
                    break
            
            if penggunaDipilih == "": break
            print(f"{"="*40}")
            print(f"|| Edit Pengguna \"{penggunaDipilih}\" ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            inputUsername = input("Username: ")
            while True:
                usernameDigunakan = False
                for username, itemPengguna in pengguna.items():
                    if (username.lower() == inputUsername.lower() and penggunaDipilih != username):
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
                        cache = pengguna.pop(penggunaDipilih)
                        pengguna[inputUsername] = {
                            "password": inputPassword,
                            "level": inputLevel
                        }
                        input("Pengguna Berhasil Diedit...!")
                        break
                    else:
                        input("Gagal Mengedit Pengguna...!")
                        break
        elif pilihan.lower() == "d":
            pilihan = input("Pilih pengguna yang ingin dihapus: ")
            i = 0
            for username, itemPengguna in pengguna.items():
                i += 1
                if (pilihan == str(i)):
                    if (usernamePengguna != username):
                        akunDihapus = pengguna.pop(username)
                        input(f"Berhasil menghapus akun \"{akunDihapus[0]}\"!")
                    else:
                        input("Tidak dapat menghapus diri sendiri!")
                    break

        elif (pilihan.lower() == "p" or pilihan.lower() == usernamePengguna) and guest == False:
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

        for i, momod in enumerate(forum[forumDipilih]["moderator"]):
            print(momod)
            if (usernamePengguna == momod):
                moderator = True

        print(f"> {usernamePengguna} {"="*30}")
        print(f"|| Forum {forumDipilih} ||")
        print()
        if guest == False:
            print(f"> T. Buat Postingan {"| > M. Manajemen Forum" if moderator or ((pengguna[usernamePengguna]["level"] == "admin") if guest == False else False) else ""}")
        print(f"{"-"*25}")
        print(f"Deskripsi: {forumDipilih}")
        print()
        print(f"Postingan:")
        nomor = 0
        for namaPost, itemPost in post.items():
            if (itemPost["forum"] == forumDipilih):
                nomor += 1
                print(f"> {nomor}. {namaPost}: {itemPost['konten']}")
                postForumTerfilter.append([nomor, namaPost])
        if len(postForumTerfilter) < 1:
            print("Belum ada postingan. Jadilah yang pertama untuk menambahkan!" if guest == False else "Belum ada postingan.")
        print(f"{"-"*25}")
        print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
        print()
        pilihan = input("Masukkan pilihan Anda: ")

        indeksPost = -1
        for indeksPost, itemPost in enumerate(postForumTerfilter):
            if (pilihan == str(indeksPost + 1)):
                postDipilih = itemPost[1]
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
                    post[judulPostinganBaru] = {
                        "author": usernamePengguna,
                        "konten": kontenPostinganBaru,
                        "forum": forumDipilih
                    }
                    input("Postingan Berhasil Ditambahkan...!")
                else:
                    input("Komentar Dibatalkan...!") 
            else:
                input("Komentar Dibatalkan...!")
        elif pilihan.lower() == "m" and (moderator or ((pengguna[usernamePengguna]["level"] == "admin") if guest == False else False)) and guest == False:
            halaman = "manajemen forum"
            break
        elif pilihan.lower() == str(indeksPost + 1) and indeksPost != -1:
            halaman = "post"
            break
        elif (pilihan.lower() == "p" or pilihan.lower() == usernamePengguna) and guest == False:
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

        for i, momod in enumerate(forum[forumDipilih]["moderator"]):
            if (usernamePengguna == momod):
                moderator = True
        if moderator == False and pengguna[usernamePengguna]["level"] != "admin":
            halaman = "forum"
            break
        print(f"> {usernamePengguna} {"="*30}")
        print(f"|| Manajemen Forum \"{forumDipilih}\" ||")
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
                for namaForum, itemForum in forum.items():
                    if (namaForum.lower() == judulBaru.lower()):
                        forumTersedia = False
                        print("Judul forum sudah ada!\n")
                        judulBaru = input("Masukkan Judul Forum Anda: ")
                        break
                if forumTersedia:
                    cache = forum[forumDipilih]
                    forum.pop(forumDipilih)
                    forum[judulBaru] = cache
                    input("Judul Forum Berhasil Diperbarui...")
                    break
        elif pilihan.lower() == "3":
            print(f"{"="*40}")
            print("|| Update Deskripsi Forum ||")
            print()
            print(f"Deskripsi Saat Ini: \"{forum[forumDipilih]["deskripsi"]}\"")
            print(f"{"-"*25}")
            print("(Ket: Kosongkan input untuk membatalkan.)")
            deskripsiBaru = input("Deskripsi Baru: ")
            while True:
                if pilihan != "":
                    forum[forumDipilih]["deskripsi"] = deskripsiBaru
                    input("Deskripsi Forum Berhasil Diperbarui...!")
                    break
                else:
                    input("Perubahan Deskripsi Forum Dibatalkan...!")
                    break
        elif pilihan.lower() == "4":
            print()
            print(f"APAKAH ANDA YAKIN INGIN MENGHAPUS FORUM \"{forumDipilih}\"?")
            print("> Y. YA")
            print("> N. TIDAK")
            pilihan = input("TENTUKAN DENGAN BIJAK: ")
            while True:
                if pilihan != "":
                    if pilihan.lower() == "y":
                        input("TELAH DIMUSNAHKAN...!")
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
        elif (pilihan.lower() == "p" or pilihan.lower() == usernamePengguna) and guest == False:
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
        listModeratorForum = []
        moderator = False

        for i, momod in enumerate(forum[forumDipilih]["moderator"]):
            listModeratorForum.append(momod)
            if (usernamePengguna == momod):
                moderator = True
        if moderator == False and pengguna[usernamePengguna]["level"] != "admin":
            halaman = "forum"
            break
        print(f"> {usernamePengguna} {"="*30}")
        print(f"|| Manajemen Mod {forumDipilih} ||")
        print()
        print(f"> T. Tambah Moderator | > D. Hapus Moderator")
        print(f"{"-"*25}")
        for i, momod in enumerate(forum[forumDipilih]["moderator"]):
            print(f"{i+1}. {momod}")
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
                    for username, itemPengguna in pengguna.items():
                        if usernameMomodBaru == username:
                            penggunaDitemukan = username
                            penggunaValid = True
                            for j, momod in enumerate(forum[forumDipilih]["moderator"]):
                                if (penggunaDitemukan == momod):
                                    penggunaValid = False
                                    break
                            break
                    if penggunaValid:
                        input(f"Berhasil menambahkan \"{penggunaDitemukan}\" sebagai Moderator!")
                        forum[forumDipilih]["moderator"].append([penggunaDitemukan])
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
            for i, momod in enumerate(forum[forumDipilih]["moderator"]):
                if (pilihan == str(i + 1)):
                    if (i == 0):
                        input("Tidak dapat mengkudeta pemilik forum!")
                    else:
                        akunDihapus = forum[forumDipilih]["moderator"].pop(i)
                        input(f"Berhasil mengkudeta \"{akunDihapus[0]}\"!")
                    break
        elif (pilihan.lower() == "p" or pilihan.lower() == usernamePengguna) and guest == False:
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

        if (len(postDipilih) < 1):
            halaman = "forum post"
            break
        
        print(f"> {usernamePengguna} {"="*30}")
        print(f"|| {postDipilih} ||")
        print()
        print(post[postDipilih]["konten"])
        print(f"{"-"*25}")
        print("Komentar:")
        nomor = 0
        for idBalasan, itemBalasan in balasan.items():
            if (len(itemBalasan["konteks"]) == 1 and itemBalasan["konteks"]["post"] == postDipilih):
                nomor += 1
                if nomor != 1: print()
                komentarMod = False
                for j, cekMod in enumerate(forum[forumDipilih]["moderator"]):
                    if (itemBalasan["author"] == cekMod):
                        komentarMod = True
                        break
                usernameKomentar = itemBalasan["author"] + (" (Admin)" if pengguna[itemBalasan["author"]]["level"] == "admin" else " (Moderator)" if komentarMod else "")
                print(f"> {nomor}. {usernameKomentar}: {itemBalasan['konten']}")
                komentarPostTerfilter.append([nomor, idBalasan])
                for idBalasanKomentar, itemBalasanKomentar in balasan.items():
                    for l, cekMod in enumerate(forum[forumDipilih]["moderator"]):
                        if (itemBalasanKomentar["author"] == cekMod):
                            komentarMod = True
                            break
                    usernameKomentar = itemBalasanKomentar["author"] + (" (Admin)" if pengguna[itemBalasanKomentar["author"]]["level"] == "admin" else " (Moderator)" if komentarMod else "")
                    if (len(itemBalasanKomentar["konteks"]) == 2 and idBalasan == itemBalasanKomentar["konteks"]["balasan"]):
                        print(f"  +--{"-"*(len(str(nomor)))}> {usernameKomentar}: {itemBalasanKomentar['konten']}")

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
                balasan[len(balasan) + 1] = {
                    "author": usernamePengguna,
                    "konten": komentarBaru,
                    "konteks": {
                        "post": postDipilih
                    }
                }
            else:
                input("Komentar Dibatalkan...!")
        elif pilihan.lower() == str(komentarDipilih[0] if len(komentarDipilih) > 0 else ""):
            print(f"{"="*40}")
            print("|| Balasan Komentar ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            balasanKomentarBaru = input("Balasan: ")

            if balasanKomentarBaru != "":
                balasan[len(balasan) + 1] = {
                    "author": usernamePengguna,
                    "konten": balasanKomentarBaru,
                    "konteks": {
                        "post": postDipilih,
                        "balasan": komentarDipilih[1]
                    }
                }
            else:
                input("Balasan Komentar Dibatalkan...!")
        elif (pilihan.lower() == "p" or pilihan.lower() == usernamePengguna) and guest == False:
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
        print(f"Akun: {usernamePengguna}")
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
                pengguna[usernameBaru] = pengguna.pop(usernamePengguna)
                usernamePengguna = usernameBaru
                input("Username Berhasil Diperbarui...!")
            else:
                input("Perubahan Username Dibatalkan...!")
        elif pilihan == "2":
            print(f"> {usernamePengguna} {"="*30}")
            print("|| Update Password ||")
            print()
            print("(Ket: Kosongkan input untuk membatalkan.)")
            passwordLama = input("Masukkan Password Lama Anda: ")
            if pengguna[usernamePengguna]["password"] == passwordLama and passwordLama != "":
                passwordBaru = input("Masukkan Password Baru Anda: ")
                if passwordBaru != "":
                    pengguna[usernamePengguna]["password"] = passwordBaru
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