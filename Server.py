import http.server
import socketserver

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()



















































