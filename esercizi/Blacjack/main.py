import random
import time

semi = ['♥', '♦', '♣', '♠']
numeri = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
valori = ["1", '2', '3', '4', '5', '6', '7', '8', '9', "10", "10", "10", "10"]
valori_mazzo = [(valore, seme) for seme in semi for valore in valori]
mazzo = [(numero, seme) for seme in semi for numero in numeri]

giocatore = {
    "split": False,
    "double": False,
    "double_split": False,
    "side_bet": False,
    "assicurazione": False,
    "blackjack": False,
    "blackjack_split": False,
    "sballato": False,
    "sballato_split": False,
    "conto": 30,
    "puntata": 0,
    "puntata_side_bet": 0,
    "puntata_assicurazione": 0,
    "carte": [],
    "carte_split": [],
    "valore": 0,
    "valore_split": 0,
    "puntata_totale": 0
    
}

banco = {
    "carte": [],
    "valore": 0,
    "vincita": 0,
    "blackjack": False
}
def ripristina_valori_giocatore():
    giocatore["split"] = False
    giocatore["double"] = False
    giocatore["side_bet"] = False
    giocatore["assicurazione"] = False
    giocatore["blackjack"] = False
    giocatore["sballato"] = False
    giocatore["puntata"] = 0
    giocatore["puntata_side_bet"] = 0
    giocatore["puntata_assicurazione"] = 0
    giocatore["carte"] = []
    giocatore["valore"] = 0
    giocatore["carte_split"] = []
    giocatore["valore_split"] = 0
    giocatore["blackjack_split"] = False
    giocatore["sballato_split"] = False
    giocatore["double_split"] = False
    giocatore["puntata_totale"] = 0
    
    
def ripristina_valori_computer():
    banco["carte"] = []
    banco["valore"] = 0
    banco["vincita"] = 0
    banco["blackjack"] = False


def ricarica_conto():
    conto = giocatore["conto"]
    print(f"conto: {conto}€")
    ricarica = int(input("Quanto vuoi ricaricare? "))
    conto += ricarica
    giocatore["conto"] = conto
    print(f"conto: {conto}€")
    return conto


def puntata():
    print(f"\nconto: {giocatore["conto"]:.1f}€||puntata minima: 0,5€")
    giocatore["puntata"] = float(input("Quanto vuoi puntare? "))
    
    
    if giocatore["conto"] < giocatore["puntata"] and not giocatore["conto"] < 0.5:
        print("Non hai abbastanza soldi")
        return puntata()
    elif giocatore["puntata"] < 0.5:
        print("Puntata minima 0,5€")    
        return puntata()
    elif giocatore["conto"] <0.5:
        print("Non hai abbastanza soldi")
        ricarica_conto()
    else:
        giocatore["puntata_totale"] += giocatore["puntata"]
        giocatore["conto"] -= giocatore["puntata"]
        
    
    print(f"conto: {giocatore["conto"]} puntata: {giocatore['puntata_totale']:.1f}€")
    
    
    
    return 

def side_bet():
    conto = giocatore["conto"]
    side_bet = input("Vuoi fare un side bet? (s/n): ")
    while side_bet.lower() == "s":
        bet_scelta = input("Scegli la side bet:\n1. 21+3\n2. Coppia Perfetta\n3. Bust it \n")
        giocatore["puntata_side_bet"] = float(input("Inserisci la tua puntata: "))
        puntata_side_bet = giocatore["puntata_side_bet"]
        if bet_scelta == "1":
            print("Hai scelto 21+3")
            giocatore["conto"] -= puntata_side_bet
            print(f"Conto: {conto}€")
        if bet_scelta == "2":
            print("Hai scelto Coppia Perfetta")
            giocatore["conto"] -= puntata_side_bet
            print(f"Conto: {conto}€")
        if bet_scelta == "3":
            print("Hai scelto Bust it")
            giocatore["conto"] -= puntata_side_bet
            print(f"Conto: {conto}€")
        side_bet = input("Vuoi fare un'altra side bet? (s/n): ")
    return


def calcola_valore_mano(carte):
    valore_totale = 0
    assi = 0
    for carta in carte:
        valore = int(valori_mazzo[mazzo.index(carta)][0])
        valore_totale += valore
        if carta[0] == "A":
            assi += 1
            valore_totale += 10
    
    while valore_totale > 21 and assi:
        valore_totale -= 10
        assi -= 1

    return valore_totale



