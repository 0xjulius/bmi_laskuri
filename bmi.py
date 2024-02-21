import math

name = input("Mikä on etunimesi?: ")
print("Hei " + name.capitalize() + "!\n")

# Pituus
while True:
    try:
        height_str = input("Kuinka pitkä olet?: ").replace(",", ".")
        height = float(height_str)
        if height <= 0:
            print("Syötä positiivinen numero")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä numeerinen arvo!")
print("Pituudeksi on määritetty", height, "senttimetriä.\n")

# Paino
while True:
    try:
        weight_str = input("Kuinka painava olet?: ").replace(",", ".")
        weight = float(weight_str)
        if weight <= 0:
            print("Syötä positiivinen numero")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä numeerinen arvo!")
print("Painoksi määritettiin", weight, "kiloa.\n")

heightM = height / 100
bmi = weight / (heightM * heightM)

print("----------------------------------------\n")
print("Painoindeksisi on tällä hetkellä: {:.2f}".format(bmi))

if bmi > 0:
    if bmi <= 14.9:
        print("Olet sairaalloisen alipainoinen! \n")
    elif bmi <= 17.9:
        print("Merkittävä alipaino! \n")
    elif bmi <= 18.9:
        print("Lievä alipaino. \n")
    elif bmi <= 24.9:
        print("Onnittelut! Olet normaalipainoinen.\n")
    elif bmi <= 29.9:
        print("Sinulla on lievä lihavuus. \n")
    elif bmi <= 34.9:
        print("Merkittävä ylipaino. \n")
    elif bmi <= 39.9:
        print("Vaikea ylipaino. \n")
    else:
        print("Sairaalloinen ylipaino. \n")
else:
    print("Syötä oikeat tiedot!!\n")
print("----------------------------------------\n")

# TAVOITE
while True:
    try:
        target_str = input("Mikä on ideaalipainosi (kg)?: ").replace(",", ".")
        target = float(target_str)
        if target <= 0:
            print("Syötä positiivinen numero.")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä numeerinen arvo.")
print("Tavoitepainoksi määritettiin", target, "kiloa.")

target_weight = abs(weight - target)
calories = target_weight * 7000

if weight > target:
    print("Haluat siis laihtua {:.2f} kiloa, joka on arviolta {:.2f} kaloria!".format(target_weight, calories))
    print("Sinun täytyy siis vähentää energian saantia, tai lisätä liikuntaa {:.2f} kalorin verran.\n".format(calories))
else:
    print("Haluat nostaa painoasi {:.2f} kiloa, joten ohjelma lopetetaan.".format(target_weight))
    exit()

# ASKELEET
while True:
    try:
        steps_per_day_str = input("Kuinka monta askelta haluat kävellä päivässä?: ").replace(",", ".")
        steps_per_day = float(steps_per_day_str)
        if steps_per_day <= 0:
            print("Syötä positiivinen kokonaisluku.")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä kokonaisluku.")

print("Tavoitteeksi määritetty", steps_per_day, "askelta per päivä!\n")


def calculate_steps(weight, target):
    # Olettaen, että 7000 kaloria johtaa 1 kg:n painonpudotukseen
    calorie_deficit = (weight - target) * 7000
    # Olettaen, että yksi askel polttaa noin 0,05 kaloria (voi vaihdella yksilöllisten tekijöiden mukaan)
    calories_per_step = 0.05
    # Lasketaan tarvittavat askeleet yhteensä painonpudotustavoitteen saavuttamiseksi
    total_steps = calorie_deficit / calories_per_step
    return total_steps

total_steps = calculate_steps(weight, target)

# Lasketaan arvioidut päivät
def calculate_days(total_steps, daily_steps):
    required_days = total_steps / daily_steps
    return required_days

# Laske arvioidut päivät tavoitteen saavuttamiseksi
required_days = calculate_days(total_steps, steps_per_day)
print("Painonpudotustavoitteesi saavuttamiseksi sinun tulisi kävellä noin {} askelta, joka on {:.1f} päivää. \n({} askelta per päivä).".format(int(total_steps), required_days, int(steps_per_day)))


def calculate_time_to_burn_calories(calories_to_burn, walking_speed_kmh, weight):
    # MET = Metabolic Equivalent of Task
    met_value = 4.3
    
    # Laske poltetut kalorit tunnissa
    calories_burned_per_hour = met_value * weight
    
    # Laske kalorien polttamiseen tarvittava aika tunteina.
    time_hours = calories_to_burn / calories_burned_per_hour
    
    return time_hours

calories_to_burn = calories
walking_speed_kmh = 6.0

# Lasketaan tarvittava aika
time_hours = calculate_time_to_burn_calories(calories_to_burn, walking_speed_kmh, weight)

print("\nSinulla kestää yhteensä noin {:.0f} tuntia polttaa {:.0f} kaloria kävelemällä reippaasti {:.0f} kilometrin tuntivauhdilla!".format(time_hours, calories_to_burn, walking_speed_kmh))


# ENERGIANTARVE

while True:
    try:
        age = input("Jos haluat laskea energiantarpeesi, niin syötä ikäsi: ").replace(",", ".")
        age = float(age)
        if age <= 0:
            print("Syötä positiivinen kokonaisluku.")
        else:
            break
    except ValueError:
        print("Ole hyvä ja syötä kokonaisluku.")

print("Iäksi määritettiin", age, ".\n")

def calculate_bmr(weight, height, age):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    return bmr

def calculate_maintenance_calories(bmr, activity_factor):
    activity_factors = {
        1: 1.2,  # Sedentary
        2: 1.375,  # Lightly active
        3: 1.55,  # Moderately active
        4: 1.725,  # Very active
        5: 1.9  # Extra active
    }
    maintenance_calories = bmr * activity_factors.get(activity_factor, 1.2)
    return maintenance_calories

print("Valitse aktiivisuustasosi:")
print("1. Istumatyö (vähän tai ei lainkaan.)")
print("2. Kevyt liikunta (1-3 kertaa viikossa.)")
print("3. Kohtalainen (3-5 kertaa viikossa.)")
print("4. Erittäin aktiivinen (6-7 kertaa viikossa.)")
print("5. +7 kertaa viikossa!")
activity_factor = int(input("Syötä aktiivisuustasoasi vastaava luku:  "))

# YLLÄPITOKALORIT
bmr = calculate_bmr(weight, height, age)
maintenance_calories = calculate_maintenance_calories(bmr, activity_factor)
print("\nYlläpitokalorisi ovat: {} kaloria. Eli jos syöt alle tämän, niin suuntaat kohti tavoitettasi!".format(maintenance_calories))

defecit = 500
calories_per_step = 0.05
defecitall = maintenance_calories - defecit
defgoal = calories_to_burn / defecit

print("Esimerkiksi 500 kilokalorin energiavajeella saisit syödä päivässä yhteensä {} kaloria, ja sitä tulisi jatkaa {:.0f} päivää, jotta pääset tavoitteeseesi.".format(defecitall, defgoal))

add_all_burned = calories_per_step * steps_per_day + defecit
total_calories_burned = calories_to_burn / add_all_burned
print("Mikäli kuitenkin lisäät askelia {:.0f}, ja vähennät energiansaantia 500 kilokaloria, saavutat tavoitteesi {:.0f} päivässä! \n".format(steps_per_day, total_calories_burned))
