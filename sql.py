import sqlite3 as sql

boglanish = sql.connect("susys.db")

malumot = boglanish.cursor()

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Odam(
    isim TEXT,
    famila TEXT,
    yosh INTEGER
)

""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Student(
    isim TEXT,
    famila TEXT
    yosh INTEGER
    kurs INTEGER
)
""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Bekorshilar(
    isim TEXT,
    famila TEXT,
    yosh INTEGER,
    ishi TEXT
)

""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Sportshilar(
    isim TEXT,
    famila TEXT,
    yosh INTEGER,
    ishi TEXT
)

""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Pythonshilar(
    isim TEXT,
    famila TEXT,
    yosh INTEGER,
    ishi TEXT
)

""")

malumot.execute(""" 
CREATE TABLE IF NOT EXISTS Qaydavshi(
    isim TEXT,
    famila TEXT,
    yosh INTEGER,
    ishi TEXT
)

""")

