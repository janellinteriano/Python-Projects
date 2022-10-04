import sqlite3

conn = sqlite3.connect('mytest.db') # creates the database

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_tfiles(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_files TEXT)") # creates table if it does not exist
    conn.commit()

conn = sqlite3.connect('mytest.db') # connects to database 

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg') # lists file names

for x in fileList:
    if x.endswith('.txt'): # sorts through items to get files with ".txt"
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_tfiles (col_files) VALUES (?)", (x,))
            print(x)
            
conn.close()
