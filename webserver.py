#
# Pthon 3 simple server
#
# Alternatives: 
# $ python3 -m http.server 8080
# $ python3 -m http.server 8080 --bind 127.0.0.1
# $ python3 -m http.server 8080 -directory /where-my-files-are
#

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()