afstandKM = int(input('Hoeveel Kilometer\'s ga je reizen?')) # input voor de hoeveelheid kilometer
weekendrit_invoer = input("is het nu weekend?") #input voor of het weekend is
leeftijd = int(input("Hoe oud ben je?")) #input voor de leeftijd


if weekendrit_invoer == 'ja': # als de input ja is dan is het weekend
    weekend = True #maak de boolean weekend True
else: # maak in elk ander geval 
    weekend = False # maak de boolean weekend False

def standaardprijs(afstandKM): # De  functie standaardprijs\
    if afstandKM <= 0:
        tarief = 0
    elif afstandKM < 50:
        tarief = afstandKM * 0.80
    else:
        tarief = 15 + afstandKM * 0.60

    return tarief

def ritprijs(afstandKM, weekend, leeftijd):
    tarief = standaardprijs(afstandKM)
    if (leeftijd <12) or (leeftijd > 64):
        if weekend == True:
            tarief = tarief * 0.65
            return round(tarief,2)
        else:
            tarief  = tarief * 0.70
        return round(tarief, 2)
    else:
        if weekend == True:
            tarief = tarief * 0.60
            return round(tarief, 2)
        else:
            return round(tarief, 2)

print("Deze rit gaat €" + str(ritprijs(afstandKM, weekend, leeftijd)) + " kosten.")

def bsprijs(afstandKM, weekend, leeftijd):
    tarief = standaardprijs(afstandKM)
    if (leeftijd == 69):
        print("kek je leeftijd")
    else:
        print("je moet die kek leeftijd hebben man ")
