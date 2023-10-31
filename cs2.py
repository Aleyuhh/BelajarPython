def input_alas_dan_tinggi():
    alas = float(input('test code nomor: '))
    atas = float(input('masukan nomr: '))

    return alas, atas

def hitung_luas_(alas,atas):
    return 0.5 * alas * atas

print(hitung_luas_(7,12))