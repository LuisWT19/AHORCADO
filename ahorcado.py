import random
import os

# --- Datos del juego ---
# Lista de palabras y sus pistas.
PALABRAS_Y_PISTAS = {
    "CASA": "Lugar donde vives.",
    "AUTO": "Medio de transporte con 4 ruedas.",
    "PERRO": "Mejor amigo del hombre.",
    "CELULAR": "Dispositivo para comunicarte y navegar por internet.",
    "COMPUTADORA": "Máquina electrónica para procesar datos.",
    "TELEVISION": "Aparato para ver programas y películas.",
    "MOCHILA": "Objeto para llevar libros y útiles.",
    "WIFI": "Conexión inalámbrica a internet."
}

# Dibujos del Ahorcado para cada intento.
DIBUJOS_AHORCADO = [
    # 0 intentos fallidos
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    # 1 intento fallido
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    # 2 intentos fallidos
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    # 3 intentos fallidos
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    # 4 intentos fallidos
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    ---------
    """,
    # 5 intentos fallidos
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    ---------
    """,
    # 6 intentos fallidos - PERDIDO
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    ---------
    """
]

# --- Funciones del juego ---

def limpiar_consola():
    """Limpia la pantalla de la consola para un juego más limpio."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    """
    Muestra el mensaje de bienvenida y espera que el usuario presione Enter.
    """
    print("=========================")
    print("= JUEGO DEL AHORCADO    =")
    print("=========================")
    input("Presiona Enter para jugar...")

def seleccionar_palabra():
    """
    Selecciona una palabra aleatoria y su pista del diccionario.
    Devuelve la palabra en mayúsculas y su pista.
    """
    palabra_secreta = random.choice(list(PALABRAS_Y_PISTAS.keys()))
    pista = PALABRAS_Y_PISTAS[palabra_secreta]
    return palabra_secreta.upper(), pista

def jugar():
    """
    Función principal que contiene la lógica del juego del Ahorcado.
    """
    limpiar_consola()
    
    palabra_secreta, pista = seleccionar_palabra()
    
    letras_adivinadas = ["_"] * len(palabra_secreta)
    letras_intentadas = set()
    intentos_fallidos = 0
    max_intentos = 6
    
    while intentos_fallidos < max_intentos and "".join(letras_adivinadas) != palabra_secreta:
        limpiar_consola()
        
        # Muestra el estado actual del juego
        print(DIBUJOS_AHORCADO[intentos_fallidos])
        print("\nPista:", pista)
        print("\nPalabra:", " ".join(letras_adivinadas))
        print("Letras intentadas:", ", ".join(sorted(list(letras_intentadas))))
        print(f"Te quedan {max_intentos - intentos_fallidos} intentos.")
        
        # Pide una letra al jugador
        try:
            letra_usuario = input("\nIngresa una letra: ").upper()
            
            # Valida la entrada del usuario
            if len(letra_usuario) != 1 or not letra_usuario.isalpha():
                input("Entrada inválida. Ingresa solo una letra. Presiona Enter para continuar...")
                continue
            
            if letra_usuario in letras_intentadas:
                input("Ya intentaste esa letra. Presiona Enter para continuar...")
                continue
                
            letras_intentadas.add(letra_usuario)
            
            # Procesa la letra
            if letra_usuario in palabra_secreta:
                print("¡Correcto!")
                for i, letra_en_palabra in enumerate(palabra_secreta):
                    if letra_en_palabra == letra_usuario:
                        letras_adivinadas[i] = letra_usuario
            else:
                print("Incorrecto. Pierdes un intento.")
                intentos_fallidos += 1
                
        except (KeyboardInterrupt, EOFError):
            print("\nJuego cancelado.")
            return

    # --- Fin del juego ---
    limpiar_consola()
    print(DIBUJOS_AHORCADO[intentos_fallidos])
    print("\nPalabra:", palabra_secreta)
    
    if "".join(letras_adivinadas) == palabra_secreta:
        print("\n¡GANASTE!")
    else:
        print("\n¡PERDISTE!")
    
    # Pregunta si quiere jugar de nuevo
    while True:
        respuesta = input("¿Jugar otra vez? (S/N): ").upper()
        if respuesta == "S":
            jugar()  # Llama a la función jugar() de nuevo para reiniciar
            return
        elif respuesta == "N":
            print("¡Gracias por jugar!")
            return
        else:
            print("Opción no válida. Por favor, ingresa S o N.")

# --- Punto de entrada del programa ---
if __name__ == "__main__":
    mostrar_bienvenida()
    jugar()