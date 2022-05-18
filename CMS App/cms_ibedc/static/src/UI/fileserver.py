from psutil import process_iter

import http.server
import socketserver
import os
from signal import signal, SIGINT, SIGTERM
from sys import exit

PORT = 5000

# web_dir = os.path.join(os.path.dirname(__file__), 'web')
# os.chdir(web_dir)



def killPort():
    # print("Killed port")
    for proc in process_iter():
        print(dir(proc))
        for conns in proc.net_connections(kind='inet'):
            if conns.laddr[1] == PORT:
                proc.send_signal(SIGTERM) 
                continue

def handler(signal_received, frame):
    # Handle any cleanup here
    # print('SIGINT or CTRL-C detected. Exiting gracefully')
    killPort()
    
    
    exit(0)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    print('Running. Press CTRL-C to exit.')
    for i in range(1000000000):
        print(i)

