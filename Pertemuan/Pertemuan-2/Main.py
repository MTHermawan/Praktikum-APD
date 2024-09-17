import json
import pip._vendor.requests as requests

# hello_world = "Hello World"
# print(hello_world[6:11])


# tuple

# warna = {
#     "warna1" : "merah",
#     "warna2" : "kuning",
#     "warna3" : "hijau"
# }

# print(warna["warna2"])

# nama = input("Masukkan nama Anda : ")
# print(f"Nama Anda adalah {nama}")

# angka = int(input("Masukkan angka Anda : "))
# print(f"Angka Anda adalah {angka + 5}")

# print(2 > 3)

api_url = "https://api.currencyapi.com/v3/latest?apikey=cur_live_pHL3hh4hVnEzabJLSqZhmD07iBrdCzPgaFSnL3nv&currencies=EUR%2CUSD%2CJPY&base_currency=IDR"
jsonResponse = requests.get(api_url)

usdValue = jsonResponse.json()["data"]["USD"]["value"]
eurValue = jsonResponse.json()["data"]["EUR"]["value"]
yenValue = jsonResponse.json()["data"]["JPY"]["value"]

rupiah = int(input("Masukkan nilai rupiah yang diinginkan : "))

usd = rupiah * usdValue
yen = rupiah * eurValue
eur = rupiah * yenValue

print(f"US Dollar: ${usd}")
print(f"Yen:  ¥{yen}")
print(f"Euro: €{eur}")