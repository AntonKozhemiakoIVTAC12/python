import paho.mqtt.client as mqtt
import json
import sqlite3


# Функция для обработки сообщений MQTT
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload)
        if all(key in data for key in ['red', 'green', 'blue', 'time']):
            #print(f"RGB:\n\tred: {data['red']}\n\tblue: {data['blue']}\n\tgreen: {data['green']}\ntime: {data['time']}")
            connection = sqlite3.connect('colors.db')
            cursor = connection.cursor()

            cursor.execute('INSERT INTO Colors (red, green, blue, time) VALUES (?, ?, ?, ?)',
                           (data['red'], data['green'], data['blue'], data['time']))
            connection.commit()
            connection.close()

        elif 'light' in data:
            print(f"light: {data['light']}\ntime: {data['time']}")
            connection = sqlite3.connect('light.db')
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Light (light, time) VALUES (?, ?)',
                           (data['light'], data['time']))
            connection.commit()
            connection.close()
        else:
            print("Invalid data format")



    except Exception as e:
        print(f"An error occurred: {e}")


connection = sqlite3.connect('colors.db')
cursor = connection.cursor()
query_colors = """ 
CREATE TABLE IF NOT EXISTS Colors 

(id INTEGER PRIMARY KEY,  

red INTEGER NOT NULL, 

green INTEGER NOT NULL,  

blue INTEGER NOT NULL, 

time TEXT NOT NULL) 

"""
cursor.execute(query_colors)
connection.commit()
connection.close()
connection = sqlite3.connect('light.db')
cursor = connection.cursor()
query_light = """ 

CREATE TABLE IF NOT EXISTS Light 

(id INTEGER PRIMARY KEY, 

light INTEGER NOT NULL, 

time TEXT NOT NULL) 

"""
cursor.execute(query_light)
connection.commit()
connection.close()
# Создаем клиент MQTT
client = mqtt.Client()
# Устанавливаем обработчик сообщений
client.on_message = on_message
# Подключаемся к брокеру MQTT
client.connect("127.0.0.1", 1883)
# Подписываемся, откуда будут приходить данные
client.subscribe("lab1")
# Запускаем бесконечный цикл для обработки сообщений
client.loop_forever()
