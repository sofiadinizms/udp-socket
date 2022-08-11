import threading
import socket

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 12606))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input("user: ")
    print("\nConectado")

    thread1 = threading.Thread(target=receiveMessage, args=[client])
    thread2 = threading.Thread(target=sendMessage, args=[client,username])

    thread1.start()
    thread2.start()

def receiveMessage(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            print(message+'\n')
        except:
            print("\nnao deu pra ficar conectado no servidor. sorry\n Pressione enter pra continuar\n")
            client.close()
            break
            

def sendMessage(client,username):
    while True:
        try:
            message = input("\n")
            client.send(f'<{username}> {message}'.encode('utf-8'))
        except:
            return
main()