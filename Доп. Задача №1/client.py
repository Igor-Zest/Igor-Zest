import socket

def start_client():
    client_1 = socket.socket() # Создается сокет аналогично серверу


    client_1.connect(('localHost', 5050)) # аналогично указываем хост и порт

    with open('F:/TEST.txt','rb') as file:

        data = file.read(1048576)


        while True:

            client_1.send(data)
            data = file.read(1048576)

            if not data:
                break
            
    print("Файл отправлен")


if __name__ == "__main__":  # - Проверка условия
    start_client()