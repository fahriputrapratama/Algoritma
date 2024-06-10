# Untuk menggabungkan dua atau lebih string menjadi satu, Anda dapatmenggunakan operator + atau metode join(). Dan ketika ingin menduplikatstring dapat menggunakan operator *
string1 = "Hello"
string2 = "World"
int1 = 5
print(string1 + " "+string2)
print((string1 + " ")*20)
print(string1 + str(int1))

# Penggabungan string
daftar_kata = ["ini", "adalah" , "sebuah", "karya"]
kalimat = " ".join(daftar_kata) # Fungsi join digunakan untuk menggabung kan variabel bertipe string
print(kalimat)

# Memisahkan string
# Untuk memisahkan string menjadi bagian-bagian yang lebih kecil, Andadapat menggunakan metode split().
kalimat = "ini adalah sebuah karya" #Perkata merupakan Substring
print(kalimat[0:10])
daftar_kata = kalimat.split()
print(daftar_kata) 
substring = kalimat.replace("karya","kalimat")
print(substring)


# Lowercase dan Uppercase
# Lowercase dan Uppercase adalah istilah yang digunakan dalammanipulasi string untuk merujuk pada proses pengubahan huruf dalamsebuah teks menjadi huruf kecil atau huruf besar.
nama = "muhammad iqbal saputra"
print(nama.lower()) # Huruf kecil
print(nama.upper()) # Huruf Besar
print(nama.capitalize()) # Huruf Kapital
print(nama.title()) # Judul / perkata di kapitalkan

# Format dengan Mata Uang
harga = 2500000
print('{:,}'.format(harga))# menambahkan titik (output 2,500,000)
print('{:.2f}'.format(harga))# menambahkan bilangan desimal (output 2500000.00)
print('{:,.2f}'.format(harga))# menambahkan bilangan desimal dan titik (output 2,500,000.00)

print (f'{harga:,}')