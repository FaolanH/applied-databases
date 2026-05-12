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

def get_session():
    global conn
    if conn is None:
        connect()

    query = "SELECT * FROM session"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
