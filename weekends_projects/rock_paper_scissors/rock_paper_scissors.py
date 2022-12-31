import random

def play():
    print("¿Piedra, papel o tijera?") # Titulo principal
    user_input = input().lower() # Usuario ingresa alguna de las 3 opciones mencionadas y se convierte a miniscula toda la palabra
    print(f"Input de usuario: {user_input}") # Verificacion de lower case

    computer_input = random.choice(["piedra", "papel", "tijera"]) # Computador selecciona de manera random alguna de las 3 opciones posibles
    print(f"Computer input: {computer_input}") # Verificacion de random.choice

    if user_input == computer_input:
        return "Es un empate"
    
    if is_win(user_input, computer_input):
        return "Ganaste!"
    
    return "Perdiste"

def is_win(player, opponent):
    # Devuelve verdadero si el player gana
    if (player == "piedra" and opponent == "tijera") or (player == "tijera" and opponent == "papel") \
        or (player == "papel" and opponent == "piedra"):
        return True

print(play()) # El colocarle print permite que lo que este con return en la funcion se muestre por consola/pantalla