import tkinter as tk
import random

words = [
    "acqua", "zebra", "fiume", "piano", "festa", "guida", "fiore",
    "fuoco", "ruota", "vento", "campo", "colle", "banco", "torre",
    "porta", "mezzo", "cuore", "salto", "dente", "arena", "porto",
    "falce", "manca", "muroa", "scena"
]

def wordle():
    parola_scelta = random.choice(words)
    tentativi = 6

    def controlla_parola():
        nonlocal tentativi
        parola_utente = entry.get().lower()
        if len(parola_utente) != 5:
            risultato_label.config(text="La parola deve essere di 5 lettere.")
            return

        if parola_utente == parola_scelta:
            risultato_label.config(text="Hai vinto!", fg="green")
            return
        else:
            risultato = ""
            for i in range(5):
                tentativi_label.config(text=f"Tentativi rimasti: {tentativi}")
                
                    
                if parola_utente[i] == parola_scelta[i]:
                    risultato += parola_utente[i].upper() + " "
                
                elif parola_utente[i] in parola_scelta:
                    if parola_utente.count(parola_utente[i]) <= parola_scelta.count(parola_utente[i]):
                        risultato += parola_utente[i].lower()
                
                    else:
                        risultato += "-"
                
                else:
                    risultato += "- "
            
            
            risultato_label.config(text=risultato)
            tentativi -= 1
            if tentativi >= 6:
                risultato_label.config(text=f"Hai perso! La parola era '{parola_scelta}'", fg="red")
            entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Wordle")
    root.geometry("300x200")
    
    tentativi_label=tk.Label(root, text="")
    tk.Label(root, text="Inserisci una parola di 5 lettere:").pack(pady=10)
    entry = tk.Entry(root)
    entry.pack()
    entry.bind("<Return>", lambda event: controlla_parola())

    btn = tk.Button(root, text="Controlla", command=controlla_parola)
    btn.pack(pady=10)

    risultato_label = tk.Label(root, text="", font=("Helvetica", 12))
    risultato_label.pack(pady=10)

    root.mainloop()

wordle()
