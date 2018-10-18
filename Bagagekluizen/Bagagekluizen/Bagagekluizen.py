
import os
import time
def openKluis(laatstekeer):
    if laatstekeer == True:
        print('de kluis wordt voor de laatste keer geopend hierna worden de gegevens verwijderd') 
    else:
        print('de kluis wordt geopend')
    time.sleep(3)
def toon_aantal_kluizen_vrij(): 
    file = open('kluizen.txt')   # open de file
    lengte = file.readlines()    #lees iedere lijn
    file.close()               #sluit het bestand
    return 12 - len(lengte)     #bereken de beschikbare kluisjes door de 12 kluisjes te delen door het aantal regels omdat een regel gelijk is aan een kluisje

def nieuwe_kluis():   # functie om een nieuwe kluis toe te voegen aan het systeem

    while True:             # loop voor wachtwoord
        wachtwoord = input('voer hier uw nieuwe wachtwoord in: \n')       # vraagt om een wachtwoord aan te maken  
        if len(wachtwoord) <6: #het aantal tekens van het wachtwoord moet 6 cijfers zijn
            print('het wachtwoord moet minimaal 6 tekens zijn') #print deze string als het aantal tekens niet gelijk is aan 6
            continue
        if wachtwoord == 'quit': #sluit het programma als deze wordt ingevoerd
            return
        password2 = input('bevestig uw wachtwoord: \n')                 # 2de keer het wachtwoord invoeren om beter te onthouden en spelfouten uit te sluiten  
        if wachtwoord == password2:                # checked of de wachtwoorden overeen komen
            break                                                       # stopt de loop als het wachtwoord voldoet aan de eisen
        else:                                                           
            print('wachtwoord komt niet overeen, \nof voer "quit" in om terug te gaan naar het hoofd menu')     # geeft feedback aan de user over het niet voldoen aan de eisen
    safe_number_list = []    # maak een lijst aan waar de gegevens van de nieuwe kluis opgeslagen kunnen zijn.   
    file = open('kluizen.txt', 'r+')    #open een bestand 
    inhoud = file.readlines()   #lees iedere lijn
   
    for item in inhoud:     # loop door ieder woord in de lijn die we net hebben ingelezen    
        temp_list = []      #maak een tijdelijke list aan die nodig is omdat we de gegevens die in de definitieve lijst komen eerst tijdelijk moeten opslaan.    
        temp_list =  item.split(';') #split het woord op de ; aangezien de string in de file twee losse woorden moeten worden.
        safe_number_list.append(int(temp_list[0]))     #neem het eerste deel van de string (het kluisnummer) mee en voeg dit toe aan de definitieve lijst.
    
    for i in range(1, 13):      # loop door 1 - 12 dit staat gelijk aan het maximaal aantal kluizen dus je loopt eigenlijk door alle kluisnummers
        if i not in safe_number_list:   # als een van de nummers niet gelijk zijn aan het kluisnummer dat voorkomt in de definitieve lijst als dit gebeurd is natuurlijk uitgesloten dat dit kluisje al in gebruik is
            line = str(i) + ';' + wachtwoord + '\n' # maak een geheel van het nieuwe kluisnummer + het wachtwoord
            file.writelines(line)    # schijf de data over het nieuwe kluisje naar de lijst              
            print('kluis nummer', i, 'is gereserveerd') # print dat het reserveren van dit kluisje is gelukt.                               
            break           #breek de loop af omdat deze niet meer nodig is.                            
        elif i == 12:                      #als alle kluisjes bezet zijn dan heb je pech :)             
            print('alle kluizen zijn bezet probeer het later nog een keer') #print deze                                                    
    file.close()        #sluit het bestand        
    del line #delete de variabele aangezien deze niet meer nodig is voor de rest van de code
    del inhoud      #delete de variabele aangezien deze niet meer nodig is voor de rest van de code       
    return                      
