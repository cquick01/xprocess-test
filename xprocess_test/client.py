#!/usr/bin/env python

import socket


class Client:

    def __init__(self, address, port=1234, timeout=30) -> None:
        self.BUFLEN = 64

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if timeout:
            self.sock.settimeout(timeout)

        self.sock.connect((address, port))

    def __del__(self) -> None:
        self.sock.close()

    def communicate(self, request: bytes) -> bytes:
        self.sock.send(request)

        response = self.sock.recv(self.BUFLEN)

        return response
