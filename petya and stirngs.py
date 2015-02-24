kata1=raw_input("Masukkan kata1: ")
kata2=raw_input("Masukkan kata2 :")

hasil=0
if len(kata1)>=len(kata2):
    Wcompare=len(kata1)
else:
    Wcompare=len(kata2)
for i in range(0,Wcompare-1):
    if kata1[i].lower()>kata2[i].lower() or len(kata1)>len(kata2):
        hasil=1
        break
    if kata1[i].lower()< kata2[i].lower() or len(kata1)<len(kata2) :
        hasil=-1
        break
print hasil
    
