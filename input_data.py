"""cara menginput data"""
nama_benda = str(input("Masukan nama benda : "))
jumlah = int(input("masukan jumldah : "))
harga = float(input("masukan harga : "))
ketentuan = bool(input("masukan ketentuan : "))
print(nama_benda)
print(jumlah)
print(harga)
print(ketentuan)

"""input array"""
my_biodata = []

nomor_induk = int(input("masukan NIM : "))
nama_saya = str(input("Masukan nama : "))

class_biodata = [nomor_induk,nama_saya]
my_biodata.append(class_biodata)
print (my_biodata)

buah = {
    'nama buah' : 'semangka',
    'harga':20.000,
    'jumlah':20,
    'ketersediaan':True
}