buku = []
judul_buku = str(input("masukan judul buku : "))
tahun_terbit = int(input("masukan tahun terbit : "))
harga_buku = float(input("masukan harga buku : "))
penulis_buku = str(input("masukan penulis buku : "))
ketersediaan = bool(input("masukan ketersediaan : "))
buku_perpus = [judul_buku,tahun_terbit,harga_buku,penulis_buku,ketersediaan]
buku.append(buku_perpus)

angka_buku = int(input("masukan angka 1 sampai 10 : "))
print(buku)

print ('pilih nomor (1, 2, 3, 4 ,5)')
buku_1 = ["kancil", 2023, 150.000]
buku_2 = ["pinokio", 2015, 170.000]
buku_3 = ["oppenheimer", 2023, 180.000]
buku_4 = ["naruto", 2023, 100.000]
buku_5 = ["buaya anak nakal", 2023, 200.000]
input_buku = int(input("masukan angka : "))
if input_buku == 1:
    print(buku_1)
if input_buku == 2:
    print(buku_2)
if input_buku == 3:
    print(buku_3)
if input_buku == 4:
    print(buku_4)
if input_buku == 5:
    print(buku_5)