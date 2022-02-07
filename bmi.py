nimi = input("Mikä on etunimesi?: ")
print("Hei " + nimi.capitalize() + "!")
pituus = float(input("Kuinka pitkä olet?: "))
paino = float(input("Kuinka painava olet?: "))

pituusM = pituus / 100
bmi = paino/(pituusM*pituusM)

print("Pituutesi on " + str(pituus) + " senttimetriä.")
print("Painosi on " + str(paino) + " kiloa.")
print("Painoindeksisi on: {:.2f}".format(bmi))

if(bmi>0):
    if(bmi<=16):
        print("Olet sairaalloisen alipainoinen. ")
    elif(bmi<=18.5):
        print("Olet alipainoinen. ")
    elif(bmi<=25):
        print("Onnittelut! Olet normaalipainoinen.")
    elif(bmi<=30):
        print("Lievä lihavuus. ")
    else:
        print("Merkittävä lihavuus. ")
else:
    print("Syötä oikeat tiedot!!")