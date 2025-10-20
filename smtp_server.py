import socket
import threading

class SMTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"SMTP server listening on {host}:{port}")

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        try:
            client_socket.send(b"220 localhost SMTP server ready\r\n")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8', errors='ignore').strip()
                print("Received:", message)
                if message.upper().startswith("QUIT"):
                    client_socket.send(b"221 Bye\r\n")
                    break
                elif message.upper().startswith("DATA"):
                    client_socket.send(b"354 End data with <CR><LF>.<CR><LF>\r\n")
                    # Read email data until we see <CRLF>.<CRLF>
                    email_data = b""
                    while True:
                        chunk = client_socket.recv(1024)
                        email_data += chunk
                        if email_data.endswith(b"\r\n.\r\n"):
                            break
                    print("Email received:", email_data.decode('utf-8', errors='ignore'))
                    client_socket.send(b"250 OK: Message accepted for delivery\r\n")
                else:
                    client_socket.send(b"250 OK\r\n")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

if __name__ == '__main__':
    server = SMTPServer('localhost', 1025)
    server.start()