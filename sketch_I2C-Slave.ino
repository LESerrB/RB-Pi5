#include <SPI.h>

void setup() {
  // Inicia la comunicación serial
  Serial.begin(9600);

  // Configura el puerto SPI como esclavo
  pinMode(MISO, OUTPUT);  // Necesario para que funcione como esclavo
  pinMode(SS, INPUT);     // Pin SS como entrada (para evitar interferencias)

  SPI.begin();  // Inicia la biblioteca SPI
  
  // Configura el modo SPI: modo 0 (CPOL = 0, CPHA = 0)
  SPI.setDataMode(SPI_MODE0);
  SPI.setClockDivider(SPI_CLOCK_DIV16);  // Ajusta la velocidad del reloj SPI
}

void loop() {
  // Lee el dato recibido a través del bus SPI
  byte receivedByte = SPI.transfer(0x00);  // Envía un byte vacío para recibir datos

  // Imprime el dato recibido en el monitor serial
  Serial.print("Recibido: ");
  Serial.println(receivedByte, HEX);  // Muestra el byte recibido en formato hexadecimal
}
