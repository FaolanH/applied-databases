import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="appdbproj", cursorclass=pymysql.cursors.DictCursor)

def get_session(number):
    if(not conn):
        print("No connection")
        connect();
    else:
        print("Already connected")

    query = "SELECT * FROM session

    with conn:
        cursor = conn.cursor()
        cursor.execute(query, (number))
        x = cursor.fetchall()
        print(x)
