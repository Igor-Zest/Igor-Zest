import socket

def start_server():
    server_1 = socket.socket() #socket.AF_INET, socket.SOCK_STREAM
    #Создание сокета. AF_INET - указание на использование сетевого протокола IPv4
    # SOCK_STREAM - определяет использование ТСР (он в свою очередь обеспечивает надежную передачу данных)


    server_1.bind(('localHost', 5050))    #((host, port)) -  пустой хост подходит для всех интерфейсов
    # сокет.bind - привязывает сокет к установленному ((хосту, и порту))


    server_1.listen(1)
    # Просмотр подключений. Аргумент указанный в скобках говорит о кол-ве ожидаемых 1 подключений


    print("Подключение прошло успешно")


 
    conn, address_c = server_1.accept() 
    # conn - возвращается новый сокет, address_c - адрес клиента, 
    #accept - принимает данные, так же блокирует выполнение, пока не произойдет подключение
    # После подключения возвращается новый сокет для соединения с клиентом в address_c  


    print(f"Подключены к клиенту: {address_c} ")

    with conn, open('F:/Python/TEST.txt','wb') as file: # wb - открытие файла в двоичном режиме
        data = conn.recv(1048576) # Принимаем данные 


        while True:             
            data = conn.recv(1048576)        # цикл записи данных, пока они есть

            if not data:
                break
            file.write(data)
            

    print('Файл: TEST.txt успешно получен')

    conn.close() # Закрытие потока

if __name__ == "__main__":  # - Проверка условия
    start_server()
    


