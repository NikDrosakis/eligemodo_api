from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import sqlite3
from typing import List
import json
import traceback
import sys
class QuestionBase(BaseModel):
 ID: int
 question: str
 choices: List[str]
 correct: str
 imageUrl: str




def create_table():
 conn = sqlite3.connect("main.sqlite")
 cursor = conn.cursor()
 table_exists = cursor.fetchone()
 if not table_exists:
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS questions 
  (ID integer primary key AUTOINCREMENT, 
  question varchar(200), 
  choices TEXT, 
  correct varchar(150), 
  imageUrl varchar(300)
  )
  """)
 return conn


def insert(questions: QuestionBase):
 conn = sqlite3.connect("main.sqlite")
 cursor = conn.cursor()
 question= questions.get("question", "")
 choices = json.dumps(questions.get("choices", {}))  # Convert dictionary to JSON string
 correct= questions.get("correct", "")
 imageUrl= questions.get("imageUrl", "")
 print(question,choices,correct,imageUrl)
 try:
  cursor.execute("INSERT INTO questions (question, choices, correct, imageUrl) VALUES (?, ?, ?, ?)",
                 (question, choices, correct, imageUrl))
  conn.commit()
 except sqlite3.Error as er:
     print('SQLite error: %s' % (' '.join(er.args)))
     print("Exception class is: ", er.__class__)
     print('SQLite traceback: ')
     exc_type, exc_value, exc_tb = sys.exc_info()
     print(traceback.format_exception(exc_type, exc_value, exc_tb))
 conn.close()
 return cursor.lastrowid


def update(id,question: QuestionBase):
 conn = sqlite3.connect("main.sqlite")
 cursor = conn.cursor()
 cursor.execute("UPDATE questions SET title=?, author=? WHERE id=?", (question.title, question.author,id))
 conn.commit()
 conn.close()
 return id


def delete(id):
 conn = sqlite3.connect("main.sqlite")
 cursor = conn.cursor()
 cursor.execute("DELETE FROM questions WHERE id=?", (id))
 conn.commit()
 conn.close()
 return id


def fetchall(table):
 conn = sqlite3.connect("main.sqlite")
 cur = conn.cursor()
 cur.execute("SELECT * FROM "+table)
 rows = cur.fetchall()
 conn.commit()
 conn.close()
 return rows


def fetch(id):
 conn = sqlite3.connect("main.sqlite")
 cur = conn.cursor()
 cur.execute("SELECT * FROM questions WHERE id=?",(id))
 rows = cur.fetchone()
 conn.commit()
 conn.close()
 return rows