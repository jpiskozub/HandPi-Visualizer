import paho.mqtt.client as mqtt
import plotly.express as px


broker = '192.168.0.101'
port = 1883
topic = 'handpi'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
def on_message(client, userdata, message):
   print("Message Recieved: "+message.payload.decode())
    
def main():
    mqttc = mqtt.Client(client_id='visualizer')
    mqttc.connect(broker, port)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    
    mqttc.subscribe(topic)    
    mqttc.loop_forever()


    
    

if __name__ == '__main__':
    
    main()