def prima_mano():
    for i in range(2):
        indice_giocatore = random.randint(0, len(mazzo) - 1)
        indice_banco = random.randint(0, len(mazzo) - 1)
        giocatore["carte"].append(mazzo[indice_giocatore])
        banco["carte"].append(mazzo[indice_banco])
        
        giocatore["valore"] = calcola_valore_mano(giocatore["carte"])
        banco["valore"] = calcola_valore_mano(banco["carte"])    

        
        
        indice = 0
        
    print(f"\nLe tue carte sono: {giocatore['carte'][0][0]}{giocatore['carte'][0][1]} e {giocatore['carte'][1][0]}{giocatore['carte'][1][1]} ---- valore: {giocatore["valore"]}")
    print(f"Le carte del banco sono: {banco['carte'][0][0]}{banco['carte'][0][1]} e X")
   
    
    if giocatore["valore"] == 21:
        giocatore["blackjack"] = True
    if banco["valore"] == 21:
        banco["blackjack"] = True
        
       
        
        
    return 

    

def chiedi_split():
    if giocatore["conto"] >= giocatore["puntata"]:
        giocatore["split"] = True if input("Vuoi fare un split? (s/n): ") == "s" else False
        
    
    if giocatore["split"]:
        giocatore['carte_split'].append(giocatore['carte'][1])
        giocatore["carte"].remove(giocatore["carte"][1])
        indice_giocatore = random.randint(0, len(mazzo) - 1)
        giocatore["carte"].append(mazzo[indice_giocatore])
        giocatore["valore"] = calcola_valore_mano(giocatore["carte"])
        giocatore["puntata_totale"] += giocatore["puntata"]
        giocatore["conto"] -= giocatore["puntata"]
        print(f"Conto: {giocatore['conto']}€||Puntata: {giocatore['puntata_totale']}€")
        print(f"Le tue carte sono: {giocatore['carte'][0][0]}{giocatore['carte'][0][1]} e {giocatore['carte'][1][0]}{giocatore['carte'][1][1]} ---- valore: {giocatore["valore"]}")
        chiedi_carta()
        
    else:
        chiedi_carta()

def chiedi_carta_split():
    
    indice_giocatore = random.randint(0, len(mazzo) - 1)
    giocatore["carte_split"].append(mazzo[indice_giocatore])
    giocatore["valore_split"] = calcola_valore_mano(giocatore["carte_split"])
    print(f"Le tue carte sono: {giocatore['carte_split']} ---- valore: {giocatore["valore_split"]}")
    carta = input("Vuoi pescare una carta? (s/n):")
    while carta.lower() == "s":
        indice_giocatore = random.randint(0, len(mazzo) - 1)
        giocatore["carte_split"].append(mazzo[indice_giocatore])
        giocatore["valore_split"] = calcola_valore_mano(giocatore["carte_split"])
        print(f"Le tue carte sono: {giocatore['carte_split']} ---- valore: {giocatore["valore_split"]}")
        
        if giocatore["valore_split"] > 21:
            print("BUST")
            giocatore["sballato_split"] = True
            break
        elif giocatore["valore_split"] == 21:
            print("Hai fatto 21")
            giocatore["blackjack_split"] = True
            break
        
        
        carta = input("Vuoi pescare una carta? (s/n):")
    computer_pesca_carta()
    return

def chiedi_assicurazione():
    vincita = 0
    giocatore["assicurazione"] = True if input("Vuoi fare una assicurazione? (s/n): ") == "s" else False
    
    if giocatore["assicurazione"]:
        giocatore["puntata_assicurazione"] = giocatore["puntata"] / 2
        giocatore["conto"] -= giocatore["puntata_assicurazione"]
        print(f"Conto: {giocatore['conto']}€||Puntata assicurazione: {giocatore['puntata_assicurazione']}€")
        
        if banco["blackjack"] and not giocatore["blackjack"]:
            vincita = giocatore["puntata_assicurazione"] * 2
            giocatore["conto"] += vincita
            print(f"Il banco ha fatto Blackjack, hai vinto: {vincita}€")
            
        elif banco["blackjack"] and giocatore["blackjack"]:
            vincita = giocatore["puntata_assicurazione"] * 2 + giocatore["puntata"]
            giocatore["conto"] += vincita
            print(f"Il banco ha fatto Blackjack, hai vinto: {vincita}€")
            
        elif giocatore["blackjack"] and not banco["blackjack"]:
            print(f"Il banco non ha un Blackjack, -{giocatore['assicurazione']}€")
            vincita = giocatore["puntata"] * 2
            giocatore["conto"] += vincita - giocatore["puntata_assicurazione"]
            print(f"Hai fatto Blackjack, hai vinto: {vincita}")
        else:
            print("Il banco non ha Blackjack")
            
            
    else:
        print("Non hai fatto un'assicurazione")
        giocatore["assicurazione"] = False
        
        
    assicurato = giocatore["assicurazione"]
    return assicurato

