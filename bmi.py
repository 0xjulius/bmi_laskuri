import math

nimi = input("Mikä on etunimesi?: ")
print("Hei " + nimi.capitalize() + "!")

while True:
    try:
        pituus_str = input("Kuinka pitkä olet?: ").replace(",", ".")
        pituus = float(pituus_str)
        if pituus <= 0:
            print("Syötä positiivinen numero")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä numeerinen arvo!")

while True:
    try:
        paino_str = input("Kuinka painava olet?: ").replace(",", ".")
        paino = float(paino_str)
        if paino <= 0:
            print("Syötä positiivinen numero")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä numeerinen arvo!")

pituusM = pituus / 100
bmi = paino / (pituusM * pituusM)

print("Pituutesi on", pituus, "senttimetriä.")
print("Painosi on", paino, "kiloa.")
print("Painoindeksisi on: {:.2f}".format(bmi))

if bmi > 0:
    if bmi <= 14.9:
        print("Olet sairaalloisen alipainoinen! ")
    elif bmi <= 17.9:
        print("Merkittävä alipaino! ")
    elif bmi <= 18.9:
        print("Lievä alipaino. ")
    elif bmi <= 24.9:
        print("Onnittelut! Olet normaalipainoinen.")
    elif bmi <= 29.9:
        print("Lievä lihavuus. ")
    elif bmi <= 34.9:
        print("Merkittävä ylipaino. ")
    elif bmi <= 39.9:
        print("Vaikea ylipaino. ")
    else:
        print("Sairaalloinen ylipaino. ")
else:
    print("Syötä oikeat tiedot!!")