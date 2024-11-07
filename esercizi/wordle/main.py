import random
words = [
    "acqua", "zebra", "fiume", "piano", "festa", "nuvol", "guida", "fiore",
    "fuoco", "ruota", "vento", "campo", "colle", "banco", "torre", "campo",
    "porta", "mezzo", "livro", "cuore", "salto", "dente", "solea", "arena",
    "porto", "falce", "manca", "muroa", "tavol", "scena"
]



def wordle():
    parola_scelta = random.choice(words)
    tentativi = 0 
    print(parola_scelta)
    while tentativi < 6:
        parola_utente = input("Inserisci una parola di 5 lettere: ")
        if len(parola_utente) != 5:
            print("La parola deve essere di 5 lettere.")
            continue
        if parola_utente == parola_scelta:
            print("Hai vinto!")
            break
        else:
            risultato = ""
            for i in range(5):
                if parola_utente[i] == parola_scelta[i]:
                    risultato += parola_utente[i].upper()
                elif parola_utente[i] in parola_scelta:
                    if parola_utente.count(parola_utente[i]) <= parola_scelta.count(parola_utente[i]):
                        risultato += parola_utente[i].lower()
                    else:
                        risultato += "-"
                else:
                    risultato += "-"
            print(risultato)
        tentativi += 1
        
wordle()