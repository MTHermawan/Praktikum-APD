import os

def garis(karakter: str = "=", panjang = 40):
    print(f"{karakter*panjang}")

def CariKey_Indeks(_dict: dict, _urut: str):
    i = 0
    for key in _dict.keys():
        i += 1
        if str(i) == _urut:
            return key
    return ""

def EditKey(_dict, _keyDipilih, _keyBaru):
    cache = _dict[_keyDipilih]
    _dict.pop(_keyDipilih)
    _dict[_keyBaru] = cache

def HapusDictionary(_dict: dict, _key):
    if _dict.get(_key):
        _dict.pop(_key)
        return True
    return False

def BersihkanTerminal():
    os.system("cls || clear")