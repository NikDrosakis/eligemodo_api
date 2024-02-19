from typing import Union
from pydantic import BaseModel
import sqlite3

class Book(BaseModel):
 title: str
 author: str
#create_table()

def create_connection():
 conn = sqlite3.connect("books.db")
 return conn
def create_table():
 conn = create_connection()
 cursor = conn.cursor()
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS books (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL,
 author TEXT NOT NULL
 )
 """)
def insert(book: Book):
 conn = create_connection()
 cursor = conn.cursor()
 cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book.title, book.author))
 conn.commit()
 conn.close()
 return cursor.lastrowid

def update(id,book: Book):
 conn = create_connection()
 cursor = conn.cursor()
 cursor.execute("UPDATE books SET title=?, author=? WHERE id=?", (book.title, book.author,id))
 conn.commit()
 conn.close()
 return id


def delete(id):
 conn = create_connection()
 cursor = conn.cursor()
 cursor.execute("DELETE FROM books WHERE id=?", (id))
 conn.commit()
 conn.close()
 return id


def fetchall():
 conn = create_connection()
 cur = conn.cursor()
 cur.execute("SELECT * FROM books")
 rows = cur.fetchall()
 conn.commit()
 conn.close()
 return rows


def fetch(id):
 conn = create_connection()
 cur = conn.cursor()
 cur.execute("SELECT * FROM books WHERE id=?",(id))
 rows = cur.fetchone()
 conn.commit()
 conn.close()
 return rows

