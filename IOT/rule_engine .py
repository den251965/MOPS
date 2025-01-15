import json
from pymongo import  MongoClient
import math
import pika
import array

id_device = 51
#мгновенное прави
light_rule = 3 #мгновенное правило берем пакеты равные 3( 25% примерно)
#Обработка длящегося правила
long_rule = 5 #берем пакеты равные 5( 75% примерно)
count_long_rule = 10 # как только подряд приходит 10 пакетов

#RabbitMQ
delitel = 10
queue_br = 'rule_control_'+str(math.ceil(id_device/delitel))
connect_rabbitmq = pika.BlockingConnection(pika.ConnectionParameters('localhost'))# Устанавливаем соединение с сервером RabbitMQ
channel = connect_rabbitmq.channel()
channel.queue_declare(queue = queue_br)

#mongo db
connect_db = MongoClient('localhost', 27017)
db = connect_db['mopsdb']
collection = db['my_light_engine']
collection_2 = db['my_long_engine']

arr =[]

def callback(ch, method, properties, data):
    print(" [x] Received %r" % data)
    js = json.loads(data)
    if js['id_device'] == id_device :
        #Обработка мгновенно правила
        if js['rule'] == light_rule :
            collection.insert_one(js)
        #Обработка длящегося правила
        if js['rule'] == long_rule :
            arr.append(js)
            if (len(arr)) == count_long_rule :
               collection_2.insert_many(arr) 
               arr.clear
        else :
            arr.clear

channel.basic_consume(queue = queue_br, on_message_callback = callback, auto_ack = True)
channel.start_consuming()
   