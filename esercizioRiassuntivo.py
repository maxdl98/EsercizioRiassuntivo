
# ogni 20 min committate

# possiamo comunicare tra noi
# chatgpt possiamo chiedere una mano



# Inizializzazione:
#l'utente deve loggarsi
# inserire username password e pin in un dizionario
# Crea una variabile somma e impostala a 0. 
# Questa variabile servirà per tenere traccia della somma dei numeri che l'utente inserisce.
# Crea una variabile contatore e impostala a 0. 
# Questa variabile servirà per contare quante volte l'utente ha inserito un numero valido.
# Loop di inserimento:

# Usa un ciclo while per chiedere all'utente di inserire un numero.
# Se l'utente inserisce un numero negativo dispari, 
# e aggiungerli a un set e stamparli.
# Condizioni:
# Se l'utente inserisce un numero pari, aggiungilo alla variabile somma e incrementa il contatore.
# Se l'utente inserisce un numero dispari, 
# non incrementare il contatore.

somma = 0
cont = 0

username = "massi"
password = "password123"
pin = "1234"

user_data = {
    "username": "massi",
    "password": "password123",
    "pin": "1234"
}

user = input("Inserisci username: ")
passwo = input("Inserisci password: ")
pin_input = input("Inserisci il tuo pin: ")

if user == user_data.get("username") and passwo == user_data.get("password") and pin_input == user_data.get("pin"):
    
    while True:
        chiedo = int(input("Inserisci un numero: "))
        
        num = []  
        messaggio = {"ciao inserisci numeri dispari"}  
        
        if chiedo > 0 and chiedo % 2 == 0:  
            cont += 1
            num.append(chiedo)
            somma += chiedo
        
        elif chiedo < 0 and chiedo % 2 != 0: 
            print("Hai inserito un numero non valido")
            messaggio.add(chiedo)
            print(messaggio)
            break  

