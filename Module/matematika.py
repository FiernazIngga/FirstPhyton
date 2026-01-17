# module matematika

def tambah(*args:int) -> int:
    hasil = 0
    for data in args:
        hasil += data
    return hasil

def kali(*args:int) -> int:
    hasil = 1
    for data in args:
        hasil *= data
    return hasil

def pangkat(n:int) -> int:
    return lambda angka:angka**n