import threading
import socket

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 12606))
        server.listen()
    except:
        return print('nao deu pra iniciar o servidor')
    
    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()


def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg,client)
        
        except:
            deleteClient(client)
            break

def broadcast(msg, client):
    for client_item in clients:
        if client_item != client:
            try:
                client_item.send(msg)
            except:
                deleteClient(client_item)
                
                
def deleteClient(client):
    clients.remove(client)

main()