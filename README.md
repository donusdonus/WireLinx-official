# **WireLinx Programmable Logic Control (PLC) User Manual**
<img src="./img/pic_10.png" width="80%">

## **Table of Contents**
- **WireLinx Programmable Logic Control (PLC) User Manual**
  - **Table of Contents**
  - [**1. Introduction**](#1-introduction)
    - **Overview of WireLinx PLC**
    - **Key Features**
    - **Applications**
  - [**2. Hardware Specifications**](#2-hardware-specifications)
  - [**3. Getting Started**](#3-getting-started)
    - **Unboxing and Setup**
    - **Connecting Power and Peripherals**
    - **Installing Required Software**
  - [**4. Programming WireLinx PLC**](#4-programming-wirelinx-plc)
    - **Supported Programming Languages**
    - **Using Ladder Logic (LD)**
    - **Configuring the Web Interface**
  - [**5. Communication Protocols**](#5-communication-protocols)
    - **RS-232 and RS-485 Communication**
    -  **Modbus RTU \& Modbus TCP**
    - **Wi-Fi and Web-based Configuration**
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
|8| **Jumper**               | Switch Power Source Terminal / USB   ||
|9| **LoRa extenal antenna** | Support antenna 2.4 GHZ    ||
|10| **Wi-Fi extenal antenna**| Support antenna 433 Mhz    ||
---

## **3. Getting Started**

### **Connecting Power and Peripherals**
- Connect the 12V-24V DC power supply to the PLC.
- Connect I/O modules as needed.
- Use Ethernet, RS-232, or RS-485 for communication.

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

### **Using Ladder Logic (LD)**
- Create rungs to define logical operations.
- Use timers, counters, and mathematical functions.

### **Configuring the Web Interface**
- Access the PLC via Wi-Fi.
- Open the configuration page on a browser.
- Modify network settings, I/O mappings, and debug logs.

---

## **5. Communication Protocols**
### **RS-232 and RS-485 Communication**
- **RS-232:** Used for general-purpose serial communication.
- **RS-485:** Ideal for industrial communication and Modbus RTU.

### **Modbus RTU & Modbus TCP**
- Used for industrial device communication.

### **Wi-Fi and Web-based Configuration**
- Wireless access to PLC settings.
- Remote programming and monitoring.

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
### Important for trainee
- Notebook for training.
- install gx-work2. 
- install ch340 driver. 
- drawing training kit. [**Download**](drawing/WireLinx_Station.pdf)

<img src="./img/training_1.png" width="80%">

1. **Introduction to PLCs**
   - What is a PLC?
   - How PLCs are used in industrial automation
2. **Understanding I/O Types**
   - Digital vs Analog Inputs/Outputs
   - Wiring and Configuration
3. **Programming with GX-WORK 2**
   - new project and test connection [Example](https://youtu.be/2iR9Q22t5_0)
   - download [Example](https://youtu.be/Tfad3BvSHQI)
   - upload [Example](https://youtu.be/ina59Y-c82w)
   - monitoring and modify value [Example](https://youtu.be/pGsTwQJBvRU)
1. **Ladder Logic Basics**
   - Creating simple logic circuits
   - input/output (X,Y)
   - internal bit (M,S)
   - Using timers (T)
   - Using counters (C)
   - Using Datamemory (D)
5. **Communication Protocols**
   - Configuring RS-232 and RS-485
   - Setting up Modbus communication
6. **Web-Based Configuration**
   - Connecting via Wi-Fi
   - Remote setup and diagnostics
7. **Troubleshooting & Maintenance**
   - Common PLC issues and solutions
   - Firmware updates and system diagnostics

---

End of Document.

