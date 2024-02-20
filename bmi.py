import math

nimi = input("Mikä on etunimesi?: ")
print("Hei " + nimi.capitalize() + "!")

# PITUUS
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

# PAINO
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

# TAVOITE
while True:
    try:
        tavoite_str = input("Mikä on ideaalipainosi (kg)?: ").replace(",", ".")
        tavoite = float(tavoite_str)
        if tavoite <= 0:
            print("Syötä positiivinen numero.")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä numeerinen arvo.")

# ASKELEET
while True:
    try:
        askeleet_paivassa_str = input("Kuinka monta askelta haluat kävellä päivässä?: ").replace(",", ".")
        askeleet_paivassa = float(askeleet_paivassa_str)
        if askeleet_paivassa <= 0:
            print("Syötä positiivinen kokonaisluku.")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä kokonaisluku.")

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
        print("Sinulla on lievä lihavuus. ")
    elif bmi <= 34.9:
        print("Merkittävä ylipaino. ")
    elif bmi <= 39.9:
        print("Vaikea ylipaino. ")
    else:
        print("Sairaalloinen ylipaino. ")
else:
    print("Syötä oikeat tiedot!!")

def laske_askeleet(paino, tavoite):
    # Olettaen, että kalorivaje 7700 kaloria johtaa 1 kg:n (2,2 lbs) painonpudotukseen
    kalorivaje = (paino - tavoite) * 7700
    # Olettaen, että yksi askel polttaa noin 0,05 kaloria (voi vaihdella yksilöllisten tekijöiden mukaan)
    kalorit_per_askel = 0.05
    # Lasketaan tarvittavat askeleet yhteensä painonpudotustavoitteen saavuttamiseksi
    kokonais_askeleet = kalorivaje / kalorit_per_askel
    return kokonais_askeleet

kokonais_askeleet = laske_askeleet(paino, tavoite)

# Lasketaan arvioidut päivät
def laske_paivat(kokonais_askeleet, paivittaiset_askeleet):
    tarvittavat_paivat = kokonais_askeleet / paivittaiset_askeleet
    return tarvittavat_paivat

# Laske arvioidut päivät tavoitteen saavuttamiseksi
tarvittavat_paivat = laske_paivat(kokonais_askeleet, askeleet_paivassa)
print("Painonpudotustavoitteesi saavuttamiseksi sinun tulisi kävellä noin {} askelta, joka on {:.1f} päivää, kun kävelet {} askelta.".format(int(kokonais_askeleet), tarvittavat_paivat, askeleet_paivassa))