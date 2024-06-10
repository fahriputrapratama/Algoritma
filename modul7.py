stok_barang = []

def tambah_barang(nama_barang, jumlah_stok):
    barang = {
        'nama': nama_barang,
        'stok': jumlah_stok
    }
    stok_barang.append(barang)
    print(f"Barang '{nama_barang}' dengan stok {jumlah_stok} berhasil ditambahkan.")

def hapus_barang(index):
    if 0 <= index < len(stok_barang):
        barang = stok_barang.pop(index)
        print(f"Barang '{barang['nama']}' berhasil dihapus.")
    else:
         print('index tidak valid')


def tampilkan_barang():
    if not stok_barang:
        print("Tidak ada data barang yang tersimpan.")
    else:
        print("Data Barang:")
        for barang in stok_barang:
            print(f"Nama: {barang['nama']}, Stok: {barang['stok']}")
def pilihan():
  while True:
    print('Selamat datang di program Manajemen Stok Barang!')
    print('Pilihan : ')
    print('1. Tambah Data Barang')
    print('2. Hapus Data Barang')
    print('3. Tampilkan Data Barang')
    print('4. keluar','\n')
    pilihan = input('Masukkan Pilihan : ')

    if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            jumlah_stok = int(input("Masukkan jumlah stok: "))
            tambah_barang(nama_barang, jumlah_stok)
    elif pilihan == '2':
            index = int(input("Masukkan index yang ingin dihapus: "))
            hapus_barang(index)
    elif pilihan == '3':
            tampilkan_barang()
    elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem manajemen stok barang.")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
pilihan()