stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
           'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
           'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastrich']

def inlezen_beginstation(stations):
   while True:
       invoer = input("Vul hier het begin station in:\n")
       fout = False
       for station in stations:
           if invoer == station:
               beginstation = invoer
               return beginstation
           else:
               if invoer not in stations:
                   fout = True
       if fout == True:
           print("Deze trein komt niet in " + invoer)


def inlezen_eindstation(stations, beginstation):
   while True:
       eindstation = input("Vul hier het eind station in:\n")
       fout = False
       index = stations.index(beginstation)
       for station in stations:
           if eindstation == station:
               index1 = stations.index(eindstation)
               if index1 > index:
                   return eindstation
               else:
                   print("Deze trein rijdt niet achterstevoren!")
                   continue
           else:
               fout = True
       if fout == True:
           print('Deze Trein komt niet in ' + eindstation)


def omroepen_reis(stations, beginstation, eindstation):
   index = stations.index(beginstation)
   index1 = stations.index(eindstation)
   aantal = index1 - index
   prijs = aantal * 5
   teller = 0
   print("Het beginstation " + beginstation + " is het " + str(index + 1) + "e station in het traject.")
   print("Het eindstation " + eindstation + " is het " + str(index1 + 1) + "e station in het traject")
   print('De afstand beslaat ' + str(aantal) + ' stations(s)')
   print('De prijs van het kaartje is ' + str(prijs) + ' euro\n\n')
   print('Jij stapt in de trein in: ' + beginstation)
   for stops in stations:
       teller += 1
       if (teller > index) and (teller < index1):
           print(' - ' + stops.rstrip())
   print('Jij stapt uit in: ' + eindstation)


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)