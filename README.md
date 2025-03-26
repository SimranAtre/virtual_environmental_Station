# virtual_environmental_Station

Project Title
Cloud-Based IoT System for Environmental Monitoring
Project Overview
This project simulates an IoT system where virtual environmental stations collect and send data from sensors (Temperature, Humidity, CO2 concentration) using the MQTT protocol. The data is then stored in the cloud (AWS IoT) and can be accessed through a web interface for the latest readings or historical data from the last five hours.
Technologies Used
•	Programming Language: Python (for sensor simulation)
•	MQTT Protocol: Used for communication between virtual sensors and cloud backend
•	Cloud Backend: AWS IoT (or ThingSpeak as an alternative)
•	Web Framework: Flask or any other lightweight web framework (if applicable)
Prerequisites
•	Python 3.x
•	AWS IoT or ThingSpeak account (for the cloud backend setup)
•	MQTT broker configuration
•	An IDE or text editor to run the scripts
•	Git (for version control)
Setup Instructions
1. Clone the Repository
Start by cloning the repository to your local machine:
git clone https://github.com/yourusername/IoT-System.git
cd IoT-System
2. Configure MQTT
•	Sign up for AWS IoT or ThingSpeak and create an MQTT topic to receive sensor data.
•	If using AWS IoT, follow the AWS IoT setup instructions to create a new thing, configure policies, and generate certificates.
•	Update the mqtt_config.py (or similar configuration file) with your MQTT broker details (AWS IoT endpoint, credentials, etc.).
3. Run the Virtual Sensor Program
Run the Python script to start generating random sensor data and sending it to the MQTT broker.
python3 aws_mqtt_publisher.py
python3 aws_mqtt_subscriber.py  
This script will simulate the environmental data (Temperature, Humidity, CO2) and publish the data at regular intervals to the MQTT topic.
4. Access Sensor Data
•	Latest Data: The web interface will display the latest sensor data for a specified environmental station.
•	Data from Last 5 Hours: The system will show sensor data from the last five hours based on the stored data in the cloud backend.
Usage
•	To view the latest sensor data, enter the unique ID of the environmental station into the web interface and submit.
•	To view historical data from the last 5 hours, enter the station ID and specify the time range.
