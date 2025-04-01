import paho.mqtt.client as mqtt

# Paramètres du serveur MQTT
broker = "broker.hivemq.com"  # Serveur MQTT public
port = 1883
topic_temp = "maison/salon/temp"
topic_hum = "maison/salon/hum"

# Callback quand un message est reçu
def on_message(client, userdata, msg):
    print(f"Message reçu sur {msg.topic} : {msg.payload.decode()}")

# Configuration du client MQTT
client = mqtt.Client()
client.on_message = on_message

# Connexion au serveur MQTT
client.connect(broker, port, 60)

# S'abonner aux sujets
client.subscribe(topic_temp)
client.subscribe(topic_hum)

# Boucle infinie pour recevoir les messages
client.loop_forever()
