from random import randint

a=[]
b=[]
for angka in range(6):
    a.append(randint(0,1))
    b.append(randint(0,1))

print "Parent 1 :"+str(a)
print "Parent 2 :"+str(b)
potong = randint(0,5)
for i in range(potong,6):
    a[i],b[i]=b[i],a[i]
print a
print b


