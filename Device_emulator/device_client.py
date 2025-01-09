import random
import json
import socket
import time

import threading

id = 0 # 

def run_device(): 

    lon = random.random() * 50
    lat = random.random() * 100
    rule = 1

    # наш json зашил внутрь питона
    data = {
       "id": id,
       "lon": lon,
       "lat": lat,
       "rule": rule
    }

    # Наш сервер к которому коннтектимся
    s = socket.socket()
    HOST = "localhost"
    PORT = 8080
    s.connect((HOST, PORT))

    data_serv = s.recv(1024)  # Получаем приветствие.
    print(f"Server Mess : \n\t{data_serv.decode('utf-8')}")

    new_ran = 0 # рандом для долготы и широты раз в 1000 чуть увеличиваем
    while True :
    
        json_data = json.dumps(data)
        # print(json_data) # вывод сообщения которое отправляем
        s.sendall(json_data.encode())

        # Подменяем статус
        if random.randint(0, 100) > 75 :
            rule = 3 # Если больше 90 помечаем 0 не корректным
        else :
            rule = 5 # Если не больше то  1 типа валидное
        data['rule'] = rule

        # Редактирование GPS
        new_ran += 0 
        if new_ran == 1000 :
            new_ran = 0
            lon += 0.00001
            lat += 0.00001
            data['lon'] = lon
            data['lat'] = lat
        time.sleep(1) # Раз в секунду шлем мессаджи
    # Завершение работы
    # s.sendall('end'.encode())

if __name__ == '__main__':
    print ("devices emulator started")
    for i in range(100):
        id += 1
        threading.Thread(target = run_device).start()
    
    
