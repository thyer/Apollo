import sqlite3
import sys

conn = sqlite3.connect('content.db')

c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS articles''')
c.execute('''CREATE TABLE IF NOT EXISTS articles (date text, topic text, title text, author text, link text)''')

num_lines = sum(1 for line in open('example_articles.txt'))
if num_lines%5 != 0:
    conn.rollback()
    sys.exit("ERROR: Bad input file!")
with open('example_articles.txt') as f:
    for x in range(int(num_lines/5)):
        date = f.readline().strip()
        topic = f.readline().strip()
        title = f.readline().strip()
        author = f.readline().strip()
        link = f.readline().strip()
        article = (date, topic, title, author, link)
        c.execute("INSERT INTO articles VALUES (?, ?, ?, ?, ?) ", article)

conn.commit()