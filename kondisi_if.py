# Kondisi if 

nilai = 80
if nilai >75:
    print("Kamu Lulus")

angka = int(input("Masukan Angka [range 0-100 ]: "))
if angka < 0 or angka > 100:
    print("Error : Nilai Range 0 - 100")
    exit() # digunakan untuk keluar dari if
print("Benar")

# kondisi if else

idris = int(input("Masukan Nilai mu : "))
if idris > 75:
    print("Idris Lulus")
else:
    print("Idris tidak lulus")

# Kondisi if else 2 kondisi