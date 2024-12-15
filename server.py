import socket
import time
import threading

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8080))

s.listen(10) # try `ab -c 10 -n 100 http://127.0.0.1:8080/` and then `ab -c 20 -n 100 http://127.0.0.1:8080/`

message = "Hello World!\n"

http_response = f"""HTTP/1.1 200 OK\r
Content-Length: {len(message)}\r\n
{message}\r\n""".encode('utf-8')


def respond(conn):
  time.sleep(0.1) # in second(s)
  print(str(conn.recv(4096)))

  conn.send(http_response)

  conn.shutdown(socket.SHUT_RDWR)
  conn.close()

while True:
  try:
    # waiting for connection
    conn, address = s.accept()
    thread = threading.Thread(target=respond, args=(conn,))
    thread.start()
  except KeyboardInterrupt:
    print("interrupted")
    s.close()