def chiedi_double():
    if giocatore["double"] and giocatore["split"]:
        indice_giocatore = random.randint(0, len(mazzo) - 1)
        giocatore["puntata_totale"] += giocatore["puntata"] 
        giocatore["conto"] -= giocatore["puntata"] 
        giocatore["carte"].append(mazzo[indice_giocatore])
        giocatore["valore"] = calcola_valore_mano(giocatore["carte"])
        print(f"Conto: {giocatore['conto']}€||Puntata: {giocatore['puntata']}€")
        print(f"Le tue carte sono: {giocatore['carte']} ---- valore: {giocatore["valore"]}")
        
        if giocatore["valore"] > 21:
            print("BUST")
            giocatore["sballato"] = True
            
        elif giocatore["valore"] == 21:
            print("Hai fatto 21")
            giocatore["puntata"] += giocatore["puntata"] * 2
            
        indice_giocatore = random.randint(0, len(mazzo) - 1)
        giocatore["carte_split"].append(mazzo[indice_giocatore])
        giocatore["valore_split"] = calcola_valore_mano(giocatore["carte_split"])
        print(f"Le tue carte sono: {giocatore['carte']} ---- valore: {giocatore["valore"]}")
        
        if giocatore["conto"] >= giocatore["puntata"]:
            giocatore["double_split"] = True if input("Vuoi fare un split? (s/n): ") == "s" else False
           
        
        if giocatore["double_split"]:
            giocatore["conto"] -= giocatore["puntata"] 
            print(f"\nConto: {giocatore['conto']}€||Puntata: {giocatore['puntata_totale']}€")
            indice_giocatore = random.randint(0, len(mazzo) - 1)
            giocatore["carte_split"].append(mazzo[indice_giocatore])
            giocatore["valore_split"] = calcola_valore_mano(giocatore["carte_split"])
            print(f"Le tue carte sono: {giocatore['carte_split']} ---- valore: {giocatore["valore_split"]}")
            
            if giocatore["valore_split"] > 21:
                print("BUST")
                giocatore["sballato_split"] = True
                computer_pesca_carta()
            elif giocatore["valore_split"] == 21:
                print("Hai fatto 21")
                computer_pesca_carta()
            else:
                computer_pesca_carta()           
    elif giocatore["double"]:
        giocatore["puntata_totale"] += giocatore["puntata"] 
        giocatore["conto"] -= giocatore["puntata"] 
        print(f"Conto: {giocatore['conto']}€||Puntata: {giocatore['puntata_totale']}€")
        indice_giocatore = random.randint(0, len(mazzo) - 1)
        giocatore["carte"].append(mazzo[indice_giocatore])
        giocatore["valore"] = calcola_valore_mano(giocatore["carte"])
        print(f"Le tue carte sono: {giocatore['carte']} ---- valore: {giocatore["valore"]}")
        
        if giocatore["valore"] > 21:
            print("BUST")
            giocatore["sballato"] = True
            
        elif giocatore["valore"] == 21:
            print("Hai fatto 21")
            computer_pesca_carta()
        else:
            computer_pesca_carta()    
    elif giocatore["double_split"]:
        giocatore["puntata_totale"] += giocatore["puntata"]
        giocatore["conto"] -= giocatore["puntata"]
        print(f"Conto: {giocatore['conto']}€||Puntata: {giocatore['puntata_totale']}€")
        indice_giocatore = random.randint(0, len(mazzo) - 1)
        giocatore["carte"].append(mazzo[indice_giocatore])
        giocatore["valore"] = calcola_valore_mano(giocatore["carte"])
        time.sleep(1)
        print(f"Le tue carte sono: {giocatore['carte']} ---- valore: {giocatore["valore"]}")

        if giocatore["valore"] > 21:
            print("BUST")
            giocatore["sballato"] = True
            computer_pesca_carta()
        elif giocatore["valore"] == 21:
            print("Hai fatto 21")
            computer_pesca_carta()
        else:
            computer_pesca_carta()
    else:
        chiedi_carta()

def chiedi_carta():
    if giocatore["conto"] > giocatore["puntata"]:
        giocatore["double"] = True if input("Vuoi fare un double? (s/n): ") == "s" else False
    
    if not giocatore["double"]:
        if giocatore["valore"] < 21:
            carta = input("Vuoi pescare una carta? (s/n):")
            while carta.lower() == "s":
                indice_giocatore = random.randint(0, len(mazzo) - 1)
                giocatore["carte"].append(mazzo[indice_giocatore])
                giocatore["valore"] = calcola_valore_mano(giocatore["carte"])
                time.sleep(1)
                print(f"Le tue carte sono: {giocatore['carte']} ---- valore: {giocatore["valore"]}")
                time.sleep(0.5)
                if not giocatore["split"]:  
                    if giocatore["valore"] > 21:
                        print("BUST")
                        giocatore["sballato"] = True
                        break
                    elif giocatore["valore"] == 21:
                        print("Hai fatto 21")
                        computer_pesca_carta()
                        break
                else: 
                    if giocatore["valore"] > 21:
                        print("BUST")
                        giocatore["sballato"] = True
                        chiedi_carta_split()
                        break
                    elif giocatore["valore"] == 21:
                        print("Hai fatto 21")
                        chiedi_carta_split()
                        break
                carta = input("Vuoi pescare un'altra carta? ciaone (s/n):")
            if carta.lower() != "s":
                if giocatore["split"]:
                    chiedi_carta_split()
                else:
                    computer_pesca_carta()
        elif giocatore["valore"] == 21 and giocatore["split"]:
            chiedi_carta_split()
        elif giocatore["valore"] == 21 and not giocatore["split"]:
            computer_pesca_carta()
    else:
        chiedi_double()
        
    return
        
        
