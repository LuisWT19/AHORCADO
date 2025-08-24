🎮 Juego del Ahorcado
¡Bienvenido a AHORCADO!
Este es un proyecto del clásico juego del Ahorcado, desarrollado en Python con una interfaz gráfica de usuario (GUI) construida con la librería PyQt6.

El juego funciona eligiendo una palabra secreta al azar de una lista predefinida. La palabra se oculta y el jugador tiene un número limitado de intentos para adivinarla, proponiendo letras una a una. Si la letra es correcta, se revela su posición en la palabra; si es incorrecta, se dibuja una parte del ahorcado.

💻 Análisis del Código
Tu código está estructurado de manera modular y organizada dentro de una clase principal llamada VentanaAhorcado. Aquí te explico cómo funcionan sus componentes clave:

Estructuras de Datos:

Diccionario (PALABRAS_Y_PISTAS): Asocia cada palabra secreta con una pista, lo que facilita la selección y gestión de los datos del juego.

Lista (DIBUJOS_AHORCADO): Contiene las diferentes etapas del dibujo del ahorcado. El juego usa el índice de esta lista para mostrar la imagen correcta según los intentos fallidos.

Clase VentanaAhorcado:

__init__: El constructor de la clase, que se encarga de inicializar la ventana y sus propiedades. Llama a los métodos initUI() y iniciar_juego() para configurar el juego.

initUI(): Se encarga de la creación y disposición de todos los elementos de la interfaz, como las etiquetas de texto, el campo de entrada y los botones.

iniciar_juego(): Reinicia el estado del juego: selecciona una nueva palabra, resetea los contadores y habilita la interfaz para una nueva partida.

procesar_adivinar(): Contiene la lógica principal del juego. Procesa la entrada del usuario, valida la letra, actualiza el estado del juego (contador de intentos, letras adivinadas) y llama a los métodos para actualizar la interfaz.

Lógica Principal: El código hace uso de sentencias if/else para la toma de decisiones (por ejemplo, si una letra es correcta o si se acabó el juego) y de bucles for para recorrer la palabra secreta.

🚀 Instalación y Uso
Sigue estos pasos para ejecutar el juego en tu computadora.

1. Requisitos Previos

Asegúrate de tener instalado Python y pip.

2. Clonar el Repositorio

Abre tu terminal y clona el proyecto con el siguiente comando:

Bash

git clone https://github.com/tu-usuario/AHORCADO.git

Navega al directorio del proyecto:

Bash

cd AHORCADO

3. Instalación de la Librería PyQt6

Para ejecutar el juego, necesitas instalar la librería PyQt6. Se recomienda usar un entorno virtual para mantener las dependencias del proyecto aisladas.

Crear y activar el entorno virtual:

Crear: python -m venv venv

Activar (Windows): .\venv\Scripts\activate

Activar (macOS/Linux): source venv/bin/activate

Instalar la librería:

Bash

pip install PyQt6

4. Ejecutar el Juego

Con el entorno activado, simplemente ejecuta el archivo principal del código:


ahorcado.py
