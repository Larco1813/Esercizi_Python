registro_pressione = [
    [            
        {"orario": "mattina", "sistolica": 0, "diastolica": 0},
        {"orario": "pomeriggio", "sistolica": 0, "diastolica": 0},
        {"orario": "sera", "sistolica": 0, "diastolica": 0}
    ], 
    [
        {"orario": "mattina", "sistolica": 0, "diastolica": 0},
        {"orario": "pomeriggio", "sistolica": 0, "diastolica": 0},
        {"orario": "sera", "sistolica": 0, "diastolica": 0}            
    ],
    [
        {"orario": "mattina", "sistolica": 0, "diastolica": 0},
        {"orario": "pomeriggio", "sistolica": 0, "diastolica": 0},
        {"orario": "sera", "sistolica": 0, "diastolica": 0}
    ],
]
medie = []

def ritorna_media():
    giorno_media = int(input("\n\nSeleziona il giorno (1, 2 o 3) per il quale desideri calcolare la media: "))
    
        
    while True:
        if 1 <= giorno_media <= 3:
            giorno_selezionato = int(giorno_media - 1)
            print(f"\nDurante il giorno {giorno_media}, la media sistolica è: {medie[giorno_selezionato]["media sistolica"]}, mentre quella diastolica è: {medie[giorno_selezionato]["media diastolica"]}")
            break
        else:
            print("Giorno non valido. Seleziona un valore tra 1 e 3.")

def pressione_alta(misurazione, idx, giorno):
    for misurazione in giorno:
        if misurazione["sistolica"] > 120:
            print(f"Attenzione! La **sistolica** del giorno {idx + 1} durante {misurazione['orario']} è alta: {misurazione['sistolica']}")
        elif misurazione["sistolica"]  < 90:
            print(f"Attenzione! La **sistolica** del giorno {idx + 1} durante {misurazione['orario']} è bassa: {misurazione['sistolica']}")
        if misurazione["diastolica"] > 80:
            print(f"Attenzione! La **diastolica** del giorno {idx + 1} durante {misurazione['orario']} è alta: {misurazione['diastolica']}")
        elif misurazione["diastolica"] < 60:
            print(f"Attenzione! La **diastolica** del giorno {idx + 1} durante {misurazione['orario']} è bassa: {misurazione['diastolica']}")
        
def richiedi_misurazione(idx , giorno):
    somma_sistolica = 0  
    somma_diastolica = 0
    print(f"\nInserisci i valori per il giorno {idx + 1}:")
        
    for misurazione in giorno:
        misurazione["sistolica"] = int(input(misurazione["orario"] + ", inserisci la sistolica: "))
        misurazione["diastolica"] = int(input(misurazione["orario"] + ", inserisci la diastolica: "))
        somma_sistolica += misurazione["sistolica"]
        somma_diastolica += misurazione["diastolica"]
    
    media_sistolica = somma_sistolica // 3
    media_diastolica = somma_diastolica // 3
    medie.append({"media sistolica": media_sistolica,
                      "media diastolica": media_diastolica})
    
    
    pressione_alta(misurazione, idx, giorno)
    
       

def registra_pressione():
    for idx, giorno in enumerate(registro_pressione):
        richiedi_misurazione(idx, giorno)
        
        
    ritorna_media()
    
        
registra_pressione()

