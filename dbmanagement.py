import sqlite3
import db

#db.init_db()
#db.clear_sessions()
get_sessions = db.get_sessions()
# Print all found sessions
for session in get_sessions:
    print(f"Session ID: {session['id']}, Access Token: {session['access_token']}, Instance URL: {session['instance_url']}, Created At: {session['created_at']}")



