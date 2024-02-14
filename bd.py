import paho.mqtt.client as mqtt
import sqlite3
import datetime

conn = sqlite3.connect('mqtt_logs.db')
cursor = conn.cursor()


def log_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    print(f"Received message on topic {message.topic}: {payload}")

    timestamp = datetime.datetime.now().isoformat()
    insert_query = "INSERT INTO mqtt_logs (timestamp, topic, message) VALUES (?, ?, ?)"
    record_data = (timestamp, message.topic, payload)
    cursor.execute(insert_query, record_data)
    conn.commit()


def establish_connection(client, userdata, flags, rc):
    cursor.execute('''CREATE TABLE IF NOT EXISTS mqtt_logs
                      (timestamp TEXT, topic TEXT, message TEXT)''')
    print("Connected with result code " + str(rc))
    client.subscribe("lamp/+")


mqtt_client = mqtt.Client()
mqtt_client.on_connect = establish_connection
mqtt_client.on_message = log_message
mqtt_client.connect("127.0.0.1", 1883, 60)

mqtt_client.loop_forever()