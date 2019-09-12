product1 = float(input("geef de prijs in euro's van product 1"))
product2 = float(input("geef de prijs in euro's van product 2"))
product3 = float(input("geef de prijs in euro's van product 3"))
product4 = float(input("geef de prijs in euro's van product 4"))
product5 = float(input("geef de prijs in euro's van product 5"))

alles = (product1+product2+product3+product4+product5)

print("De prijs inclusief belasting is:")
print(round(alles*1.07, 2))
