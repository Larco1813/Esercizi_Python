with open('esercizi/rimario/parole.txt', 'r', encoding='utf-8') as file:
    righe = file.readlines()
parole = []


for riga in righe:
    parole.extend(riga.strip().split())


def controlla_rima():
    parola_utente = input("inserisci una parola: ")
    rime = []
    rima_utente = parola_utente[-3:]
    
    for parola in parole:
        if parola[-3:] == rima_utente:
            rime.append(parola)
    
    risultato = ", ".join(rime)
    
    if risultato == "":
        print("non ci sono parole che fanno rima con " + parola_utente)
    else: 
        print(risultato)

        
controlla_rima()

