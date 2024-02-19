from dotenv import load_dotenv
import mariadb
import sys
import os
from pydantic import BaseModel

load_dotenv()
class Book(BaseModel):
	title: str
	author: str


# Connect to MariaDB Platform
try:
	conn = mariadb.connect(
		user=os.getenv("MARIA_USER"),
		password=os.getenv("MARIA_PASSWORD"),
		host=os.getenv("MARIA_HOST"),
		port=os.getenv("MARIA_PORT"),
		database=os.getenv("MARIA_DB")
	)


except mariadb.Error as e:
	print(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)


def fetch(table_id):
	mariac = conn.cursor(prepared=True)
	mariac.execute("SELECT * FROM books WHERE id=?", (table_id,))
	row = mariac.fetchone()
	mariac.close()
	return row


def fetchall(table):
	mariac = conn.cursor(prepared=True)
	mariac.execute("SELECT * FROM " + table)
	row = mariac.fetchall()
	mariac.close()
	return row


def insert(q, args):
	mariac = conn.cursor(prepared=True)
	mariac.execute(q, args)
	mariac.commit()
	mariac.close()
	if mariac.lastrowid:
		return mariac.lastrowid
	else:
		return False


def update(q, args):
	mariac = conn.cursor(prepared=True)
	mariac.execute(q, args)
	mariac.commit()
	mariac.close()
	if mariac.lastrowid:
		return mariac.lastrowid
	else:
		return False


def delete(q, args):
	mariac = conn.cursor(prepared=True)
	mariac.execute(q, args)
	mariac.commit()
	mariac.close()
	if mariac.lastrowid:
		return mariac.lastrowid
	else:
		return False
