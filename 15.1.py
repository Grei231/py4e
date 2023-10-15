import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fh = open("mbox-short.txt")

email_counts = {}

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')[1]
    email_counts[domain] = email_counts.get(domain, 0) + 1

# Move the commit operation outside of the loop
for domain, count in email_counts.items():
    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (domain, count))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
