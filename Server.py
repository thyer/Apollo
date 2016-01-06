from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sqlite3

hostName = ""
hostPort = 80
conn = sqlite3.connect('content.db')

c = conn.cursor()


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        print(self.path)
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.serve_index()
        elif self.path == '/favicon.ico':
            self.send_response(200)
            self.send_header("Content-type", "image/ico")
            self.end_headers()
            self.serve_fav_icon()
        elif self.path == '/apollo.png':
            self.send_response(200)
            self.send_header("Content-type", "image/ico")
            self.end_headers()
            self.serve_brand()
        elif "/query/" in self.path:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.serve_query(self.path.replace("/query/", ""))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<p>Invalid path: %s</p>" % self.path, "utf-8"))

    def serve_index(self):
        with open("index.html") as f:
            for line in f:
                self.wfile.write(bytes(line, "utf-8"))

    def serve_fav_icon(self):
        with open("favicon.ico") as f:
            for line in f:
                self.wfile.write(bytes(line, "utf-8"))

    def serve_brand(self):
        with open("apollo.png") as f:
            for line in f:
                self.wfile.write(bytes(line, "utf-8"))

    def serve_query(self, topic):
        for row in c.execute("SELECT * FROM articles WHERE topic LIKE \'%s\'" % topic):
            index = 0
            dict = {}
            for item in row:
                if index % 5 == 0:
                    index = 0
                index += 1
                if index == 1:
                    dict['date'] = item
                elif index == 3:
                    dict['title'] = item
                elif index == 4:
                    dict['author'] = item
                elif index == 5:
                    dict['link'] = item
            self.wfile.write(bytes("<div id=\"card\"><hr><h3>" + dict.get('title') + "</h3>", "utf-8"))
            self.wfile.write(bytes("Author: " + dict.get('author') + "<br>", "utf-8"))
            self.wfile.write(bytes("Published: " + dict.get('date') + "<br>", "utf-8"))
            self.wfile.write(bytes("URL: <a href=\"" + dict.get('link') + "\">link</a><hr></div>", "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))