
import paho.mqtt.client as mqtt

import dearpygui.dearpygui as dpg

import plotly.express as px

from queue import Queue

broker = '192.168.0.100'
port = 1883
topic = 'handpi'

mqttqueue = Queue()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    
def on_message(client, userdata, message):
    mqttqueue.put(message.payload.decode('utf-8'))
  
def on_disconnect(client, userdata,rc=0):
    print("DisConnected result code "+str(rc))
    client.loop_stop()
    
def main():
    mqttc = mqtt.Client(client_id='visualizer')
    mqttc.connect(broker, port)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    
    mqttc.subscribe(topic)    
    
    dpg.create_context()
    dpg.create_viewport(title='Custom Title', width=600, height=200)
    
    with dpg.window(label="Example Window"):
        dpg.add_text("Hello, world")
        
   
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

   
    while dpg.is_dearpygui_running():
        try:
            mqttc.loop_start()
            dpg.add_text(str(mqttqueue.get()))

            dpg.render_dearpygui_frame()
            
        except KeyboardInterrupt:
            print ('Interrupted')
            mqttc.loop_stop()
            mqttc.disconnect()
    else:
        mqttc.loop_stop()
        mqttc.disconnect()
           

    
    

if __name__ == '__main__':
    
    main()
