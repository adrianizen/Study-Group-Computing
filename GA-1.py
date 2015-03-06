from random import randint
#mencari solusi minimal yang mungkin dari antara 0..16

#fungsi sperti ini:
def f(x,y):
    fungsi= (3*x^2) +(2*y^2)-(4*x)+(y*1.0)/2
    return fungsi

#inisialisasi individu(solusi) random(populasi) beserta nilai fitnessnya
def make_pop(n):
    p=[[randint(0,1) for rand in range(8)]for jumlah in range(n)]
    return p
a=10
print a 
#penggabungan 2 individu(solusi) dan dihitung nilai fitness nya
#meloloskan kumpulan solusi bds nilai fitnessnya'
#allright
