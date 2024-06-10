from queue import LifoQueue

#Deklarasi stack
stack = LifoQueue(maxsize=3)

#cara tambah data stack
stack.put('Arkan')
stack.put('Harto')
stack.put('Ali')

#display stack
print(stack.queue)

#menampilkan top elemen stack
print(f'Top/peek stack : {stack.queue[-1]}')

#menghapus stack
stack.get()
print(stack.queue)

#mengecek stack kosong atau tidak
print(stack.empty())

#
print(f'stack full atau tidak : {stack.full()}')

#menentukan jumlah elemen stack
print(f'jumlah stack : {stack.qsize()}')