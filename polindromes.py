revsdict={'A':'A','E':'3','H':'H','I':'I','J':'L','L':'J','M':'M','O':'O','S':'2','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'5','1':'1','2':'S','3':'E','5':'S','8':'8'}

kata=raw_input("Masukkan kata : ");
upkata=kata.upper()
panjang=len(kata)
last=panjang

mirror=True
poly=True

for i in range(0,panjang-1):
    if(upkata[i]==upkata[last-1]):
        if(not((upkata[i] in revsdict) and (upkata[last-1] in revsdict))):
            mirror=False
    elif(upkata[i]!=upkata[last-1]):
            poly=False
            if(upkata[i]!=revsdict[upkata[last-1]]):
                mirror=False
                break
    last=last-1

if(poly):
    if(mirror):conclude="Mirrored Polindrom"
    else:conclude="Regular Polindrom"
else:
    if(mirror):conclude="Mirrored String"
    else:conclude="not a Polindrom"

print upkata +"is "+conclude
