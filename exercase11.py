stack = []
stack2 = []

while True:
        print(f'riwayat pencarian saat ini : {stack}')
        print('Pilihan : ')
        print('1. Tambah Pencarian')
        print('2. Hapus Pencarian Terakhir')
        print('3. Undo')
        print('4. keluar','\n')
        pilihan = input('Pilih Operasi (1/2/3/4) : ')

        if pilihan == '1':
            bahasa = str(input('Masukkan kata kunci pencarian : '))
            stack.append(bahasa)
            print(f'{bahasa} berhasil ditambahkan')
        elif pilihan == '2':
            data = stack.pop()
            stack2.append(data)
            print(f'{data} dihapus dari riwayat pencarian')
        elif pilihan == '3':
            if len(stack) == 0:
                 print('tidak ada yang bisa diundo')
            else:
                data = stack2.pop()
                stack.append(data)
                print(f'{data} dikembalikan ke riwayat pencarian')
        elif pilihan == '4':
            print("SUWUN")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
pilihan()
