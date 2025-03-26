import paho.mqtt.client as mqtt
import json
import ssl
import random
import time

# AWS IoT Configuration
aws_endpoint = "audvd8um3ivf8-ats.iot.us-east-1.amazonaws.com"  # Replace with your AWS endpoint
port = 8883
topic = "iot/environment"

# Paths to AWS IoT certificates 
ca_path = "certs/AmazonRootCA1.pem"
cert_path = "certs/device-certificate.pem.crt"
key_path = "certs/private.pem.key"


# Function to generate random sensor data
def generate_sensor_data():
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": random.randint(300, 2000)
    }

# Callback when connected
def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT Core with result code", rc)

# MQTT client setup
client = mqtt.Client()
client.on_connect = on_connect

# Use AWS IoT certificates
client.tls_set(ca_path, certfile=cert_path, keyfile=key_path, tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect(aws_endpoint, port, 60)

# Publish sensor data every 5 seconds
while True:
    sensor_data = generate_sensor_data()
    client.publish(topic, json.dumps(sensor_data))
    print("Published to AWS IoT:", sensor_data)
    time.sleep(5)
