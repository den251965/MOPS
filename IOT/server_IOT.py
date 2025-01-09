import socket

import threading
# Пул потоков для нашего сервера
class ClientThread(threading.Thread): 
 
    def __init__(self, conn, details): 
        self.conn = conn
        self.details = details
        threading.Thread.__init__ ( self )

        print (f"[+] New server socket thread started for \t{HOST} : \t{PORT}")
        self.conn.sendall("You connected!".encode('utf-8')) 

    def run(self): 
        while True : 
            json_data = self.conn.recv(1024)
            data = json_data.decode('utf-8')
            if data == 'end':
                print('end') # окончание работы сосединения
                break
            if data != '':
                # js = json.loads(data)
                # if js['status'] == 0 :
                #     print(data)  # вывод данных по статусу  
                print(data)  # то что отправляем в монгу и брокер  


if __name__ == '__main__':
    s = socket.socket()
    HOST = "localhost"
    PORT = 8080 
    couter = 150 # Кол-во соединений
    s.bind((HOST, PORT))
    s.listen(couter)

    p = True
    while p == True:  
        (conn, details) = s.accept() 
        ClientThread(conn, details).start()  