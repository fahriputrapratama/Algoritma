a = True
b = False

print("a AND b" , a and b)
print("a OR b ", a or b)
print("NOT B", not b)

name = input("silahkan masukan nama : ")
sudah_bayar = True
absensi = int(input('masukan nilai absensi : '))
if (sudah_bayar==True and absensi >= 70):
    print(f"{name} Boleh ujian")
else:
    print("{name} MINIMAL ADUS")