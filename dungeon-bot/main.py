import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('dungeons.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS account(user_name TEXT, date_joined TEXT, value INTEGER)")

def dynamic_data_entry():
    uname = input("Please choose a username: ")
    date = str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d"))
    value = 0

    c.execute("INSERT INTO account (user_name, date_joined, value) VALUES (?, ?, ?)", (uname, date, value))
    print("DEBUG: account registered" + str(date))
    conn.commit()

create_table()
dynamic_data_entry()
time.sleep(1)

c.close()
conn.close()

