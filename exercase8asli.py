from module8 import tampilkan_hasil
def main():
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    nilai = []
    
    for i in range(jumlah_siswa):
        nilai.append(int(input(f"Masukkan nilai ujian siswa ke-{i+1}: ")))

    tampilkan_hasil(nilai)
    
main()