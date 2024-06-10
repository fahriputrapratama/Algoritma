
def ratarata(nilai):
    rata_rata = sum(nilai)/len(nilai)
    print(rata_rata)

def tertinggi(nilai):
    nilai_tertinggi = max(nilai)
    print(nilai_tertinggi)

def terendah(nilai):
    nilai_terendah = min(nilai)
    print(nilai_terendah)

def diatas_rata(nilai):
    jumlah_nilai_diatas_ratarata = sum(True for i in nilai if i > ratarata)
    print(jumlah_nilai_diatas_ratarata)

def tampilkanhasil(nilai):
    rata_rata = ratarata(nilai)
    nilai_tertinggi= tertinggi(nilai)
    nilai_terendah = terendah(nilai)
    nilai_diatas_rata = diatas_rata(nilai)

    print(rata_rata)
    print(nilai_tertinggi)
    print(nilai_terendah)
    print(nilai_diatas_rata)