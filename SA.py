import classify
import base64

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = 'class.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Music_to_video'
IDF_list = ['Sentence_I']
ODF_list = ['MP3_O']
device_id = '31283301712240019' #if None, device_id = MAC address
device_name = 'music_genre'
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

have_recieved = [0]
filename = '/home/zyj/Module-class/damo-vilab/output/test.mp4'

def Sentence_I():
    if classify.classname == "" : return None
    return_string = classify.generate_sentence()
    classify.classname = ""
    return return_string

def MP3_O(data:list):
    classify.classname = classify.music_genre(data)
