'''Module Matematika'''

def tambah(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil

def kali(*args):
    hasil = i
    for i in args:
        hasil *= i
    return hasil

def pangkat(n):
    return lambda angka:angka**n