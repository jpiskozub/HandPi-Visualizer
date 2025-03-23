# HandPi Project

## Overview
The Visualizer consists of two Python scripts that work together to collect, transmit, and visualize data from flex sensors and an IMU (Inertial Measurement Unit). The system uses MQTT protocol for communication between components.

## Components

### 1. handpy_mockup.py
This script simulates a hand-tracking device with flex sensors and IMU data. It acts as an MQTT publisher that sends sensor data to a specified broker.

#### Functionality:
- Connects to an MQTT broker at IP 192.168.0.100 on port 1883
- Publishes mock sensor data to the 'handpi' topic
- Simulates continuous data transmission (10,000 iterations)
- Each message contains 25 values representing:
  - 10 flex sensor values (first 10 values)
  - IMU data including Euler angles and accelerometer readings
  - Additional sensor metrics

### 2. handvis.py
This script is a data visualizer that subscribes to the MQTT topic and displays the received sensor data in real-time using DearPyGui.

#### Functionality:
- Connects to the same MQTT broker and subscribes to the 'handpi' topic
- Processes received messages through a queue system
- Renders a graphical interface with a bar chart displaying flex sensor values
- Contains mappings for:
  - ADC channels (P1_1, P1_2, P2_1, etc.)
  - IMU channels (Euler_x, Euler_y, Euler_z, Acc_x, Acc_y, Acc_z)
  - Sign types classification (static vs. dynamic) for what appears to be sign language characters

## Data Structure
The data transmitted between the scripts consists of tuples with 25 values:
- Values 0-9: Flex sensor readings for different fingers/joints
- Values 10-12: Euler angles (x, y, z)
- Values 13-15: Accelerometer data (x, y, z)
- Values 16-24: Additional metrics or sensor readings

## Dependencies
The project requires the following Python libraries:
- `paho-mqtt`: For MQTT communication
- `dearpygui`: For graphical visualization
- Standard libraries: `queue`

## Usage
1. Ensure an MQTT broker is running at the specified IP address (192.168.0.100:1883)
2. Run `handpy_mockup.py` to start publishing simulated sensor data
3. Run `handvis.py` to visualize the incoming data in real-time

## Notes
The system appears designed for hand gesture recognition, possibly for sign language interpretation, as suggested by the sign_types_dict that maps Polish alphabet characters to static or dynamic gesture types.
