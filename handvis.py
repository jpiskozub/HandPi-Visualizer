
import paho.mqtt.client as mqtt

import dearpygui.dearpygui as dpg


from queue import Queue

broker = '192.168.0.100'
port = 1883
topic = 'handpi'

mqttqueue = Queue()

ADC_channels=['P1_1', 'P1_2', 'P2_1', 'P2_2', 'P3_1', 'P3_2', 'P4_1', 'P4_2', 'P5_1', 'P5_2']
IMU_channels = ['Euler_x', 'Euler_y', 'Euler_z', 'Acc_x', 'Acc_y', 'Acc_z']

sign_types = ['static', 'dynamic']
sign_types_dict = {'a': sign_types[0],
                   'ą': sign_types[1],
                   'b': sign_types[0],
                   'c': sign_types[0],
                   'ć': sign_types[1],
                   'ch': sign_types[1],
                   'cz': sign_types[1],
                   'd': sign_types[1],
                   'e': sign_types[0],
                   'ę': sign_types[1],
                   'f': sign_types[1],
                   'g': sign_types[1],
                   'h': sign_types[1],
                   'i': sign_types[0],
                   'j': sign_types[1],
                   'k': sign_types[1],
                   'l': sign_types[0],
                   'ł': sign_types[1],
                   'm': sign_types[0],
                   'n': sign_types[0],
                   'ń': sign_types[1],
                   'o': sign_types[0],
                   'ó': sign_types[1],
                   'p': sign_types[0],
                   'r': sign_types[0],
                   'rz': sign_types[1],
                   's': sign_types[0],
                   'ś': sign_types[1],
                   'sz': sign_types[1],
                   't': sign_types[0],
                   'u': sign_types[0],
                   'w': sign_types[0],
                   'y': sign_types[0],
                   'z': sign_types[1],
                   'ź': sign_types[1],
                   'ż': sign_types[1]}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    
def on_message(client, userdata, message):
    
    mqttqueue.put(message.payload.decode('utf-8'))
    #dpg.render_dearpygui_frame()
  
def on_disconnect(client, userdata,rc=0):
    print("Disconnected result code "+str(rc))
    client.loop_stop()
    
def main():
    mqttc = mqtt.Client(client_id='visualizer')
    mqttc.connect(broker, port)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_disconnect = on_disconnect
    
    mqttc.subscribe(topic)    
    
    dpg.create_context()
    dpg.create_viewport(title='HandPi', width=600, height=200)
    
    with dpg.window(label="Flex sensors"):
        with dpg.plot(label="Bar Series", height=-1, width=-1):
            dpg.add_plot_axis(dpg.mvXAxis, label="Sensor", no_gridlines=False)
            dpg.set_axis_ticks(dpg.last_item(), (("P1_1", 11), ("P1_2", 21), ("P2_1", 31), ("P2_2", 42), ("P3_1",51), ("P3_2",61), ("P4_1",71), ("P4_2",81), ("P5_1",91), ("P5_2", 101)))
            dpg.add_plot_axis(dpg.mvYAxis, label="Value", tag="yaxis_tag")
            dpg.add_bar_series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], weight=1, parent="yaxis_tag", tag = 'vals')

        
    dpg.show_metrics()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    mqttc.loop_start()
 

    
    while dpg.is_dearpygui_running():
        try:
            
            
            
            vals = eval(mqttqueue.get())
                
            dpg.set_value('vals', [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], vals[0:9]])
            
            print(vals)

            dpg.render_dearpygui_frame()
            
        except KeyboardInterrupt:
            print ('Interrupted')
            mqttc.loop_stop(force=True)
    else:
        mqttc.loop_stop()
        mqttc.disconnect()
           
    dpg.destroy_context()
    
    

if __name__ == '__main__':
    
    main()
