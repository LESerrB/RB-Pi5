import RPi.GPIO as GPIO
import time

# Pines GPIO para la comunicación con el HX711
HX711_DOUT = 5  # Pin de datos
HX711_SCK = 6   # Pin de reloj

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(HX711_DOUT, GPIO.IN)
GPIO.setup(HX711_SCK, GPIO.OUT)

def leer_hx711():
    """Lee el valor del HX711."""

    # Espera a que el HX711 esté listo
    while GPIO.input(HX711_DOUT):
        time.sleep(0.001)

    # Lee los 24 bits de datos
    datos = 0
    for _ in range(24):
        GPIO.output(HX711_SCK, GPIO.HIGH)
        datos = (datos << 1) | GPIO.input(HX711_DOUT)
        GPIO.output(HX711_SCK, GPIO.LOW)

    # Genera el pulso 25 para finalizar la lectura
    GPIO.output(HX711_SCK, GPIO.HIGH)
    GPIO.output(HX711_SCK, GPIO.LOW)

    # Convierte el valor a un entero con signo
    if datos & 0x800000:
        datos |= 0xFF000000

    return datos

try:
    while True:
        valor = leer_hx711()
        print(f"Valor del HX711: {valor}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa terminado.")

finally:
    GPIO.cleanup()