import paho.mqtt.client as mqtt
import ssl

# AWS IoT Configuration
aws_endpoint = "audvd8um3ivf8-ats.iot.us-east-1.amazonaws.com"
port = 8883
topic = "iot/environment"

# Paths to AWS IoT certificates 
ca_path = "certs/AmazonRootCA1.pem"
cert_path = "certs/device-certificate.pem.crt"
key_path = "certs/private.pem.key"

# Callback to print incoming messages
def on_message(client, userdata, message):
    print("Latest Data Received:", message.payload.decode())

# MQTT Client Setup
client = mqtt.Client()
client.on_message = on_message

client.tls_set(ca_path, certfile=cert_path, keyfile=key_path, tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect(aws_endpoint, port, 60)

client.subscribe(topic)
client.loop_forever()
