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
    print("Humedad: ")
    msg = [0xFD, 0xFE]
    resp = spi.xfer2(msg)
    print(resp)

    print("\n================================\n")

    print("Temperatura: ")
    msg = [0xFA, 0xFB, 0xFC]
    resp = spi.xfer2(msg)
    print(resp)

    
    print("\n================================\n")

    print("Presion: ")
    msg = [0xF7, 0xF8, 0xF9]
    resp = spi.xfer2(msg)
    print(resp)
    
    time.sleep(0.5)