import asyncio
import itertools
import json
import time
import websockets




async def handler(websocket,d):


    try:
        # Play the move.
        event = {"status":True}
        for i in range(30):
            time.sleep(10)
            await websocket.send(json.dumps(event))
    except Exception as exc:
        # Send an "error" event if the move was illegal.
        print(exc)
        
async def main():
    async with websockets.serve(handler, "localhost", 8000):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
    
    

# import socket

# sock = socket.socket()
# sock.bind(('', 8000))
# sock.listen(5)
# while True:
#     client, adress = sock.accept()



#     client.send('HTTP/1.0 200 OK\r\n'.encode())
#     client.send("Access-Control-Allow-Credentials: true\r\n".encode())
#     # client.send("Access-Control-Allow-Origin: http://127.0.0.1:8069\r\n".encode())
#     client.send("Content-Type: text/html\r\n".encode())
#     client.send("Access-Control-Allow-Origin: http://127.0.0.1:8069\r\n\r\n".encode())
#     client.send('<html><body><h1>Hello World</body></html>'.encode())
    # client.close()


    # sock.close()
    
    
    
    
    
    
    
    
    
    
    

# import socket, json

# sample_response = json.dumps({"status": True,"message":"A new server event occured"})
# # Define socket host and port
# SERVER_HOST = '0.0.0.0'
# SERVER_PORT = 8000

# # Create socket
# # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# with socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_socket.bind((SERVER_HOST, SERVER_PORT))
#     server_socket.listen(1)
#     print('Listening on port %s ...' % SERVER_PORT)

#     while True:    
#         # Wait for client connections
#         client_connection, client_address = server_socket.accept()

#         # Get the client request
#         request = client_connection.recv(1024).decode()
#         print(request)

#         # Send HTTP response
#         res = r'''HTTP/1.0 200 OK
#                 Content-Type: text/plain
#                 Access-Control-Allow-Origin: http://127.0.0.1:8069
#                 Access-Control-Allow-Headers: Authorization, Content-Type
#                 Access-Control-Allow-Methods', 'GET'
#                 Hello, world!

#                 '''
#         response = f'{res}\n\n{sample_response}'
#         client_connection.send(response.encode())
#         client_connection.send("Access-Control-Allow-Origin: *\r\n\r\n".encode())
#         client_connection.send("Content-Type: text/html\r\n\r\n".encode())
        
#         client_connection.send("Access-Control-Allow-Headers: Authorization, Content-Type\r\n\r\n".encode())
#         client_connection.close()

#     # Close socket
#     server_socket.close()

