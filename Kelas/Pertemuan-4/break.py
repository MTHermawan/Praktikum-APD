for i in range(1, 10):
    if i == 4:
        break
    else:
        print(f"Perulangan ke-{i}")

# perulangan di atas akan berhenti pada perulangan ke-4

# =======================================================================

while True:
    ulang = input("Mabar lagi: ")

    if ulang == "gk":
        break
    print("Mabar lagi")

# Program akan berhenti ketika user input "gk"