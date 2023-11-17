import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 8080

def receber_mensagens(s):
    while True:
        data = s.recv(1024)

        if not data:
            break

        print(data.decode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    receber_mensagens_thread = threading.Thread(target=receber_mensagens, args=(s,))
    receber_mensagens_thread.start()

    print("Conectado ao chat. Digite seu nickname.")
    nickname = input("Nickname: ")

    print(f"Seja bem vindo(a) ao chat, {nickname}!")
    s.send(f"{nickname} entrou no chat!".encode("utf-8"))

    while True:
        mensagem = input()
        s.send(f"{nickname}: {mensagem}".encode("utf-8"))

        time.sleep(0.1)
