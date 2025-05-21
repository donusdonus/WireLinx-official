## WireLinx PLC Training Course [ Commissiong Concept ]

### Content
- #### LAB1 Ladder Logic Programming Concept ( 08:00 - 09:00 )
  - ##### 1.1 Study Machine Concept.
  - ##### 1.2 FlowChart Process Sequence. 
  - ##### 1.3 Pattern Ladder Logic Program.
  - ##### 1.4 Input File Program Commissioning.
  - ##### 1.5 Output File Program Commissioning.
  - ##### 1.6 Process File Program Commissioning.
  - ##### 1.7 Output Address Mapping.
  - ##### 1.8 Predictive Maintainence Concept.
- #### Guide PLC Memory address ( 10:20 - 11:00)
- #### LAB2 Application analog sensor ( 11:00 - 12:00 )
  - ##### 2.1 Digital and Analog Signal
  - ##### 2.2 Analog Digital Converter (ADC) with voltage.
  - ##### 2.3 Sensor Temperature and Humidity Convert.
  - ##### 2.4 Ladder Logic Compute Scaling Data.
- #### LAB3 Application Scada system with PLC ( 13:00 - 14:00 )
---
## LAB1 Ladder Logic Programming Concept ( 08:00 - 09:00 )
### 1.1 Study Machine Concept.
![alt text](FillerMachine.gif)

---
### 1.2 FlowChart Process Sequence. 
![alt text](image-21.png)

---
### 1.4 Input File Program Commissioning.
![alt text](image-22.png)
```
File:INPUT
```
![alt text](image-2.png)

---
### 1.5 Output File Program Commissioning.
```
File:OUTPUT
```
![alt text](image-3.png)

---
### 1.6 Process File Program Commissioning.
![alt text](image-23.png)
```
File:LAB1  
Section:Start Process 
```
![alt text](image-1.png)
```
File:LAB1  
Section:Prepare Machine Before Run
```
![alt text](image-5.png)
```
File:LAB1  
Section:Machine Running
```
![alt text](image-6.png)
```
File:LAB1  
Section:Process
```
![alt text](image-8.png)
```
File:LAB1  
Section:Counter And Stop Process
```
![alt text](image-9.png)

---
### 1.7 Output Address Mapping.
![alt text](image-24.png)
```
File:OUTPUT
```
![alt text](image-10.png) 
![alt text](image-11.png)
![alt text](image-12.png)
![alt text](image-13.png)
![alt text](image-14.png)

---
### 1.8 Predictive Maintainence Concept.

![alt text](image-26.png)
```
File:LAB2
Section Counter Hardware Running
```
![alt text](image-15.png)
```
File:LAB2
Section Counter Hardware All Reset
```
![alt text](image-16.png)
```
File:LAB2
Section Detect Cycle Hardware Maintain
```
![alt text](image-18.png)
```
File:OUTPUT
```
![alt text](image-19.png)

---
## Guide PLC Memory address ( 10:20 - 11:00)
- ### System Memory.
---

## LAB2 Application analog sensor ( 11:00 - 12:00 )
### 2.1 Digital and Analog Signal
![alt text](image-30.png)

---
### 2.2 Analog Digital Converter (ADC) with voltage.
![alt text](image-31.png)

---
### 2.3 Sensor Temperature and Humidity Convert.
![alt text](image-32.png)

---

### 2.4 Ladder Logic Compute Scaling Data.
```
File:LAB21
```
![alt text](image-20.png)

---

## Application Scada system with PLC ( 13:00 - 14:00 )
![alt text](image-33.png)
![alt text](image-34.png)
![alt text](image-35.png)
