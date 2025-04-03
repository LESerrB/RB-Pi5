import time
import spidev

bus = 0
device = 0

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 1000000 #1MHZ
spi.mode = 0

################################################################
############## Codigo para Display 7segmentos SPI ##############
################################################################
# Id query
print("ID register: ")
msg = [0xD0]
print("MSG: ", msg)
resp = spi.xfer2(msg)
print("Resp: ", resp)

while True:
    print("Status: ")
    msg = [0xF3]
    resp = spi.xfer2(msg)
    print("resp: " + resp + "[0]: " + resp[0] + " [1]: " + resp[1])
    print(1 & resp[0])

    if (8 & resp[0]) == 0:
        print("Transfiriendo...")
    else:
        print("Midiendo...")

    if (1 & resp[0]) == 0:
        print("Copiado al registro, se puede leer")
    else:
        print("Copiando...")

    # print("0 updated", 1 & resp[0])

    # print("\n================================\n")

    # print("Humedad: ")
    # msg = [0xFD, 0xFE]
    # resp = spi.xfer2("FD: ", msg[0], "FE: ", msg[1])
    # print(resp)

    # print("\n================================\n")

    # print("Temperatura: ")
    # msg = [0xFA, 0xFB, 0xFC]
    # resp = spi.xfer2(msg)
    # print(resp)

    # print("\n================================\n")

    # print("Presion: ")
    # msg = [0xF7, 0xF8, 0xF9]
    # resp = spi.xfer2(msg)
    # print(resp)

    # print("\n================================\n")
    time.sleep(1)