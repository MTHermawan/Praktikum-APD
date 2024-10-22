import os
from crud_template import *
from fungsi_prosedur import *

# Deklarasi Variabel
guest = False
usernamePengguna = ""
pilihan = ""
halaman = "login"
riwayatHalaman = [halaman]
forumDipilih = ""
postDipilih = ""

def TambahRiwayatHalaman(halaman):
    if (riwayatHalaman[len(riwayatHalaman) - 1] != halaman):
        riwayatHalaman.append(halaman)

def KembaliHalaman():
    if (len(riwayatHalaman) > 1):
        riwayatHalaman.pop()
        return riwayatHalaman[len(riwayatHalaman) - 1]
    return halaman

def CekLogin():
    return usernamePengguna or guest

def Logout():
    global usernamePengguna
    global guest
    global halaman
    global pilihan
    global forumDipilih
    global postDipilih

    usernamePengguna = ""
    guest = False
    halaman = "login"
    pilihan = ""
    forumDipilih = ""
    postDipilih = ""
    return halaman

while pilihan.lower() != "n":
    # Isi Semua Halaman Program

    # Halaman Log In
    while halaman == "login" and not CekLogin():
        guest = False
        BersihkanTerminal()

        garis()
        print(f"|| Forum Diskusi Online ||")
        garis("-", 30)
        print(f"1. Pengguna Baru? Buat Akun Baru")
        print(f"2. Sudah Punya Akun? Log In")
        print(f"3. Masuk sebagai Guest")
        garis("-", 30)
        print(f"N. Keluar dari Program")
        print()
        pilihan = input("Masukkan Pilihan Anda: ")
        print("="*40)
        
        match (pilihan.lower()):
            case "1":
                print("|| REGISTER ||")
                print()
                print("(Ket: Kosongkan input untuk membatalkan.)")
                while True:
                    inputUsername = input("Username: ")
                    if (KeyTerpakai(pengguna, inputUsername)):
                        print("Username telah digunakan!")
                        print()
                    elif (inputUsername):
                        inputPassword = input("Password: ")
                        if (TambahPengguna(inputUsername, inputPassword)):
                            input("Pengguna Berhasil Ditambahkan...!")
                            break
                        else:
                            input("Register dibatalkan...!")
                            break
                    else:
                        input("Register dibatalkan...!")
                        break  
            case "2":
                print("|| LOG IN ||")
                print()
                print(("(Ket: Kosongkan input untuk membatalkan.)"))
                inputUsername = input("Username: ")
                if not inputUsername:
                    input("Login dibatalkan...!")
                    break
                inputPassword = input("Password: ")
                if (inputUsername and inputPassword):
                    if (CekPassword(inputUsername, inputPassword)):
                        usernamePengguna = inputUsername
                        input("Login Berhasil...!")
                        halaman = "menu utama"
                    else:
                        input("Username atau Password Salah...!")
                else:
                    input("Login dibatalkan...!")
            case "3":
                guest = True
                halaman = "menu utama"
            case "n":
                break
            case _:
                input("Pilihan Tidak Valid...!")

    if CekLogin():
        # Halaman Menu Utama
        while halaman == "menu utama":
            BersihkanTerminal()
            TambahRiwayatHalaman(halaman)

            print(f"> {usernamePengguna} {"="*30}")
            print(f"|| Menu Utama ||")
            if not guest:
                print()
                print(f"Selamat Datang, {usernamePengguna}!")
            garis("-", 30)
            print(f"> 1. Lihat Forum")
            if (CekAdmin(usernamePengguna)):
                print(f"> 2. Dashboard")
                print(f"> 3. Pengguna")
            garis("-", 30)
            print(f"> {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
            print()
            pilihan = input("Masukkan pilihan Anda: ")

            match (pilihan.lower()):
                case "1":
                    halaman = "forum"
                case "2" if CekAdmin(usernamePengguna):
                    halaman = "dashboard"
                case "3" if CekAdmin(usernamePengguna):
                    halaman = "pengguna"
                case "l" if guest:
                    halaman = Logout()
                case "n":
                    break
                case _ if (pilihan.lower() == "p" or CekPenggunaValid(pilihan)) and not guest:
                    halaman = "pengaturan"
                case _:
                    input("Pilihan Tidak Valid...!") 

        # Halaman Forum
        while halaman == "forum":
            BersihkanTerminal()
            TambahRiwayatHalaman(halaman)
            forumDipilih = ""

            print(f"> {usernamePengguna} {"="*30}")
            print("|| Forum ||")
            print()
            if not guest:
                print(f"> T. Buat Forum")
            garis("-", 30)
            i = 0
            for namaForum, itemForum in forum.items():
                print(f"> {i+1}. {namaForum}")
                i += 1
            if (len(forum) < 1):
                print("Belum ada forum. Jadilah yang pertama untuk menambahkan!")
            garis("-", 30)
            print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
            print()
            pilihan = input("Masukkan pilihan Anda: ")

            forumDipilih = CariKey_Indeks(forum, pilihan)

            match (pilihan.lower()):
                case "t" if not guest:
                    garis()
                    print("|| Buat Forum ||")
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    while True:                            
                        judulForumBaru = input("Masukkan Judul Forum Anda: ")
                        if (KeyTerpakai(forum, judulForumBaru)):
                            input("Judul forum sudah ada...!")
                            print()
                        elif (judulForumBaru):
                            deskripsiForumBaru = input("Masukkan Deksripsi Forum Anda: ")
                            if (TambahForum(judulForumBaru, deskripsiForumBaru, [usernamePengguna])):
                                input("Forum Berhasil Ditambahkan...!")
                                forumDipilih = judulForumBaru
                                halaman = "forum post"
                                break
                            else:
                                input("Pembuatan Forum Dibatalkan...!")
                                break
                        else:
                            input("Pembuatan Forum Dibatalkan...!")
                            break
                case "l" if guest:
                    halaman = Logout()
                case "n" | "b":
                    break
                case _ if forumDipilih:
                    halaman = "forum post"
                case _ if (pilihan.lower() == "p" or CekPenggunaValid(pilihan)) and not guest:
                    halaman = "pengaturan"
                case _:
                    input("Pilihan Tidak Valid...!")

        # Halaman Dashboard
        while halaman == "dashboard" and CekAdmin(usernamePengguna):
            BersihkanTerminal()

            print(f"> {usernamePengguna} {"="*30}")
            print("|| Dashboard ||")
            print()
            garis("-", 30)
            print(f"Total Forum = {len(forum)}")
            print(f"Total Postingan = {len(post)}")
            print(f"Total Pengguna = {len(pengguna)}")
            garis("-", 30)
            print()
            input("Kembali ke Menu Utama...")
            pilihan = "b"
            break

        # Halaman Manajemen Penggna
        while halaman == "pengguna" and CekAdmin(usernamePengguna):
            BersihkanTerminal()
            TambahRiwayatHalaman(halaman)

            penggunaDipilih = ""

            print(f"> {usernamePengguna} {"="*30}")
            print("|| Pengguna ||")
            print()
            print(f"> T. Tambah Pengguna | > E. Edit Pengguna | > D. Hapus Pengguna")
            garis("-", 30)
            i = 0
            for username, itemPengguna in pengguna.items():
                print(f"{i+1}. Username: {username}, Pass: {itemPengguna.get("password", "")}, Level: {itemPengguna.get("level", "")}")
                i += 1
            garis("-", 30)
            print(f"> B. Kembali | > P. Pengaturan | > N. Keluar dari Program")
            print()
            pilihan = input("Masukkan pilihan Anda: ")

            match (pilihan.lower()):
                case "t":
                    garis()
                    print("|| Tambah Pengguna ||")
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    while True:
                        inputUsername = input("Username: ")
                        if (KeyTerpakai(pengguna, inputUsername)):
                            print("Username telah digunakan!")
                            print()
                        elif (inputUsername):
                            inputPassword = input("Password: ")
                            if (not inputPassword):
                                input("Gagal menambahkan pengguna...!")
                                break
                            print("Pilih Level: ")
                            print("1. Admin")
                            print("2. User")
                            inputLevel = ""
                            while inputPassword:
                                pilihan = input("Pilih level: ")
                                match (pilihan):
                                    case "1":
                                        inputLevel = level[0]
                                        break
                                    case "2":
                                        inputLevel = level[1]
                                        break
                                    case "":
                                        break
                                    case _:
                                        print("Pilihan tidak valid!\n")
                            if (TambahPengguna(inputUsername, inputPassword, inputLevel)):
                                input("Pengguna Berhasil Ditambahkan...!")
                                break
                            else:
                                input("Gagal menambahkan Pengguna...!")
                                break
                        else:
                            input("Gagal menambahkan pengguna...!")
                            break
                case "e":
                    print("\n(Ket: Kosongkan input untuk membatalkan.)")
                    while True:
                        pilihan = input("Pilih pengguna yang ingin diedit: ")
                        if (pilihan):
                            penggunaDipilih = CariKey_Indeks(pengguna, pilihan)
                            if penggunaDipilih:
                                break
                            input("Pengguna tidak ditemukan...!")
                            print()
                        else:
                            input("Edit berhasil dibatalkan...!")
                            break

                    if not penggunaDipilih: break
                    garis()
                    print(f"|| Edit Pengguna \"{penggunaDipilih}\" ||")
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    while True:
                        inputUsername = input("Username: ")
                        if (KeyTerpakai(pengguna, inputUsername) and inputUsername != penggunaDipilih):
                            print("Username telah digunakan!")
                            print()
                        elif (inputUsername):
                            inputPassword = input("Password: ")
                            if (not inputPassword):
                                input("Edit berhasil dibatalkan...!")
                                break

                            print("Pilih Level: ")
                            print("1. Admin")
                            print("2. User")
                            inputLevel = ""
                            while inputPassword:
                                pilihan = input("Pilih level: ")
                                match (pilihan):
                                    case "1":
                                        inputLevel = level[0]
                                        break
                                    case "2":
                                        inputLevel = level[1]
                                        break
                                    case "":
                                        break
                                    case _:
                                        print("Pilihan tidak valid!\n")
                            if (not inputLevel):
                                input("Edit berhasil dibatalkan...!")
                                break

                            if (EditPengguna(penggunaDipilih, inputUsername, inputPassword, inputLevel)):
                                input("Pengguna Berhasil Diedit...!")
                                break
                            else:
                                input("Gagal Mengedit Pengguna...!")
                                break
                        else:
                            input("Edit berhasil dibatalkan...!")
                            break
                case "d":
                        pilihan = input("Pilih pengguna yang ingin dihapus: ")
                        if HapusDictionary(pengguna, CariKey_Indeks(pengguna, pilihan)):
                            input("Pengguna Berhasil Dihapus...!")
                        else:
                            input("Gagal Menghapus Pengguna...!")
                case "l" if guest:
                    halaman = Logout()
                case "n" | "b":
                    break
                case _ if (pilihan.lower() == "p" or CekPenggunaValid(pilihan)) and not guest:
                    halaman = "pengaturan"
                case _:
                    input("Pilihan Tidak Valid...!")

        # Halaman List Post dari Forum
        while halaman == "forum post":
            BersihkanTerminal()
            TambahRiwayatHalaman(halaman)

            postForumTerfilter = []
            postDipilih = ""
            moderator = CekModeratorForum(forum[forumDipilih], usernamePengguna)

            print(f"> {usernamePengguna} {"="*30}")
            print(f"|| Forum {forumDipilih} ||")
            print()
            if not guest:
                print(f"> T. Buat Postingan {"| > M. Manajemen Forum" if moderator or CekAdmin(usernamePengguna) else ""}")
            garis("-", 30)
            print(f"Deskripsi: {forum[forumDipilih]['deskripsi']}")
            print()
            print(f"Postingan:")
            nomor = 0
            for namaPost, itemPost in post.items():
                if (itemPost["forum"] == forumDipilih):
                    nomor += 1
                    print(f"> {nomor}. {namaPost}: {itemPost['konten']}")
                    postForumTerfilter.append([nomor, namaPost])
            if len(postForumTerfilter) < 1:
                print("Belum ada postingan. Jadilah yang pertama untuk menambahkan!" if not guest else "Belum ada postingan.")
            garis("-", 30)
            print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
            print()
            pilihan = input("Masukkan pilihan Anda: ")

            postDipilih = CariKey_Indeks(post, pilihan)

            match (pilihan.lower()):
                case "t" if not guest:
                    print("="*40)
                    print("|| Buat Postingan ||")
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    judulPostinganBaru = input("Judul Postingan: ")

                    if judulPostinganBaru:
                        kontenPostinganBaru = input("Konten: ")
                        if (TambahPostingan(judulPostinganBaru, usernamePengguna, kontenPostinganBaru, forumDipilih)):
                            input("Postingan Berhasil Ditambahkan...!")
                        else:
                            input("Batal membuat postingan...!") 
                    else:
                        input("Batal membuat postingan...!")
                case "m" if moderator or CekAdmin(usernamePengguna):
                    halaman = "manajemen forum"
                case "l" if guest:
                    halaman = Logout()
                case "n" | "b":
                    break
                case _ if postDipilih:
                    halaman = "post"
                case _ if (pilihan.lower() == "p" or CekPenggunaValid(pilihan)) and not guest:
                    halaman = "pengaturan"
                case _:
                    input("Pilihan Tidak Valid...!")
        
        # Halaman List Post dari Forum
        while halaman == "manajemen forum":
            BersihkanTerminal()
            TambahRiwayatHalaman(halaman)

            postForumTerfilter = []
            moderator = CekModeratorForum(forum[forumDipilih], usernamePengguna)

            if not moderator or not CekAdmin(usernamePengguna):
                halaman = "forum"
                break

            print(f"> {usernamePengguna} {"="*30}")
            print(f"|| Manajemen Forum \"{forumDipilih}\" ||")
            print()
            garis("-", 30)
            print(f"> 1. Moderator")
            print(f"> 2. Ganti Judul Forum")
            print(f"> 3. Ganti Deskripsi Forum")
            print(f"> 4. Hapus Forum")
            garis("-", 30)
            print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
            print()
            pilihan = input("Masukkan pilihan Anda: ")

            match (pilihan.lower()):
                case "1":
                    halaman = "manajemen mod"
                case "2":
                    garis()
                    print("|| Update Judul Forum ||")
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    while True:
                        judulBaru = input("Masukkan Judul Baru Forum: ")
                        if KeyTerpakai(forum, judulBaru):
                            print("Judul forum sudah ada!\n")
                            print()
                        elif judulBaru:
                            EditKey(forum, forumDipilih, judulBaru)
                            input("Judul Forum Berhasil Diperbarui...")
                            break
                        else:
                            input("Batal mengubah judul forum...!")
                            break
                case "3":
                    garis()
                    print("|| Update Deskripsi Forum ||")
                    print()
                    print(f"Deskripsi Saat Ini: \"{forum[forumDipilih]["deskripsi"]}\"")
                    garis("-", 30)
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    while True:
                        deskripsiBaru = input("Deskripsi Baru: ")
                        if deskripsiBaru:
                            forum[forumDipilih]["deskripsi"] = deskripsiBaru
                            input("Deskripsi Forum Berhasil Diperbarui...!")
                            break
                        else:
                            input("Batal mengubah deskripsi forum...!")
                            break
                case "4":
                    print()
                    print(f"APAKAH ANDA YAKIN INGIN MENGHAPUS FORUM \"{forumDipilih}\"?")
                    print("> Y. YA")
                    print("> N. TIDAK")
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    while True:
                        pilihan = input("TENTUKAN DENGAN BIJAK: ")
                        if pilihan:
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
                                print()
                        else:
                            input("SUNGGUH MENARIK...")
                            break
                case "l" if guest:
                    halaman = Logout()
                case "n" | "b":
                    break
                case _ if (pilihan.lower() == "p" or CekPenggunaValid(pilihan)) and not guest:
                    halaman = "pengaturan"
                case _:
                    input("Pilihan Tidak Valid...!")
        
        # Halaman List Post dari Forum
        while halaman == "manajemen mod":
            BersihkanTerminal()
            TambahRiwayatHalaman(halaman)
            
            postForumTerfilter = []
            listModeratorForum = []
            moderator = CekModeratorForum(forum[forumDipilih], usernamePengguna)

            if not moderator or not CekAdmin(usernamePengguna):
                halaman = "forum"
                break

            print(f"> {usernamePengguna} {"="*30}")
            print(f"|| Manajemen Mod {forumDipilih} ||")
            print()
            print(f"> T. Tambah Moderator | > D. Hapus Moderator")
            garis("-", 30)
            for i, momod in enumerate(forum[forumDipilih]["moderator"]):
                print(f"{i+1}. {momod}")
            garis("-", 30)
            print(f"> B. Kembali | > {"L. Log in" if guest else "P. Pengaturan"} | > N. Keluar dari Program")
            print()
            pilihan = input("Masukkan pilihan Anda: ")

            match (pilihan.lower()):
                case "t":
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    while True:
                        usernameMomodBaru = input("Username Moderator Baru: ")
                        if usernameMomodBaru:
                            if (CekModeratorForum(forum[forumDipilih], usernameMomodBaru)):
                                input("Pengguna sudah menjadi Moderator!")
                                break
                            elif (CekPenggunaValid(usernameMomodBaru)):
                                forum[forumDipilih]["moderator"].append(usernameMomodBaru)
                            else:
                                input("Pengguna tidak ditemukan...!")
                                break
                        else:
                            input("Batal menambahkan moderator...!")
                            break
                case "d":
                    garis()
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
                case "l" if guest:
                    halaman = Logout()
                case "n" | "b":
                    break
                case _ if (pilihan.lower() == "p" or CekPenggunaValid(pilihan)) and not guest:
                    halaman = "pengaturan"
                case _:
                    input("Pilihan Tidak Valid...!")
        
        # Halaman Konten Suatu Post
        while halaman == "post":
            BersihkanTerminal()
            TambahRiwayatHalaman(halaman)

            if (len(postDipilih) < 1):
                halaman = "forum post"
                break

            dataNomorKomentar = []
            for value in KomentarForum(postDipilih).values():
                dataNomorKomentar.append(value["nomor"])
            
            print(f"> {usernamePengguna} {"="*30}")
            print(f"|| {postDipilih} ||")
            print()
            print(post[postDipilih]["konten"])
            garis("-", 30)
            print("Komentar:")

            TampilkanKomentar(postDipilih)

            garis("-", 30)
            if guest:
                print(f"> B. Kembali | > L. Log in | > N. Keluar dari Program")
            else:
                print(f"> K. Komentar | > B. Kembali | > P. Pengaturan | > N. Keluar dari Program")
            print()
            pilihan = input("Masukkan pilihan Anda: ")

            match (pilihan.lower()):
                case "k" if not guest:
                    garis()
                    print("|| Komentar ||")
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    kontenKomentar = input("Komentar: ")

                    if kontenKomentar:
                        BalasKomentarPost(postDipilih, usernamePengguna, kontenKomentar)
                    else:
                        input("Komentar Dibatalkan...!")
                case _ if pilihan.lower() in dataNomorKomentar and not guest:
                    garis()
                    print("|| Balasan Komentar ||")
                    print()
                    print("(Ket: Kosongkan input untuk membatalkan.)")
                    balasanKomentarBaru = input("Balasan: ")

                    if balasanKomentarBaru:
                        BalasKomentarPost(postDipilih, usernamePengguna, balasanKomentarBaru, pilihan)
                    else:
                        input("Balasan Komentar Dibatalkan...!")
                case _ if (pilihan.lower() == "p" or pilihan.lower() == usernamePengguna) and not guest:
                    halaman = "pengaturan"
                case "l" if guest:
                    halaman = Logout()
                case "n" | "b":
                    break
                case _:
                    input("Pilihan Tidak Valid...!")

        # Halaman Pengaturan
        while halaman == "pengaturan":
            if guest:
                halaman = "login"
                break
            BersihkanTerminal()
            TambahRiwayatHalaman(halaman)

            garis()
            print(f"|| Pengaturan ||")
            print()
            print(f"Akun: {usernamePengguna}")
            garis("-", 30)
            print(f"> 1. Update Username")
            print(f"> 2. Update Password")
            print(f"> 3. Log Out")
            garis("-", 30)
            print(f"> B. Kembali | > N. Keluar dari Program")
            print()
            pilihan = input("Masukkan pilihan Anda: ")

            match (pilihan):
                case "1":
                    garis()
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
                case "2":
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
                case "3":
                    halaman = Logout()
                    input("Berhasil Log Out...!")
                case "n" | "b":
                    halaman = ""
                case _:
                    input("Pilihan Tidak Valid...!")    

    # Kembali ke halaman sebelumnya
    if pilihan.lower() == "b":
        # Perulangan 2x untuk kembali ke dua halaman terakhir (termasuk halaman saat ini)
        halaman = KembaliHalaman()
        pilihan = ""
        continue
        
input("Program ditutup...")