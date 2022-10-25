import sqlite3

conn = sqlite3.connect('setting.db')

c = conn.cursor()

c.execute("""CREATE TABLE Information (
        id integer PRIMARY KEY AUTOINCREMENT,
        sensor text,
        device text,
        address text,
        location text,
        low_range text,
        high_range text,
        signal text,
        unit text
        )
""")
conn.commit()
conn.close()
