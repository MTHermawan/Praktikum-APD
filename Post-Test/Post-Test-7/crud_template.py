import os

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

post = {
    "Lorem Ipsum": {
        "author": "user",
        "konten": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "forum": "Teknologi"
    }
}

balasan = {
    "0" : {
        "author": "user",
        "konten": "Halo Obrolan",
        "konteks": {
            "post": "Lorem Ipsum",
        }
    },
    "1" : {
        "author": "user",
        "konten": "P",
        "konteks": {
            "post": "Lorem Ipsum",
            "balasan": ["0"]
        }
    },
    "2" : {
        "author": "user",
        "konten": "P",
        "konteks": {
            "post": "Lorem Ipsum",
            "balasan": ["0", "1"]
        }
    },
    "3" : {
        "author": "user",
        "konten": "P",
        "konteks": {
            "post": "Lorem Ipsum",
            "balasan": ["0", "1"]
        }
    },
    "4" : {
        "author": "user",
        "konten": "P",
        "konteks": {
            "post": "Lorem Ipsum",
        }
    },
    "5" : {
        "author": "user",
        "konten": "P",
        "konteks": {
            "post": "Lorem Ipsum",
            "balasan": ["0", "1", "2"]
        }
    },
    "6" : {
        "author": "user",
        "konten": "P",
        "konteks": {
            "post": "Lorem Ipsum",
            "balasan": ["0", "1", "2", "5"]
        }
    }
}

def TambahPengguna(_username, _password, _level = "user"):
    if _username and _password:
        if not pengguna.get(_username):
            pengguna.setdefault(_username, {
                "password": _password,
                "level": _level
            })
    return False

def EditPengguna(_oldusername, _newusername, _password, _level = "user"):
    if _oldusername and _newusername and _password:
        if pengguna.get(_oldusername):
            pengguna.pop(_oldusername)
            pengguna[_newusername] = {
                "password": _password,
                "level": _level
            }
            return True
    return False

def TambahPostingan(_judul, _usernameAuthor, _konten, _forum):
    if _judul and _konten and _forum:
        post[_judul] = {
            "author": _usernameAuthor,
            "konten": _konten,
            "forum": _forum
        }
        return True
    return False

def KomentarForum(_post):
    _idBalasan = None
    _level = 0
    _nomor = []
    _nomorIdKomentar = {}

    # Bismillah... Bisa nih pasti kali ini
    def RekursifKomentar(_idBalasan, _level, _nomor):
        for key, itemBalasan in balasan.items():
            konteksBalasan = itemBalasan["konteks"].get("balasan", [])
            if (itemBalasan["konteks"].get("post") == _post):
                if (len(konteksBalasan) == _level and ((_level == 0 and not _idBalasan) or (_level > 0 and _idBalasan in konteksBalasan))): 
                    if len(_nomor) < _level + 1:
                        _nomor.append(1)
                    else:
                        _nomor[_level] += 1
                        _nomor = _nomor[0:_level + 1]
                    _nomorIdKomentar.setdefault(key, {
                        "nomor": FormatNomorArray(_nomor),
                        "nomorUtama": _nomor[0]
                    })
                    RekursifKomentar(str(key), _level + 1, _nomor)
    RekursifKomentar(_idBalasan, _level, _nomor)
    return _nomorIdKomentar

def TampilkanKomentar(_judulPost):
    for id, items in KomentarForum(_judulPost).items():
        level = balasan[id]["konteks"].get("balasan")
        badge = "(Admin)" if CekAdmin(balasan[id]["author"]) else "(Moderator)" if CekModeratorForum(forum[post[_judulPost]["forum"]], balasan[id]["author"]) else ""
        content = f"{items['nomor']}. {balasan[id]['author']} {f"{badge} " if badge else ""}: {balasan[id]['konten']}"
        if not level:
            if items["nomorUtama"] > 1: print()
            print(f"> {content}")
        else:
            spasi = " " * (len(str(items["nomorUtama"])) + (len(level) * 2) + 2)
            print(f"{spasi}+-> {content}")

def BalasKomentarPost(_post, _usernameAuthor = None, _kontenKomentar = None, _komentarDipilih = None):
    if _komentarDipilih and _kontenKomentar:
        for id, items in KomentarForum(_post).items():
            if (balasan[id]["konteks"]["post"] == _post and items.get("nomor")):
                if (items["nomor"] == _komentarDipilih):
                    balasan.setdefault(str(len(balasan)), {
                        "author": _usernameAuthor,
                        "konten": _kontenKomentar,
                        "konteks": {
                            "post": _post,
                            "balasan": balasan[id]["konteks"].get("balasan", []) + [id]
                        }
                    })
                    return True
    elif _kontenKomentar:
        balasan.setdefault(str(len(balasan)), {
            "author": _usernameAuthor,
            "konten": _kontenKomentar,
            "konteks": {
                "post": _post
            }
        })
        return True
    return False

def TambahForum(_judul, _deskripsi, _moderator):
    if _judul and _deskripsi and _moderator:
        forum.setdefault(_judul, {
            "deskripsi": _deskripsi,
            "moderator": _moderator
        })
        return True
    return False

def CekPenggunaValid(_username):
    return KeyTerpakai(pengguna, _username)

def CekAdmin(_username):
    user = pengguna.get(_username)
    
    if user:
        return user["level"] == "admin"
    return False
    
def CekModeratorForum(_forum, _username):
    if CekPenggunaValid(_username):
        return _username in _forum["moderator"]
    return False

def CekPassword(_username, _password):
    if pengguna.get(_username):
        return (pengguna[_username]["password"] == _password)
    return False

def FormatNomorArray(nomorArr = [], indeks = 0):
    if indeks < len(nomorArr) - 1:
        return f"{nomorArr[indeks]}.{FormatNomorArray(nomorArr, indeks + 1)}"
    elif indeks == len(nomorArr) - 1:
        return f"{nomorArr[indeks]}"
    else:
        return ""
    
def KeyTerpakai(_dict: dict, _findKey: str):
    lowerDict = []
    if _dict and _findKey:
        for key in _dict.keys():
            lowerDict.append(key.lower())
        return _findKey.lower() in lowerDict
    return False