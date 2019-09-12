#Zea mays DNA
file = '/home/karsten/Documents/School stuff/Bio-informatica/FASTA/Zea mays/Zea mays-DNA.fasta'
dna = ""
with open(file) as inFile:
    for line in inFile:
        if not line.startswith(">"):
            dna += line.strip()
            

print(dna)
    
#dna = file.read()

#print (dna)
def percentage(a, g, t, c, whole):
    return 100 * float(a)/float(whole)


a = dna.count("A")
g = dna.count("G")
t = dna.count("T")
c = dna.count("C")
whole = a+g+t+c
print ("Het aantal A'tjes is:", a)

print ("Het aantal G'tjes is:", g)

print ("Het aantal T'tjes is:", t)

print ("Het aantal C'tjes is:", c)
print ("Het totaal aantal nucleotiden is:", whole)

print ("Het percentage A'Tjes is:", float(100*a/whole))
print ("Het percentage G'Tjes is:", float(100*g/whole))
print ("Het percentage C'Tjes is:", float(100*c/whole))
print ("Het percentage T'Tjes is:", float(100*t/whole))
print ("Het percentage GC is:", float(100*(t+c)/whole))
