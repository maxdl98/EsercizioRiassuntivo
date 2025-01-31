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

def decoratore(funzione):
    def wrapper(*args, **kwargs):
          
        user = args[0]  
        passw = args[1]  
        pin = args[2] 

        if user == user_data.get("username") and passw == user_data.get("password") and pin == user_data.get("pin"):
            print("Login con successo")
            risultato = funzione(*args, **kwargs)
            return risultato
        else:
            print("credenziali sbagliate")
    return wrapper

@decoratore  
def verifica_login(user, passw, pin):
    print("funzione di login eseguita.")
    return True


user_input = input("Inserisci username: ")
passw_input = input("Inserisci password: ")
pin_input = input("Inserisci il tuo pin: ")

verifica_login(user_input, passw_input, pin_input)