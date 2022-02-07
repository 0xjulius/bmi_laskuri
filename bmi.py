import math
nimi = input("Mikä on etunimesi?: ")
print("Hei " + nimi.capitalize() + "!")
pituus = float(input("Kuinka pitkä olet?: "))
paino = float(input("Kuinka painava olet?: "))

s_pituus = str(pituus)
s_paino = str(paino)

pituusM = pituus / 100
pituuspow = math.pow(pituusM, 2.5)
bmi = 1.3 * paino/pituuspow

print("Pituutesi on " + s_pituus + " senttimetriä.")
print("Painosi on " + s_paino + " kiloa.")
print("Painoindeksisi on: {:.2f}".format(bmi))

if(bmi>0):
    if(bmi<=14.9):
        print("Olet sairaalloisen alipainoinen! ")
    elif(bmi<=17.9):
        print("Merkittävä alipaino! ")
    elif(bmi<=18.9):
        print("Lievä alipaino. ")
    elif(bmi <= 24.9):
        print("Onnittelut! Olet normaalipainoinen.")
    elif(bmi<=29.9):
        print("Lievä lihavuus. ")
    elif(bmi <= 34.9):
        print("Merkittävä ylipaino. ")
    elif(bmi <= 39.9):
        print("Vaikea ylipaino. ")
    else:
        print("Sairaalloinen ylipaino. ")
else:
    print("Syötä oikeat tiedot!!")