import time
import spidev
import RPi.GPIO as GPIO

# Configura los pines de control (RES, DC, CS)
RES_PIN = 25
DC_PIN = 24
CS_PIN = 8

# Configura la Raspberry Pi para usar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RES_PIN, GPIO.OUT)
GPIO.setup(DC_PIN, GPIO.OUT)
GPIO.setup(CS_PIN, GPIO.OUT)

# Inicializa el bus SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus SPI 0, dispositivo 0
spi.max_speed_hz = 8000000  # Velocidad SPI (ajusta según sea necesario)
spi.mode = 0b00  # Modo SPI 0 (CPOL=0, CPHA=0)

def reset_display():
    GPIO.output(RES_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(RES_PIN, GPIO.HIGH)
    time.sleep(0.1)

def send_command(command):
    GPIO.output(DC_PIN, GPIO.LOW)  # Modo comando
    GPIO.output(CS_PIN, GPIO.LOW)  # Habilitar CS
    spi.xfer([command])  # Enviar el comando SPI
    GPIO.output(CS_PIN, GPIO.HIGH)  # Deshabilitar CS

def send_data(data):
    GPIO.output(DC_PIN, GPIO.HIGH)  # Modo datos
    GPIO.output(CS_PIN, GPIO.LOW)   # Habilitar CS
    spi.xfer([data])  # Enviar datos SPI
    GPIO.output(CS_PIN, GPIO.HIGH)  # Deshabilitar CS

def initialize_display():
    reset_display()

    # Inicializa el display SSD1312 con comandos específicos
    send_command(0xAE)  # Apagar el display
    send_command(0xD5)  # Configura el reloj
    send_command(0x80)  # Reloj 100Hz
    send_command(0xA8)  # Configura el multiplex
    send_command(0x3F)  # Rango multiplex
    send_command(0xD3)  # Desplazamiento de la posición
    send_command(0x00)  # No hay desplazamiento
    send_command(0x40)  # Dirección de inicio
    send_command(0x8D)  # Activar la carga de voltaje
    send_command(0x14)  # Configura el voltaje
    send_command(0xA1)  # Dirección de segmento
    send_command(0xC8)  # Modo de la comutación de los pines
    send_command(0xDA)  # Configuración de los pines de la pantalla
    send_command(0x12)  # Comando de los pines de la pantalla
    send_command(0x81)  # Control de contraste
    send_command(0x7F)  # Contraste medio
    send_command(0xD9)  # Configuración de pre-carga
    send_command(0xF1)  # Pre-carga a 0xF1
    send_command(0xDB)  # Configuración de la resistencia de la carga
    send_command(0x40)  # Resistencia a 0x40
    send_command(0xA4)  # Mostrar la imagen sin invertir
    send_command(0xA6)  # Configura la pantalla para no invertir
    send_command(0xAF)  # Enciende el display

def clear_display():
    for page in range(8):
        send_command(0xB0 + page)  # Selecciona la página de memoria
        send_command(0x00)  # Dirección columna baja
        send_command(0x10)  # Dirección columna alta
        for i in range(128):  # Limpia una página de 128 píxeles
            send_data(0x00)

def display_text(text):
    # Esta función solo muestra texto simplificado (reemplazar con código para controlar píxeles de texto)
    for i in range(len(text)):
        send_data(ord(text[i]))

if __name__ == "__main__":
    try:
        initialize_display()  # Inicializa el display
        clear_display()  # Limpia el display

        # Muestra un texto simplificado
        display_text("Hola Mundo")

        time.sleep(10)  # Muestra el texto durante 10 segundos

    finally:
        GPIO.cleanup()  # Limpia los pines GPIO al finalizar
