import os
os.system('cls')

'''
Studi kasus masalah pada parameter
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Ucup")
fungsi(True)
'''

# penggunaan type hints

def sepuluh_pangkat(argument:int) -> int: # Agar ada dokumentasi ketika di hover ada int nya
    '''Fungsi dengan hints'''
    output = 10**argument
    return output

hasil = sepuluh_pangkat(2.5)
print(hasil)

import string

def halo(argument:string):
    print(argument)

halo("Halo")