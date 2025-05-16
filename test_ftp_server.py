from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Set up an authorizer (user credentials)
authorizer = DummyAuthorizer()
authorizer.add_user("123456", "admin", ".", perm="elradfmwMT")  # FTP root = current directory

# FTP handler with login auth
handler = FTPHandler
handler.authorizer = authorizer

# Start FTP server on localhost:21
server = FTPServer(("127.0.0.1", 21), handler)
print("[*] FTP test server running at 127.0.0.1:21 (user: admin / pass: admin )")
server.serve_forever()
