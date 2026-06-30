import sqlite3

def init_db():
    """Connects to SQLite and creates the movies table if it doesn't exist."""
    conn = sqlite3.connect("movies_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT,
            year INTEGER,
            genre TEXT
        )
        """)
    conn.commit()
    conn.close()

def get_all_movies():
    """Returns all movies from the database."""
    conn = sqlite3.connect("movies_database.db")
    cursor = conn.cursor()
    rows = cursor.fetchall()
    conn.close()
    return rows

def refresh_table(self):
    """Fetches movies from database and displays them in the table."""
    self.movie_table.delete(*self.movie_table.get_children())

    rows = get_all_movies()

    for row in rows:
        self.movie_table.insert("", "end", values=row)