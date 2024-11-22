import os
import json

os.system("clear || cls")

# txt = text
# json = javascript object notation
# csv =

# with open("D:\Kuliah (Git Repository)\Praktikum-APD\Pertemuan-8\data.txt", "r") as file:
#     konten = file.read()
#     print(konten)

# with open("D:\Kuliah (Git Repository)\Praktikum-APD\Pertemuan-8\data.txt", "a") as file:
#     file.write("Hermawan,18,Pria.\n")

path = "D:\Kuliah (Git Repository)\Praktikum-APD\Pertemuan-8\data-json.json"

def ReadData():
    with open(path) as jsonFile:
        return json.load(jsonFile)
    
def WriteData(newData):
    data = ReadData()
    data.append(newData)
    with open(path, "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

newParam = {
    "nama" : "Hermawan",
    "umur" : "18",
    "jenis_kelamin" : "pria"
}

data = ReadData()
print(data)

WriteData(newParam)