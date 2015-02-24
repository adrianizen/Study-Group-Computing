from random import randint
keys=[]
for i in range(6):
    keys.append(str(randint(0,1)))

ubah={'1':'0','0':'1'}
newind_1=[]
newind_2=[]
ind_1=raw_input("Masukkan individu 1: ")
ind_2=raw_input("Masukkan individu 2: ")

for i in range(0,len(ind_1)):
    if keys[i]=='1':
        newind_1.append(ubah[ind_1[i]])
        newind_2.append(ubah[ind_2[i]])
    else:
        newind_1.append(ind_1[i])
        newind_2.append(ind_2[i])

print keys
print "".join(newind_1)
print "".join(newind_2)
