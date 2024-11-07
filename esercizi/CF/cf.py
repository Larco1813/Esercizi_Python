import json

def leggi_dati_json_italiano(file_path_italiano):
    with open(file_path_italiano, 'r', encoding='utf-8') as file:
        dati = json.load(file) 
        
        
    return dati



def leggi_dati_json_straniero(file_path_straniero):
    with open(file_path_straniero, 'r', encoding='utf-8') as file:
        dati = json.load(file) 
    return dati




def cod_nome(nome):
    consonanti = ""
    vocali = ""
    cod = ""
    for lettera in nome: 
    
        if lettera.lower() not in "aeiou":  
            consonanti += lettera.upper()
        elif lettera.lower() in "aeiou": 
            vocali += lettera.upper()
    if len(consonanti) >= 4:
        cod = consonanti[0] + consonanti[2] + consonanti[3]
    else:
        cod = (consonanti + vocali)[:3].ljust(3, "X")
        
        
    return cod





def cod_cognome(cognome):
    consonanti = ""
    vocali = ""
    cod = ""
    
    for lettera in cognome: 
        if lettera.lower() not in "aeiou":  
            consonanti += lettera.upper()
        elif lettera.lower() in "aeiou": 
            vocali += lettera.upper()
    if len(consonanti) >=4:
        cod = consonanti[:3]
    else:
        cod = (consonanti + vocali)[:3].ljust(3, "X")
    
    
    return cod





def cod_data(data_input, sesso):
    mese_let = "ABCDEHLMPRST"
    mese = mese_let[int(data_input[3:5]) -1]
    giorno = str(data_input[0:2])
    
    if len(data_input.split("/")[2]) == 4:
        anno = str(data_input[8:10])
    elif len(data_input.split("/")[2]) == 2:
        anno = str(data_input[6:8])
    else:
        print("formato data non valido")
        
   
    if sesso.upper() == "F":
        giorno = str(int(giorno) + 40)
        


    return anno + mese + giorno





def cod_provenienza(nazione_utente, comune_utente):
    cod_provenienza = ""
    file_path_italiano = 'esercizi/CF/comuni.json'
    file_path_straniero = 'esercizi/CF/stati.json'
    comuni = leggi_dati_json_italiano(file_path_italiano)
    stati = leggi_dati_json_straniero(file_path_straniero)
    nazione_utente = nazione_utente.strip().lower()
    
    if nazione_utente.lower() == "italia": 
        for comune in comuni["comuni"]:
            if comune["comune"].strip().lower() == comune_utente.lower():
                if "cod_fisco" in comune:
                    cod_provenienza = comune["cod_fisco"]
                else:
                    print(f"Il comune '{comune_utente}' non ha un codice fiscale.")
                break 
    else:
        for nazione in stati["stati"]:
            if nazione["nome"].lower() == nazione_utente.lower():
                if "codice" in nazione:
                    cod_provenienza = nazione["codice"]
                else:
                    print(f"Lo Stato '{nazione_utente}' non ha un codice fiscale.")
                break

        
    return cod_provenienza





def cod_carattere_controllo(cf_parziale):
    valori_pari = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    valori_dispari = {
        '0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
       'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21,
       'K': 2, 'L': 4, 'M': 18, 'N': 20, 'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14,
       'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23
    }
    caratteri_controllo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    somma = 0
 
    
    for i, carattere in enumerate(cf_parziale):
        if (i + 1) % 2 == 0:  
            somma += valori_pari[carattere]
        else:  
            somma += valori_dispari[carattere]
    
    
    resto = somma % 26

    cod = caratteri_controllo[resto]
    
    return cod





def generaCF():
    nome = cod_nome(input("inserisci il tuo nome: "))
    cognome = cod_cognome(input("inserisci il tuo cognome: "))
    data_input = input("Inserisci la tua data di nascita (formato: gg/mm/aaaa o gg/mm/yy): ")
    sesso = input("Inserisci il tuo sesso (M o F): ")
    data = cod_data(data_input, sesso)
    nazione_utente = input("Inserisci il tuo paese natale: ")
    comune_utente = None
    
    
    if nazione_utente.lower() == "italia":
        comune_utente = input("Inserisci il comune di nascita: ")
    
    provenienza = cod_provenienza(nazione_utente, comune_utente)
    cf_parziale = cognome + nome + data + provenienza
    carattere_controllo = cod_carattere_controllo(cf_parziale)
    cf = cf_parziale + carattere_controllo
    
    
    print("Il tuo codice fiscale è: " + cf)
    
    
generaCF()    