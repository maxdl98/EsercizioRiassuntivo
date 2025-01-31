
# ogni 20 min committate

# possiamo comunicare tra noi
# chatgpt possiamo chiedere una mano



# Inizializzazione:

# Crea una variabile somma e impostala a 0. 
# Questa variabile servirà per tenere traccia della somma dei numeri che l'utente inserisce.
# Crea una variabile contatore e impostala a 0. 
# Questa variabile servirà per contare quante volte l'utente ha inserito un numero valido.
# Loop di inserimento:

# Usa un ciclo while per chiedere all'utente di inserire un numero.
# Se l'utente inserisce un numero negativo, 
# il programma deve fermarsi e visualizzare il totale della somma dei numeri inseriti fino a quel momento e quanti numeri validi sono stati inseriti.
# Condizioni:
# Se l'utente inserisce un numero pari, aggiungilo alla variabile somma e incrementa il contatore.
# Se l'utente inserisce un numero dispari, 
# non incrementare il contatore.
# Se l'utente inserisce qualcosa che non è un numero (ad esempio, una stringa),
# mostra un messaggio di errore e chiedi di inserire un numero valido, senza interrompere il ciclo.

somma = 0
cont = 0

while True:
    try:
        chiedo = int(input("Inserisci un numero"))
    except Exception:
        print("C'è un errore")
        
    
    if chiedo > 0 and chiedo % 2 == 0:
        cont = cont + 1
        somma = somma + chiedo
    
    if chiedo < 0 and chiedo % 2 == 1:
        print("Hai inserito un numero non valido")
        print("Ecco la somma: ", somma, "Ecco quanti numeri hai inserito: ", cont)
        break
