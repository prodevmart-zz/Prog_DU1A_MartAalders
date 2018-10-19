def standaardprijs(afstandKM):

# 0.80 cent per treinrit

	if afstandKM > 50:
		prijs = 15 + 0.60 * afstandKM
		return prijs
	elif afstandKM < 0:
		prijs = 0
		return prijs

	else:
		prijs = 0.80 * afstandKM
		return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
	
	prijs = standaardprijs(afstandKM)
	if leeftijd < 12 or leeftijd > 65:
	#30 Korting
	#35 procent korting vanwege weekend
		prijs / 100 * 65
		return prijs
	elif leeftijd < 12 or leeftijd > 65 and weekendrit == False:
		return (prijs / 100) * 70
	elif leeftijd < 12 or leeftijd > 65 and weekendrit == True:
		return (prijs / 100) * 65
	elif weekendrit == True:
		prijs = ((prijs  / 100 * 40) / 100) * 60
		return prijs
	else:
		prijs = prijs  / 100 * 40
		return prijs


print(ritprijs(66, True, 120))

