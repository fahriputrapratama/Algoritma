print("----//---- Gaji Karyawan ----//----")
#menginput data
nama_karyawan = str(input('masukan nama karyawan : '))
jam = int(input('masukan jam kerja dalam satu hari : '))
tarif = int(input("masukan tarif perjam : "))

#pengkalian jumlah jam kerja dengan hari (20) dengan menggunakan operator penugasan
jam *= 20 #hari

#memasukan total gaji perbulan
total_gaji = jam * tarif

#printout hasil
print(f"{nama_karyawan}, memiliki gaji perbulan yaitu : {total_gaji:,.2f} Rupiah")