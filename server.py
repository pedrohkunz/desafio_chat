import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

clientes = {}

def conectar_cliente(conn, addr):
    identificador_cliente = addr

    clientes[identificador_cliente] = conn

    try:
        while True:
            data = conn.recv(1024)

            if not data:
                break

            print(f"Recebido de {identificador_cliente}: {data.decode('utf-8')}")

            for cliente_id, cliente_conn in clientes.items():
                if cliente_id != identificador_cliente:
                    try:
                        cliente_conn.sendall(data)
                    except Exception as e:
                        print(f"Erro ao enviar mensagem para {cliente_id}: {e}")

    finally:
        del clientes[identificador_cliente]
        print(f"Conexão de {identificador_cliente} fechada.")
        conn.close()
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("Servidor iniciado!")

    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=conectar_cliente, args=(conn, addr))
        client_thread.start()
