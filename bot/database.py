import sqlite3
import os
from contextlib import contextmanager

DB_PATH = os.getenv("DB_PATH", "reports.db")

@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """Инициализация структуры БД"""
    with get_connection() as conn:
        cursor = conn.cursor()
        # Создание таблиц
        cursor.executescript('''
            CREATE TABLE IF NOT EXISTS employees (
                user_id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                position TEXT DEFAULT 'Рабочий'
            );
            
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                text TEXT,
                photo_path TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()