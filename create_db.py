import sqlite3


conn = sqlite3.connect("dati.db")
c = conn.cursor()


c.execute('''
CREATE TABLE IF NOT EXISTS rezultati(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          vards TEXT NOT NULL,
          klikski INTEGER NOT NULL,
          laiks INTEGER NOT NULL,
          datums INTEGER NOT NULL
)
''')


ieraksti = [
    ("Anonīmais", 1000, 1000, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01"),
    ("Anonīmais", 100, 100, "2020-01-01")
]


c.executemany('''
INSERT INTO rezultati (vards, klikski, laiks, datums)
VALUES (?, ?, ?, ?)
''', ieraksti)


conn.commit()
conn.close()

print("Izveidots!")