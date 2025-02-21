# **WireLinx Programmable Logic Control (PLC) User Manual**
<img src="./img/pic_10.png" width="80%">

## **Table of Contents**
- **WireLinx Programmable Logic Control (PLC) User Manual**
  - **Table of Contents**
  - [**1. Introduction**](#1-introduction)
    - Overview of WireLinx PLC
    - Key Features
    - Applications
  - [**2. Hardware Specifications**](#2-hardware-specifications)
  - [**3. Getting Started**](#3-getting-started)
    - Installing Required Software
    - Configuring the Web Interfac
  - [**4. Programming WireLinx PLC**](#4-programming-wirelinx-plc)
    - Supported Programming Languages
    - Internal Memory Structure
  - [**5. Communication Protocols**](#5-communication-protocols)
    - Wi-Fi and Web-based Configuration
    - RS-232 and RS-485 Communication
    - Modbus RTU \& Modbus TCP
  - [**6. Working with I/O**](#6-working-with-io)
  - [**7. Safety and Maintenance**](#7-safety-and-maintenance)
  - [**Training Topics for Basic PLC**](#training-topics-for-basic-plc)
---

## **1. Introduction**
### **Overview of WireLinx PLC**
WireLinx PLC is a programmable logic controller designed for industrial automation and IoT applications. It features a modular and flexible architecture, allowing for seamless integration with existing systems.

### **Key Features**
- **Core Processor:** ESP32-S3 with built-in Wi-Fi
- **Digital Inputs:** Source Type with Isolation
- **Digital Outputs:** Sink Type with Isolation
- **Communication Interfaces:** RS232 , RS485
- **Real-Time Clock (RTC) Support**
- **Web-Based Configuration Interface**
- **Supports Ladder Logic Programming**

### **Applications**
WireLinx PLC can be used in:
- Industrial automation
- Smart building systems
- SCADA & remote monitoring
- Energy management
- IoT & smart agriculture

---

## **2. Hardware Specifications**

<img src="./img/layout_1.png" width="80%">

|No.| Component               | Specification                    |Number|
|-|-------------------------|---------------------------------|---|
|| **Processor**          | ESP32-S3                        ||
|1| **Power Suppply**     | DC Voltage 24VDC.     ||
|2| **Analog Inputs**       | Voltage Input 0-10V. Resolution 16 Bits |4 Channels|
|3| **Digital Inputs**     | 24VDC Source Type    | 8 Points|
|4| **Digital Outputs**    | 24VDC Sink Type  100 mA/ch   |8 Points|
|5| **RS-485**            | 1 Channel Support ASCII , FXCPU ,  ModbusSlave  |1 Channel|
|6| **RS-232**            | 1 Channel Support ASCII , FXCPU ,  ModbusSlave  |1 Channel|
|7| **USB**               | USB-Serial Programmable Port   |1 Channel|
|8| **Jumper**               | Switch Select Power Source Terminal / USB   ||
|9| **LoRa extenal antenna** | Support antenna 2.4 GHZ    ||
|10| **Wi-Fi extenal antenna**| Support antenna 433 Mhz    ||
---

## **3. Getting Started**

### **Installing Required Software**
- **Download and install GX-WORK2**

### **Operating Buttons and Status Indicators**
WireLinx PLC is equipped with multiple buttons and LED indicators for user interaction and system status monitoring.

#### **Buttons**
- **Reset Button:** Used to restart the PLC without affecting saved configurations.
- **User Button:** Can be programmed for specific functions such as mode selection or manual override.

#### **Status Indicators (LEDs)**
- **Power LED:** Indicates whether the PLC is powered on.
- **Communication LED:** Blinks when there is active communication via RS-232, RS-485, or Wi-Fi.
- **I/O Status LEDs:** Display the state of digital inputs and outputs.
- **Error LED:** Lights up in case of system errors or malfunctions.
---

## **4. Programming WireLinx PLC**
### **Supported Programming Languages**
- **Ladder Logic**

### **Internal Memory Structure**
| **Memory Type** | **Usage**                                   | **Address Range** | **Capacity**      |
|---------------|------------------------------------------|----------------|----------------|
| **X (Input Relays)**  | Represents physical input points       | X0 - X377  | 256 points     |
| **Y (Output Relays)** | Represents physical output points      | Y0 - Y377   | 256 points     |
| **M (Internal Relays)** | General-purpose internal logic storage | M0 - M3071        | 3072 points    |
| **S (Step Relays)**   | Used for step sequence control        | S0 - S999         | 1000 points    |
| **D (Data Registers)** | Stores numerical values for processing | D0 - D7999        | 8000 words (16-bit each) |
| **T (Timers)**        | Used for timing operations            | T0 - T255         | 256 timers     |
| **C (Counters)**      | Used for counting operations          | C0 - C199         | 200 counters   |


---

## **5. Communication Protocols**

### **Wi-Fi and Web-based Configuration**
- Wireless access to PLC settings.

    <img src="image-18.png" width="70%">
    <br>
- Remote programming and monitoring.

### **RS-232 and RS-485 Communication**
- **RS-232:** Used for general-purpose serial communication.
- **RS-485:** Ideal for industrial communication and Modbus RTU.

### **Modbus RTU & Modbus TCP**
- Table Modbus Address Mapping common with ModbusTCP Server and ModbusRTU Slave Mode.

| **Modbus** |**PLC**| **Type**                  | **Access**  | **Function Code** | **Description**                        |
|-|-|-------------------------|------------|-----------------|------------------------------------|
| **00001 - 01000** |**S0 - S999**| **Coil (Discrete Output)**  | Read/Write  | 01 (Read) / 05, 15 (Write) | Stores ON/OFF values for outputs  |
| **10001 - 11536** |**M1 - M1535**| **Discrete Input**       | Read-only   | 02 (Read)        | Stores ON/OFF values for inputs   |
| **30001 - 33000** |**D0 - 02999**| **Input Register**       | Read-only   | 04 (Read)        | Stores analog input values        |
| **40001 - 43000** |**D3000 - 05999**| **Holding Register**     | Read/Write  | 03 (Read) / 06, 16 (Write) | Stores analog output and parameters |


---
## **6. Working with I/O**
- ### Example input wiring connection

  <img src="./img/input_wiring.png" width="80%">
  
- ### Example output wiring connection
  
  <img src="./img/output_wiring.png" width="80%">
---
## **7. Safety and Maintenance**
---

## **Training Topics for Basic PLC**
### prepare for trainee

- Notebook for training.
- install gx-work2. 
- install ch340 driver. 
- drawing training kit. [**Download**](drawing/WireLinx_Station.pdf)

<img src="./img/training_1.png" width="80%">

<br><h2>1.Ladder Logic Basics</h2>
| No.        | Symbol           | Description  |
| :-: |:-| :-----|
| 1 | ![alt text](image-7.png) | Contact Normally Open |
| 2 | ![alt text](image-9.png) | Contact Normally Close |
| 3 | ![alt text](image-8.png) |Coil |
| 4 | ![alt text](image-10.png)|Timer |
| 5 | ![alt text](image-11.png)|    Counter |
| 6 | ![alt text](image-13.png)|    Instruction Set |

<br><h2>2. Programming with GX-WORK 2.</h2>
2.1 new project and test connection</p>
<a href="https://youtu.be/2iR9Q22t5_0">
<img src="image-19.png" alt="Video Title" width="400">
</a>

<br>2.2 download ladder logic to plc.</p>
<a href="https://www.youtube.com/watch?v=Tfad3BvSHQI">
<img src="image-20.png" alt="Video Title" width="400">
</a>

<br>2.3 upload ladder logic from plc.</p>
<a href="https://www.youtube.com/watch?v=ina59Y-c82w">
<img src="image-21.png" alt="Video Title" width="400">
</a>

<br>2.4 monitoring and modify value.</p>
<a href="https://youtu.be/pGsTwQJBvRU">
<img src="image-22.png" alt="Video Title" width="400">
</a>

<h2>3. PLC Basic Programming Exercises.</h2>
3.1 Create simple ladder logic program to turn on an output when a switch is pressed<p>
    <p style="text-align: center;">
       <img src="image-24.png" width="40%">
    </p>
    3.2 Write program to self-holding circuit a relay using a start and stop button.<p>
    <p style="text-align: center;">
       <img src="image-25.png" width="40%">
    </p><br>
    3.3 Write timer to turn off relay automatically after a preset time.<p>
    </p>
    3.4 Write program to counter the number of cycle.<p>
    </p>
    3.5 Convert Electrical function process to ladder logic process.<p>
    <p style="text-align: center;">
       <img src="image-15.png" width="70%">
    </p><br>
4. **Communication Protocols**
   - Configuring RS-232 and RS-485
   - Setting up Modbus communication

5. **Web-Based Configuration**
   - Connecting via Wi-Fi
   - Remote setup and diagnostics

6. **Troubleshooting & Maintenance**
   - Common PLC issues and solutions
   - Firmware updates and system diagnostics

---

End of Document.

