import sys
import random
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QLabel, QLineEdit, QPushButton, 
                             QHBoxLayout, QSizePolicy)
from PyQt6.QtCore import Qt

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
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """
]


class VentanaAhorcado(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Juego del Ahorcado - PyQt6")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #f0f0f0;")
        
        self.initUI()
        self.iniciar_juego()

    def initUI(self):
        # Layout principal de la ventana
        layout_principal = QVBoxLayout()
        layout_principal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Etiqueta para el dibujo del ahorcado
        self.label_dibujo = QLabel()
        self.label_dibujo.setText(DIBUJOS_AHORCADO[0])
        self.label_dibujo.setStyleSheet("font-family: monospace; font-size: 14px; color: #333;")
        self.label_dibujo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.label_dibujo)

        # Etiqueta para la palabra
        self.label_palabra = QLabel()
        self.label_palabra.setStyleSheet("font-size: 24px; font-weight: bold; color: #007bff;")
        self.label_palabra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.label_palabra)
        
        # Etiqueta para la pista
        self.label_pista = QLabel()
        self.label_pista.setStyleSheet("font-style: italic; color: #666;")
        self.label_pista.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.label_pista)

        # Etiqueta para las letras ya intentadas
        self.label_intentadas = QLabel("Letras intentadas: ")
        self.label_intentadas.setStyleSheet("font-size: 12px; color: #999;")
        self.label_intentadas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.label_intentadas)
        
        # Etiqueta para los intentos restantes
        self.label_intentos = QLabel()
        self.label_intentos.setStyleSheet("font-size: 12px; color: #dc3545;")
        self.label_intentos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(self.label_intentos)

        # Contenedor para la entrada de texto y el botón
        layout_input = QHBoxLayout()
        layout_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.entrada_letra = QLineEdit()
        self.entrada_letra.setFixedSize(50, 30)
        self.entrada_letra.setMaxLength(1)
        self.entrada_letra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_input.addWidget(self.entrada_letra)
        
        self.boton_adivinar = QPushButton("Adivinar")
        self.boton_adivinar.clicked.connect(self.procesar_adivinar)
        self.boton_adivinar.setFixedSize(100, 30)
        self.boton_adivinar.setStyleSheet("background-color: #28a745; color: white; font-weight: bold; border-radius: 5px;")
        layout_input.addWidget(self.boton_adivinar)
        
        layout_principal.addLayout(layout_input)

        # Botón para reiniciar el juego
        self.boton_reiniciar = QPushButton("Jugar de nuevo")
        self.boton_reiniciar.clicked.connect(self.iniciar_juego)
        self.boton_reiniciar.setVisible(False)
        self.boton_reiniciar.setStyleSheet("background-color: #007bff; color: white; font-weight: bold; border-radius: 5px;")
        layout_principal.addWidget(self.boton_reiniciar)

        self.setLayout(layout_principal)

    def iniciar_juego(self):
        self.palabra_secreta, self.pista = random.choice(list(PALABRAS_Y_PISTAS.items()))
        self.letras_adivinadas = ["_"] * len(self.palabra_secreta)
        self.letras_intentadas = set()
        self.intentos_fallidos = 0
        self.max_intentos = 6
        
        self.entrada_letra.setEnabled(True)
        self.boton_adivinar.setEnabled(True)
        self.boton_reiniciar.setVisible(False)
        
        self.actualizar_interfaz()

    def procesar_adivinar(self):
        letra_usuario = self.entrada_letra.text().upper()
        self.entrada_letra.clear()
        
        if not letra_usuario.isalpha() or len(letra_usuario) != 1:
            self.label_intentos.setText("Entrada inválida. Ingresa solo una letra.")
            return

        if letra_usuario in self.letras_intentadas:
            self.label_intentos.setText("Ya intentaste esa letra.")
            return
        
        self.letras_intentadas.add(letra_usuario)
        
        if letra_usuario in self.palabra_secreta:
            self.label_intentos.setText("¡Correcto!")
            for i, letra_en_palabra in enumerate(self.palabra_secreta):
                if letra_en_palabra == letra_usuario:
                    self.letras_adivinadas[i] = letra_usuario
        else:
            self.intentos_fallidos += 1
            self.label_intentos.setText("Incorrecto. Pierdes un intento.")
        
        self.actualizar_interfaz()
        self.verificar_fin_juego()

    def actualizar_interfaz(self):
        self.label_dibujo.setText(DIBUJOS_AHORCADO[self.intentos_fallidos])
        self.label_palabra.setText(" ".join(self.letras_adivinadas))
        self.label_pista.setText(f"Pista: {self.pista}")
        self.label_intentadas.setText("Letras intentadas: " + ", ".join(sorted(list(self.letras_intentadas))))
        self.label_intentos.setText(f"Te quedan {self.max_intentos - self.intentos_fallidos} intentos.")

    def verificar_fin_juego(self):
        if self.intentos_fallidos >= self.max_intentos:
            self.label_intentos.setText(f"¡PERDISTE! La palabra era: {self.palabra_secreta}")
            self.entrada_letra.setEnabled(False)
            self.boton_adivinar.setEnabled(False)
            self.boton_reiniciar.setVisible(True)
        elif "_" not in self.letras_adivinadas:
            self.label_intentos.setText("¡GANASTE! ¡Felicidades!")
            self.entrada_letra.setEnabled(False)
            self.boton_adivinar.setEnabled(False)
            self.boton_reiniciar.setVisible(True)

# --- Punto de entrada del programa ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaAhorcado()
    ventana.show()
    sys.exit(app.exec())