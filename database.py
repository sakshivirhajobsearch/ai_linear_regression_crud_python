import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dataset (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    x_value REAL NOT NULL,
                    y_value REAL NOT NULL
                )''')
    conn.commit()
    conn.close()

def get_all_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM dataset")
    rows = c.fetchall()
    conn.close()
    return rows

def add_data(x, y):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO dataset (x_value, y_value) VALUES (?, ?)", (x, y))
    conn.commit()
    conn.close()

def get_data_by_id(record_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM dataset WHERE id=?", (record_id,))
    row = c.fetchone()
    conn.close()
    return row

def update_data(record_id, x, y):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("UPDATE dataset SET x_value=?, y_value=? WHERE id=?", (x, y, record_id))
    conn.commit()
    conn.close()

def delete_data(record_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM dataset WHERE id=?", (record_id,))
    conn.commit()
    conn.close()
