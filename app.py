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

msg = [0x88, 0x8A, 0x8C]
resp = spi.xfer2(msg)
dig_T1 = resp[0]
dig_T2 = resp[1]
dig_T3 = resp[2]

while True:
    print("Status: ")
    msg = [0xF3]
    resp = spi.xfer2(msg)
    print("resp: ", resp, " | [0]: ", resp[0])
    print(1 & resp[0])

    if (8 & resp[0]) == 0:
        print("Transfiriendo...")
    else:
        print("Midiendo...")

    if (1 & resp[0]) == 0:
        print("Copiado al registro, se puede leer")
    else:
        print("Copiando...")

    print("\n================================\n")

    # print("Humedad: ")
    # msg = [0xFD, 0xFE]
    # resp = spi.xfer2("FD: ", msg[0], "FE: ", msg[1])
    # print(resp)

    # print("\n================================\n")

    print("Temperatura: ")
    msg = [0xFA, 0xFB, 0xFC]
    resp = spi.xfer2(msg)
    print(resp)
    adc_T = ((resp[0] << 16) | (resp[1] << 8) | resp[2]) >> 4
    print(adc_T)
    # Returns tempe rature in DegC, resolution is 0.01 DegC. Output value of “5123” equals 51.23 DegC.
    # t_fine carries fine temperature as global value
    var1 = ((((adc_T>>3) - (dig_T1<<1))) * (dig_T2)) >> 11;
    var2 = (((((adc_T>>4) - (dig_T1)) * ((adc_T>>4) - (dig_T1)))>> 12) * (dig_T3)) >> 14;
    t_fine = var1 + var2;
    T = (t_fine * 5 + 128) >> 8;
    print("Temp: ", T = T / 100)

    # print("\n================================\n")

    # print("Presion: ")
    # msg = [0xF7, 0xF8, 0xF9]
    # resp = spi.xfer2(msg)
    # print(resp)

    # print("\n================================\n")
    time.sleep(1)

# Returns pressure in Pa as unsigned 32 bit integer in Q24.8 format (24 integer bits and 8 fractional bits).
#Output value of “24674867” represents 24674867/256 = 96386.2 Pa = 963.862 hPa
# BME280_U32_t BME280_compensate_P_int64(BME280_S32_t adc_P){
#     BME280_S64_t var1, var2, p;
#     var1 = ((BME280_S64_t)t_fine) – 128000;
#     var2 = var1 * var1 * (BME280_S64_t)dig_P6;
#     var2 = var2 + ((var1*(BME280_S64_t)dig_P5)<<17);
#     var2 = var2 + (((BME280_S64_t)dig_P4)<<35);
#     var1 = ((var1 * var1 * (BME280_S64_t)dig_P3)>>8) + ((var1 * (BME280_S64_t)dig_P2)<<12);
#     var1 = (((((BME280_S64_t)1)<<47)+var1))*((BME280_S64_t)dig_P1)>>33;

#     if (var1 == 0)
#         return 0; #avoid exception caused by division by zero

#     p = 1048576-adc_P;
#     p = (((p<<31)-var2)*3125)/var1;
#     var1 = (((BME280_S64_t)dig_P9) * (p>>13) * (p>>13)) >> 25;
#     var2 = (((BME280_S64_t)dig_P8) * p) >> 19;
#     p = ((p + var1 + var2) >> 8) + (((BME280_S64_t)dig_P7)<<4);

#     return (BME280_U32_t)p;
# }

#Returns humidity in %RH as unsigned 32 bit integer in Q22.10 format (22 integer and 10 fractional bits).
#Output value of “47445” represents 47445/1024 = 46.333 %RH
# BME280_U32_t bme280_compensate_H_int32(BME280_S32_t adc_H){
#     BME280_S32_t v_x1_u32r;
#     v_x1_u32r = (t_fine – ((BME280_S32_t)76800));
#     Bosch Sensortec | BME280 Data sheet 26 | 60
#     Modifications reserved | Data subject to change without notice Document number: BST-BME280-DS001-23 Revision_1.23_012022
#     v_x1_u32r = (((((adc_H << 14) – (((BME280_S32_t)dig_H4) << 20) – (((BME280_S32_t)dig_H5) *
#     v_x1_u32r)) + ((BME280_S32_t)16384)) >> 15) * (((((((v_x1_u32r *
#     ((BME280_S32_t)dig_H6)) >> 10) * (((v_x1_u32r * ((BME280_S32_t)dig_H3)) >> 11) +
#     ((BME280_S32_t)32768))) >> 10) + ((BME280_S32_t)2097152)) * ((BME280_S32_t)dig_H2) +
#     8192) >> 14));
#     v_x1_u32r = (v_x1_u32r – (((((v_x1_u32r >> 15) * (v_x1_u32r >> 15)) >> 7) *
#     ((BME280_S32_t)dig_H1)) >> 4));
#     v_x1_u32r = (v_x1_u32r < 0 ? 0 : v_x1_u32r);
#     v_x1_u32r = (v_x1_u32r > 419430400 ? 419430400 : v_x1_u32r);
#     return (BME280_U32_t)(v_x1_u32r>>12);
# }
