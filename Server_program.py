'''what is port forwarding'''

import socket as s
from threading import Thread


HOST = ''
PORT = 5465


class ASPthreading(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        self.conn.sendall("HI YOU ARE CONNECTED TO THE SERVER \n".encode())
        recv_data = conn.recv(1024)
        while recv_data:
            print("{} : ".format(self.addr[0]) + recv_data.decode(), end='')
            recv_data = conn.recv(1024)


sck = s.socket(s.AF_INET, s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
sck.bind((HOST, PORT))
sck.listen()
while True:
    print("Waiting for a connection")
    conn, addr = sck.accept()
    print("Connection received from IP {} : BACK PORT {}".format(addr[0], addr[1]))
    ASPthreading(conn, addr).start()
