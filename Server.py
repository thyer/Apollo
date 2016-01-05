import http.server

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler

httpd = http.server.HTTPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()