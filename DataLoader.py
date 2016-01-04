import sqlite3
import sys

conn = sqlite3.connect('content.db')

c = conn.cursor()

c.execute('''DROP TABLE articles''')
c.execute('''CREATE TABLE IF NOT EXISTS articles (date text, topic text, title text, author text, link text)''')

num_lines = sum(1 for line in open('example_articles.txt'))
if num_lines%5 != 0:
    conn.rollback()
    sys.exit("ERROR: Bad input file!")
with open('example_articles.txt') as f:
    for x in range(int(num_lines/5)):
        date = f.readline()
        topic = f.readline()
        title = f.readline()
        author = f.readline()
        link = f.readline()
        article = (date, topic, title, author, link)
        c.execute("INSERT INTO articles VALUES (?, ?, ?, ?, ?) ", article)

conn.commit()