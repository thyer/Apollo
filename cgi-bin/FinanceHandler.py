#!/usr/bin/env python
import cgitb
import sqlite3

cgitb.enable()
conn = sqlite3.connect('content.db')
c = conn.cursor()

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
for row in c.execute('SELECT * FROM articles WHERE topic LIKE \'FINANCE\''):
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
    print("<hr>")
    print("<H3>" + dict.get('title') + "</H3>")
    print("Author: " + dict.get('author') + "<br>")
    print("Published: " + dict.get('date') + "<br>")
    print("URL: <a href=\"" + dict.get('link') + "\">link</a>")
    print("</hr>")