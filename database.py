import psycopg2
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "resumedb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resumes (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            experience TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(name, email, phone, skills, experience):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO resumes (name, email, phone, skills, experience)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, email, phone, ', '.join(skills), experience))
    conn.commit()
    conn.close()

def fetch_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resumes")
    data = cursor.fetchall()
    conn.close()
    return data
