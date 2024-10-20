

parole = [
    "Amicizia", "Bellissimo", "Cucina", "Difficile", "Elefante", "Fantasia", "Generoso",
    "Ispirare", "Laboratorio", "Meraviglia", "Nostalgia", "Offrire", "Pensiero",
    "Qualità", "Risultato", "Sicurezza", "Tradizione", "Università", "Vegetale", 
    "Abitazione", "Crescita", "Divertente", "Esperienza", "Fratello", "Giocattolo",
    "Inseguito", "Lavoratore", "Montagna", "Notte", "Osservare", "Prendersi", 
    "Quotidiano", "Responsabile", "Scoprire", "Teatrale", "Umanità", "Volontario",
    "Amministrare", "Carattere", "Educazione", "Fattoria", "Giustizia", "Hospital", 
    "Istituto", "Maturità", "Nutriente", "Ospitale", "Pensatore", "Qualificato", 
    "Regolamento", "Appuntamento", "Sostenibile", "Programmare", "Comunicare", 
    "Sorpresa", "Riflessione", "Esplorare", "Semplicità", "Trascorrere", 
    "Navigazione", "Collaborare", "Abbigliamento", "Dedicazione", "Eccellenza", 
    "Sviluppo", "Flessibilità", "Conoscenza", "Affidabilità", "Informazione", 
    "Ambiente", "Creatività", "Valutazione", "Invenzione", "Determinazione", 
    "Ricchezza", "Intelligenza", "Autenticità", "Innovazione", "Apprezzamento", 
    "Motivazione", "Gestione", "Iniziativa", "Comportamento", "Associazione", 
    "Immaginazione", "Condivisione", "Riconoscimento", "Realtà", "Osservazione", 
    "Accoglienza", "Impegno", "Persuasione", "Rappresentazione", "Organizzazione", 
    "Evidenza", "Preoccupazione", "Utilizzazione", "Fondamentale", 
    "Conferenza", "Caratteristica", "Contemporaneo", "Autorevolezza", 
    "Consapevolezza"
]

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

