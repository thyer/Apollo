import sqlite3
conn = sqlite3.connect('content.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS articles (date text, topic text, title text, author text, link text)''')

c.execute("INSERT INTO articles VALUES('2015-12-17', 'INFOSEC', 'Social Engineering in the 21st Century', 'Brian Krebs', 'https://krebsonsecurity.com')")
conn.commit()