def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai) 

def nilai_tertinggi(nilai):
    return max(nilai)

def nilai_terendah(nilai):
    return min(nilai)

def jumlah_di_atas_rata_rata(nilai):
    rata_rata = hitung_rata_rata(nilai)
    return len([n for n in nilai if n > rata_rata])

def tampilkan_hasil(nilai):
    rata_rata = hitung_rata_rata(nilai)
    tertinggi = nilai_tertinggi(nilai)
    terendah = nilai_terendah(nilai)
    di_atas_rata_rata = jumlah_di_atas_rata_rata(nilai)
    
    print(f"Rata-rata nilai ujian kelas: {rata_rata:.2f}")
    print(f"Nilai tertinggi dalam kelas: {tertinggi}")
    print(f"Nilai terendah dalam kelas: {terendah}")
    print(f"Jumlah siswa yang mendapatkan nilai di atas rata-rata: {di_atas_rata_rata}")
    
