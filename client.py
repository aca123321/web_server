import socket
import threading

def request():
  s = socket.socket()
  s.connect(("localhost", 8080))

  s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
  print(str(s.recv(4096)))

threads = []
for _ in range(10):
  thread = threading.Thread(target=request, args=())
  thread.start()
  threads.append(thread)

for t in threads:
    t.join()
