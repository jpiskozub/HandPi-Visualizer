import paho.mqtt.client as mqtt

mqttc=mqtt.Client(client_id='handpi')

broker= '192.168.0.101'
port=1883
topic='handpi'


mqttc.connect(broker,port)

try:
    while True:
        msg = (25905, 11909, 18324, 18330, 20017, 18343, 20499, 16829, 20308, 15385, 133.625, -1.4375, -161.0, 0.01, -0.01, 0.12, 0.001090830782496456, 0.002181661564992912, 0.001090830782496456, 42.75, -44.25, 30.25, -0.24, 3.16, -9.14)
        print (msg)
        mqttc.publish(topic,str(msg))
except KeyboardInterrupt:
    print('Interrupted!')