kata=raw_input("Masukkan kata: ")
lowerinput=kata.lower()

newkata=[]
vowels=['a','e','i','o','u']
for i in range(0,len(kata)):
    if not(lowerinput[i] in vowels):
        newkata.append(".")
        newkata.append(lowerinput[i])

print "".join(newkata)

// "."join([huruf for huruf in a if huruf not in vowel])*)
