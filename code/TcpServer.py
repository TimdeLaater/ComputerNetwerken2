from contextlib import nullcontext
import socket
import sys

HOST = ''
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('# Socket created')

# Create socket on port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('# Bind failed. ')
    sys.exit()

print('# Socket bind complete')



# Start listening on socket
s.listen(10)
print('# Socket now listening')

# Wait for client
conn, addr = s.accept()
print('# Connected to ' + addr[0] + ':' + str(addr[1]))

#While connected

# Receive data from client
while True:
   
    data = conn.recv(1024)
    if not data: break
    line = data.decode('UTF-8')    # convert to string (Python 3 only)
    line = line.replace("\n","")   # remove newline character
    print("Ontvangen:", line )        
    conn.send(str.encode(input()))
conn.close()
s.close()