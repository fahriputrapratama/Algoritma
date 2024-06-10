print('perhitungan rata rata nilai siswa'.upper())
jumlah_siswa = int(input('masukan jumlah siswa : '.title()))

nilai_awal = 0
for siswa in range (1, jumlah_siswa +1):
    nilai_siswa = int(input(f'Masukan Nilai Siswa Ke {siswa} : '))
    nilai_awal += nilai_siswa
rata_nilai = nilai_awal / jumlah_siswa
print(f"Jumlah rata rata nilai dari {jumlah_siswa} siswa adalah : ",rata_nilai)