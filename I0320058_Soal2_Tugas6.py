#Buatlah program menghitung nilai rata-rata dari nilai yang diinput oleh user dengan
#menggunakan perintah perulangan for atau while

def rt(y):
    panjang=len(y)
    jumlah=sum(y)
    ratarata=panjang/jumlah
    return ratarata

x=[]
n= int(input('Masukkan jumlah data yang akan dimasukkan : '))

for i in range(1, n+1):
    a=int(input('Masukkan Angka ke-%d : '%i))
    x.append(a)

print('Rata-ratanya adalah', round(rt(x), 3))