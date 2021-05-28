from tkinter import *
import sqlite3
conn = sqlite3.connect(("registration.db"))
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS signup_form(
            first_name text,
            last_name text,
            user_name text,
            new_password text,
            postal_number integer,
            address_name text,
            contact_number integer


)""")
conn.commit()
conn.close()

def forget():
    conn = sqlite3.connect()
    c = conn.cursor()
    # c.execute(""""""")