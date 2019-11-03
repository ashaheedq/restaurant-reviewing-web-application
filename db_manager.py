import sqlite3

# run the sql command and return data, and col names
def sql_command(command, param=''):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute(command, param)
    data = cur.fetchall()
    con.commit()
    con.close()
    col = [description[0] for description in cur.description]
    return data, col

# run sql command but don't return anything
def update_(command, param):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute(command, param)
    con.commit()
    con.close()
