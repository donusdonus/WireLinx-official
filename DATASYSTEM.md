#### D Memory Systen Content

| Address         |  Status         |Type|Access|      Description           | Note |
| :----------: | :--------------: |:---:|:---:| :-------------------------|:--:
| D8200 | CPU 0 Cycle Time (us.) |Uint16|R|Cycle Time Process In Core0 Unit In microsecond ||
| D8201 | CPU 1 Cycle Time (us.) |Uint16|R|Cycle Time Process In Core1 Unit In microsecond||
| D8202 | CHIP CPU Temperature |Uint16|R|Temperature Chip | Value x 0.1 |
| D8203 | PLC State ||R|PLC Mode Operation<br>0 = No Operation<br>1 = DATA RESET BEFORE PLC RUNNING<br>2 = PLC PROGRAM UNDER DETECTION<br>3 = NORMAL OPERATION<br>4 = STL OPERATION<br>5 = PLC PROGRAM ERROR HANDLING<br>6 = PLC PROGRAM ERROR<br>||
| D8204 | Voltage Shunt (mV.)  | Uint16 |R| Voltage Shunt in mV Unit ||
| D8205 | Voltage Bus (V.)     | Uint16 |R| Voltage Bus in V Unit ||
| D8206 | Current (mA.)        | Uint16 |R| Current in mA Unit ||
| D8207 | Power Consumtion (mW.) | Uint16 |R| Power in mW Unit ||
| D8208 | Voltage load (V.)  |Uint16 |R| Voltage load in V Unit ||
| D8209 | Timer Prescale  | |R|||
| D8210 | Timer 1 ms. Monitor | |R| Monitor Base Clock In 1 ms ||
| D8211 | Firmware Version | |R|||
| D8212 | WebConfig Version | |R|||
| D8213 | Device Group1 Status Enable | |R| D8213.0 I2C Bus Enable INA219<br>D8213.1 I2C Bus Enable ADS1115<br>D8213.2 I2C Bus Enable PCF8574<br>D8213.3 SPI Bus Enable SDCARD<br>D8213.4 SPI Bus Enable SX1278<br>||
| D8214 | Device Group2 Status Enable | |R|||
| D8220 | CH1 Analog Input 0-10V. | |R| Analog Value 0-26800 to 0-10 VDC.||
| D8221 | CH2 Analog Input 0-10V. | |R| Analog Value 0-26800 to 0-10 VDC.||
| D8222 | CH3 Analog Input 0-10V. | |R| Analog Value 0-26800 to 0-10 VDC.||
| D8223 | CH4 Analog Input 0-10V. | |R| Analog Value 0-26800 to 0-10 VDC.||
| D8225 | RGB1 (Red) | |R/W| RGB1 Red Color 0-255 ||
| D8226 | RGB1 (Green) | |R/W| RGB1 Green Color 0-255 ||
| D8227 | RGB1 (Blue) | |R/W| RGB1 Blue Color 0-255 ||
| D8228 | RGB2 (Red) | |R/W|RGB2 Red Color 0-255 ||
| D8229 | RGB2 (Green) | |R/W|RGB2 Green Color 0-255 ||
| D8230 | RGB2 (Blue) | |R/W|RGB2 Blue Color 0-255 ||
| D8231 | COM0 CONFIG0 | |R|||
| D8232 | COM0 CONFIG1 | |R|||
| D8233 | COM0 TX BUFFER | |R|Buffer Send Data Byte Unit|Valid|
| D8234 | COM0 RX BUFFER | |R|Buffer Recive Data Byte Unit|Valid|
| D8235 | COM0 Operate time (ms.) | |R|Cycle Send/Recive Time in ms. |Valid|
| D8236 | COM1 CONFIG0 | |R|||
| D8237 | COM1 CONFIG1 | |R|||
| D8238 | COM1 TX BUFFER | |R|Buffer Send Data Byte Unit|Valid|
| D8239 | COM1 RX BUFFER | |R|Buffer Recive Data Byte Unit|Valid|
| D8240 | COM1 Operate time (ms.) | |R|Cycle Send/Recive Time in ms. |Valid|
| D8241 | COM2 CONFIG0 | |R|||
| D8242 | COM2 CONFIG1 | |R|||
| D8243 | COM2 TX BUFFER | |R|Buffer Send Data Byte Unit|Valid|
| D8244 | COM2 RX BUFFER | |R|Buffer Recive Data Byte Unit|Valid|
| D8245 | COM2 Operate time (ms.) | |R|Cycle Send/Recive Time in ms. |Valid|
| D8246 | LoRa CONFIG0 | |R|||
| D8247 | LoRa CONFIG1 | |R|||
| D8248 | LoRa TX BUFFER | |R|||
| D8249 | LoRa RX BUFFER | |R|||
| D8250 | LoRa Operate time (us.) | |R|||
| D8251 | SDCARD Operate time (ms.) | |R| SDCARD Scantime in ms.|Valid|
| D8252 | SPI ScanTimes (us.) | |R| SPI ScanTime in Microsecond Unit.||
| D8253 | IIC ScanTimes (ms.) | |R| IIC ScanTime in Microsecond Unit.|Valid|






