# hier wordt het programma tkinter geimporteerd voor een simple GUI waarmee je een bestand kan uitkiezen
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# het bestand dat je met de GUI wordt krijg een variable en wordt gefilterd
# op enters en er wordt voor gezorgt dat de eerste regel wordt overgeslagen.
bestand = filedialog.askopenfilename()
dna = ""
with open(bestand) as inFile:
    for line in inFile:
        if not line.startswith(">"):
            dna += line.strip()

# het bestand(dat nu dna heet) wordt geprint voor gebruiksvriendlijkheid.
print(dna)

# alle AGTC uit het bestand worden getelt en ieder krijgt zijn eigen variabele.    
a = dna.count("A")
g = dna.count("G")
t = dna.count("T")
c = dna.count("C")
whole = a+g+t+c

# hier worden er een hoop print functies uitgevoerd die het aantal
# nucliotiden aangeven.
print ("Het aantal A'tjes is:", a)

print ("Het aantal G'tjes is:", g)

print ("Het aantal T'tjes is:", t)

print ("Het aantal C'tjes is:", c)
print ("Het totaal aantal nucleotiden is:", whole)

# de percentages worden berekend en geprint.
print ("Het percentage A'Tjes is:", float(100*a/whole))
print ("Het percentage G'Tjes is:", float(100*g/whole))
print ("Het percentage C'Tjes is:", float(100*c/whole))
print ("Het percentage T'Tjes is:", float(100*t/whole))
print ("Het percentage GC is:", float(100*(t+c)/whole))

