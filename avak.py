from tkinter import *
import paho.mqtt.client as mqtt
from tkinter import colorchooser
last_received_messages = {}
initialized = False
current_color = None  # Добавлено отслеживание текущего цвета

def on_message(client, userdata, msg):
    global initialized, current_color
    p = msg.payload.decode('utf-8')

    # Проверяем, является ли сообщение таким же, как предыдущее по данной теме
    if initialized and msg.topic in last_received_messages and last_received_messages[msg.topic] == p:
        return

    last_received_messages[msg.topic] = p
    if msg.topic == "lamp/brightness":
        br.set(int(p))
    elif msg.topic == "lamp/rgb":
        rgb = hex_to_rgb(p)
        if current_color != rgb:
            er.delete(0, END)
            er.insert(0, str(rgb[0]))
            eg.delete(0, END)
            eg.insert(0, str(rgb[1]))
            eb.delete(0, END)
            eb.insert(0, str(rgb[2]))
            color_box.config(bg=conv(rgb))
            current_color = rgb

        send(rgb[0], rgb[1], rgb[2], br.get())
    elif msg.topic == "lamp/light-sensor":
        # Обработка данных от сенсора освещенности
        light_intensity = float(p)
        if light_intensity >= 50:
            # Включить лампу, так как уровень освещенности высок
            send(255, 255, 255, br.get())
        else:
            # Выключить лампу, так как уровень освещенности низок
            send(0, 0, 0, br.get())

    initialized = True


def on_connect(client, userdata, flags, rc):
    client.subscribe("lamp/+")


def send_color():
    color = colorchooser.askcolor()
    if color[1] is not None:
        r, g, b = [int(c) for c in color[0]]
        er.delete(0, END)
        er.insert(0, str(r))
        eg.delete(0, END)
        eg.insert(0, str(g))
        eb.delete(0, END)
        eb.insert(0, str(b))
        color_box.config(bg=color[1])
        send(r, g, b, br.get())


def send(r, g, b, br_val):
    client.publish("lamp/rgb", conv((r, g, b)))
    client.publish("lamp/brightness", br_val)


def conv(rgb):
    return "#{:02x}{:02x}{:02x}".format(*map(int, rgb))


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


r = Tk()
r.title("Control")
l_b = Label(r, text="Яркость:")
l_b.pack()

br = Scale(r, from_=0, to=100, orient=HORIZONTAL)
br.pack()
er = Entry(r)
eg = Entry(r)
eb = Entry(r)
c = Canvas(r, width=50, height=10)
c.pack()
color_box = Label(r, bg="white", width=10, height=3)
color_box.pack()

b_color = Button(r, text="Выбрать цвет", command=send_color)
b_color.pack()

c = Canvas(r, width=50, height=10)
c.pack()
b_u = Button(r, text="Обновить", command=lambda: send(int(er.get()), int(eg.get()), int(eb.get()), br.get()))
b_u.pack()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)
client.loop_start()

r.mainloop()