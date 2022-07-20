#!/usr/bin/env python3

import threading
import socket
import argparse
import os

class Server(threading.Thread):

    def __init__(self, host, port): # Constructor
        super().__init__()   # Child of class
        self.connections = [] # self
        self.host = host
        self.port = port

    def run(self):
        pass