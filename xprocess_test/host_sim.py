#!/usr/bin/env python3

import socketserver


class Handler(socketserver.BaseRequestHandler):
    """
    Need to implement handle method to exchange data
    with TCP client
    """

    def handle(self):
        while True:
            self.packet = self.request.recv(1024)

            if not self.packet:
                break

            self.parser(self.packet)

    def parser(self, data: bytes):
        for data_byte in data:
            print(data_byte)

        self.request.sendall(data)


class HostSim:
    def __init__(self):
        HOST = "127.0.0.1"
        PORT = 1234
        socketserver.TCPServer.allow_reuse_address = True
        self.tcp_server = socketserver.TCPServer((HOST, PORT), Handler)

        print("HostSim server running")
        self.tcp_server.serve_forever()

    def __del__(self):
        self.tcp_server.server_close()


if __name__ == "__main__":
    sim = HostSim()
