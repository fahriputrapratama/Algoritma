# deklarasi variabel data stack
data_stack = []

# penambahan data pada variabel data_stack dengan menggunakan fungsi append()
data_stack.append('Bagas')
data_stack.append('Fahri')
data_stack.append('Atha')
data_stack.append('Jarot')

# Printout
for index, name in enumerate(data_stack):
    print(f'{index} : {name}')


print('\n fungsi .pop()')
# menghapus stack menggunakan fungsi .pop()

data_stack.pop()

for index, name in enumerate(data_stack):
    print(f'{index} : {name}')

# mengecek isi stack ada atau tidak dengan menggunakan
print('Stack Kosong :')
print('Ya' if len(data_stack) == 0 else 'Tidak')

# menampulkan jumlah stack
print('Jumlah Elemen Stack : ', len(data_stack))

# menampilkan data top dengan menambah [-1] pada variabel data_stack
print(f'Data Stack Top : {data_stack[-1]}')