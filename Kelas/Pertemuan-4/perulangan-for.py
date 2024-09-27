# Pengenalan 'for'

print("perulangan ke-0")
print("perulangan ke-1")
#...
print("perulangan ke-9")

# Kode di atas dapat disingkat dengan perulangan 'for' di bawah ini

batas = 10
for i in range(1, batas, 2):
    print(f"Perulangan ke-{i}")

# -------------------------------------------
# parameter fungsi range(start, stop, step)
# -------------------------------------------

print()
# =======================================================================
# Penggunaan 'for' pada List

buahBuahan = ["apel", "mangga", "anggur"]

for buah in buahBuahan:
    print(buah)

print()
# =======================================================================
# Nested 'for' (perulangan 'for' di dalam perulangan 'for')

for baris in range(1, 4):
    print("Baris ke", baris)
    for kolom in range(1, 4):
        print(kolom, "kolom", end=" ")
    print()
print()