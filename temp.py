import random
import time
import paho.mqtt.client as mqtt

# Paramètres du serveur MQTT
broker = "broker.hivemq.com"  # Utilisation d'un serveur MQTT public
port = 1883
topic_temp = "maison/salon/temp"
topic_hum = "maison/salon/hum"

# Callback quand la connexion MQTT est établie
def on_connect(client, userdata, flags, rc):
    print("Connecté au serveur MQTT avec le code de retour : " + str(rc))

# Configuration du client MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, port, 60)

# Boucle de publication des données simulées
while True:
    # Générer des valeurs simulées pour la température et l'humidité
    temperature = round(random.uniform(20.0, 30.0), 2)  # Température entre 20 et 30°C
    humidity = round(random.uniform(40.0, 60.0), 2)  # Humidité entre 40% et 60%

    # Publier les données de température et d'humidité sur MQTT
    client.publish(topic_temp, str(temperature))
    client.publish(topic_hum, str(humidity))
    
    print(f"Température: {temperature}°C, Humidité: {humidity}%")
    
    # Attendre avant de publier de nouvelles données
    time.sleep(5)