def kluis_openen():             #een functie die een kluisje opent als deze persoon een kluisje heeft gereserveerd
    kluizen_gegevens = {}       # een dictonary om de gegevens van de kluis in op te slaan
    file = open('kluizen.txt')  #open het bestand
    inhoud = file.readlines()	# lees elke lijn
    for entry in inhoud:        #loop door elk woord in het bestand    
        temp_list = []			# maak een tijdelijke lijst aan
        temp_list =  entry.split(';')	#filter ; uit het woord in het bestand
        kluizen_gegevens[int(temp_list[0])] = temp_list[1].strip() #het eerste woord (het kluisnummer) uit de tijdelijke lijst (het kluisnummer) gelijkmaken aan het wachtwoord (zonder \n) van de definitieve lijst
    file.close() # sluit het bestand
    while True:                     # oneindige loop 
        kluisnummer = input('wat is uw huidige kluis nummer?\n') # input van de gebruiker
        if kluisnummer == 'quit': #sluit de loop als gebruiker deze string invoert
            break
        try:
            if int(kluisnummer) >= 1 and int(kluisnummer) < 12: # check of de gebruiker wel een geldige invoer geeft die gelijk is aan een kluisnummer
                wachtwoord = input('wat is het bijbehorende wachtwoord?\n') #vraagt de gebruiker om een wachtwoord
                if int(kluisnummer) in kluizen_gegevens and kluizen_gegevens[int(kluisnummer)] == wachtwoord: #checkt of het kluisnummer voorkoomt in de dictonary kluizen_gegevens en check of die waarde gelijk is aan het ingevoerde wachtwoord
                    openKluis(False) #maak kluis open
                    break
                else: #maak geen kluis open en print een bericht
                    print('het opgegeven wachtwoord en kluisnummer komen niet overeen of bestaan niet.\n Probeer het nog een keer of typ "quit" om naar het hoofdmenu terug te keren')
                    continue
            else:
                print('voer een geldig kluisnummer in of typ quit om terug te gaan naar het hoofdmenu')
        except ValueError:
            print('voer een geldig kluisnummer in of typ quit om terug te gaan naar het hoofdmenu')
            continue
    del kluizen_gegevens
    del inhoud                  
    return
def kluis_teruggeven():         
    kluizen_gegevens = {} # een dictonary aanmaken 
    file = open('kluizen.txt') # maak een bestand aan die kluizen.txt
    inhoud = file.readlines() # lees alle inhoud van het bestand uit
    for entry in inhoud: # lees ieder woord uit het bestand
        temp_list = [] # maak een tijdelijke lijst
        temp_list =  entry.split(';') #split het woord op de ; zodat er twee losse strings ontstaan
        kluizen_gegevens[int(temp_list[0])] = temp_list[1].strip() #maak de kluisnummmer van de definitieve lijst  gelijk aan de gesplite  tijdelijke lijst
	file.close()
    while True:
        kluisnummer = input('wat is uw huidige kluis nummer?\n') # vraag om het kluisnummer van de gebruiker
        if kluisnummer == 'quit': # sluit  de loop
            break
        try:
            if int(kluisnummer) >= 1 and int(kluisnummer) < 12:
                wachtwoord = input('wat is het bijbehorende wachtwoord?\n')
                if int(kluisnummer) in kluizen_gegevens and kluizen_gegevens[int(kluisnummer)] == wachtwoord:
                    del kluizen_gegevens[int(kluisnummer)]
                    file = open('kluizen.txt', 'w+')
                    for key in kluizen_gegevens:
                        line = str(key) + ';' + str(kluizen_gegevens[key] + '\n')
                        file.writelines(line)
                    openKluis(True)
                    file.close()
                    break
                else:
                    print('het opgegeven wachtwoord en kluisnummer komen niet overeen of bestaan niet.\n Probeer het nog een keer of typ "quit" om naar het hoofdmenu terug te keren')
                    continue
            else:
                print('voer een geldig kluisnummer in of typ quit om terug te gaan naar het hoofdmenu')
        except ValueError:
           print('voer een geldig kluisnummer in of typ quit om terug te gaan naar het hoofdmenu')
           continue
    return
while True:                     
    print(' 1: Ik wil weten hoeveel kluizen nog vrij zijn \n 2: Ik wil een nieuwe kluis \n 3: Ik wil even iets uit mijn kluis halen\n 4: Ik geef mijn kluis terug\n 5: Ik wil stoppen') # melding met navigatie door het systeem
    while True:                
        try:                    
            actie = int(input('Wat wilt u doen? \n'))  
        except ValueError:      
            print('voer een geldige optie in') 

            continue            
        else:                   
            if actie in [1, 2, 3, 4, 5]:   
                os.system('cls' if os.name == 'nt' else 'clear')
                break                       
            else:                          
                print('voer een geldige optie in')      
                continue                   

    if actie == 1:              

        print('Er zijn nog' , toon_aantal_kluizen_vrij(), 'kluizen vrij')   
        time.sleep(4)           

    elif actie == 2:           
       
        nieuwe_kluis()          

    elif actie == 3:            

        kluis_openen()          

    elif actie == 4:           

        kluis_teruggeven()      

    else:                       
        print('tot ziens')
        break                   
    os.system('cls' if os.name == 'nt' else 'clear')    

