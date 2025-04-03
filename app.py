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
while True:
    print("ID register: ")
    msg = [0xD0, 0x00]
    print("MSG: ", msg)
    resp = spi.xfer2(msg)
    print("Resp: ", resp)
    # time.sleep(1)

# Turn on one segment of each character to show that we can
# address all of the segments

# while 1:
#     # The decimals, colon and apostrophe dots
#     msg = [0x77]
#     result = spi.xfer2(msg)
