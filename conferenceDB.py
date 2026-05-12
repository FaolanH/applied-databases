import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="appdbproj",
        cursorclass=pymysql.cursors.DictCursor
    )

def get_session(speaker_name):
    global conn
    if conn is None:
        connect()

    query = """
    SELECT speakerName, sessionTitle, roomID
    FROM session 
    WHERE speakerName LIKE %s
"""
    cursor = conn.cursor()
    cursor.execute(query, ("%" + speaker_name + "%",))
    rows = cursor.fetchall()
    return rows