def computer_pesca_carta():
    time.sleep(0.5)
    print(f"Le carte del banco sono: {banco['carte']} ---- valore: {banco["valore"]}")
    while banco["valore"] < 17:
        indice_banco = random.randint(0, len(mazzo) - 1)
        banco["carte"].append(mazzo[indice_banco])
        banco["valore"] = calcola_valore_mano(banco["carte"])
        time.sleep(0.5)
        
        print(f"il banco ha pescato: {banco['carte'][-1][0]}{banco['carte'][-1][1]}")
        
        time.sleep(1)
        
        print(f"Le carte del banco sono: \n{banco['carte']} ---- valore: {banco["valore"]}")
        
    
    controlla_carte_banco()
    
        
    return


def controlla_carte_banco():
    
    
    if banco["valore"] <= 21:
        if banco["valore"] < 17:
            computer_pesca_carta()
        elif banco["valore"] >=17:
            if banco["valore"] > giocatore["valore"]:
                print("Il banco ha vinto")
                print(f"Hai perso: {giocatore["puntata_totale"]}€")
                return
            elif banco["valore"] < giocatore["valore"]:
                vincita = giocatore["puntata_totale"] * 2
                giocatore["conto"] += vincita
                print(f"Hai vinto: {vincita}€")
                return
            elif banco["valore"] == giocatore["valore"]:
                vincita = giocatore["puntata_totale"]
                giocatore["conto"] += vincita
                print(f"PUSH, hai vinto: {vincita}€")
                return
    else:
        print("Il banco ha SBALLATO")
        vincita = giocatore["puntata_totale"] * 2
        giocatore["conto"] += vincita
        print(f"Hai vinto: {vincita}€")        
        return

def gestisci_blackjack():
    time.sleep(0.5)
    if banco["blackjack"] and not giocatore["blackjack"]:
        print(f"Le carte del banco sono: {banco["carte"]}")
        print(f"Il banco ha fatto Blackjack, hai perso: {giocatore['puntata_totale']}€")
    elif giocatore["blackjack"] and not banco["blackjack"]:
        vincita = giocatore["puntata"] * 2 + (giocatore["puntata"] / 2)
        giocatore["conto"] +=  giocatore["puntata"] * 2 + (giocatore["puntata"] / 2)
        print(f"Le carte del banco sono: {banco["carte"]}")
        print(f"BLACKJACK, hai vinto: {vincita}€")
    elif giocatore["blackjack"] and banco["blackjack"]:
        giocatore["conto"] += giocatore["puntata"]
        print(f"Le carte del banco sono: {banco["carte"]}")
        print(f"PUSH, hai vinto: {giocatore['puntata']}€")

def gioco():
    


    si_gioca = True
    assicurato = False
    while si_gioca:
        puntata()
        #side_bet()
        prima_mano()
        if banco["carte"][0][0] == "A":
            assicurato = chiedi_assicurazione()
            if not assicurato and banco["blackjack"] or giocatore["blackjack"]:
                gestisci_blackjack()
                print("Hai cewvhjwebkj la partita")
                ripristina_valori_giocatore()
                ripristina_valori_computer()
                gioco()
            elif giocatore["carte"][0][0] == giocatore["carte"][1][0]:
                print("entra qua")
                chiedi_split() 
            if not assicurato and not banco["blackjack"] and not giocatore["blackjack"]:
                chiedi_carta()  
            if not assicurato and banco["blackjack"] or giocatore["blackjack"]:
                    gestisci_blackjack()         
        elif giocatore["blackjack"]:
            gestisci_blackjack()
        elif giocatore["carte"][0][0] == giocatore["carte"][1][0]:
            chiedi_split()
        elif banco["blackjack"]:
            chiedi_carta()            
        else: 
            chiedi_carta()
            
        
        
        ripristina_valori_giocatore()
        ripristina_valori_computer()
        if giocatore["conto"] < 0.5:
            ricarica = input("Vuoi ricaricare il conto? (s/n): ")
            if ricarica.lower() == "s":
                ricarica_conto()
            else:
                print("Arrivederci")
                break
        
gioco()