import socket
import sys, os

def irccat(msg, host='localhost', port=5000):
    s = socket.socket()
    s.settimeout(1)
    s.connect((host, port))
    s.send(msg + "\n")
    s.close()

class SimpleClient:
    def __init__(self, host="localhost", port=5000):
        self.host = host
        self.port = port
    def send(self, msg):
        return irccat(msg, host, port)

class PersistentClient:
    def __init__(self, host="localhost", port=5000):
        self.socket = None
        self.host = host
        self.port = port
    def _connect(self):
        s = socket.socket()
        s.settimeout(1)
        s.connect((self.host, self.port))
        self.socket = s

    def send(self, msg):
        try :
            self.socket.send(msg + "\n")
        except:
            self._connect()
            self.socket.send(msg + "\n")

def main():
    msg = ' '.join(sys.argv[1:])
    irccat(msg)
