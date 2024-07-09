class Book:
    def __init__(self, judul, penulis, tahun_terbit):
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun_terbit = tahun_terbit

    def get_judul(self):
        return self.__judul
    
    def get_penulis(self):
        return self.__penulis
    
    def get_tahun(self):
        return self.__tahun_terbit
    
    def information(self):
        return f'Judul: {self.get_judul()} \nPenulis: {self.get_penulis()} \nTahun Terbit: {self.get_tahun()}'


class Ebook:
    def __init__(self, ukuran):
        self.__ukuran = ukuran

    def get_ukuran(self):
        return self.__ukuran
    
    def info_ebook(self):
        return f'Ukuran Buku: {self.get_ukuran()} KB'


class SiKancil(Book, Ebook):
    def __init__(self, judul, penulis, tahun_terbit, ukuran):
        Book.__init__(self, judul, penulis, tahun_terbit)
        Ebook.__init__(self, ukuran)
    
    def info(self):
        return f'{self.information()} \nUkuran Dalam Ebook: {self.get_ukuran()} KB'


