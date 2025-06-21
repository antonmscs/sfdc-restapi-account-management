import sqlite3

def get_db_connection():
    conn = sqlite3.connect('sfdc-api.db')
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

def close_db_connection(conn):
    if conn:
        conn.close()    
        
        
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create a table for storing user sessions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            access_token TEXT NOT NULL,
            instance_url TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    close_db_connection(conn)
    
def save_session(access_token, instance_url):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO sessions (access_token, instance_url)
        VALUES (?, ?)
    ''', (access_token, instance_url))
    
    conn.commit()
    close_db_connection(conn)
    
def get_sessions():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sessions')
    sessions = cursor.fetchall()
    
    close_db_connection(conn)

    return sessions
def clear_sessions():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM sessions')
    
    conn.commit()
    close_db_connection(conn)
    
def get_session_by_id(session_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sessions WHERE id = ?', (session_id,))
    session = cursor.fetchone()
    
    close_db_connection(conn)
    
    return session  
