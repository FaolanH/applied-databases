import pymysql
from neo4j import GraphDatabase

conn = None

driver = None

def connect_neo4j():
    global driver
    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "test1234"),
    database="attendeeNetwork"
    )



)

#def get_attendee_relationships(tx):
    #query = 

def main():
    connect_neo4j()
    with driver.period() as period:
        values = period.read_transaction(get_attendee_relationships, "RETURN 1 AS x")

def connect_db():
    global conn
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="appdbproj",
        cursorclass=pymysql.cursors.DictCursor
    )
#  Choice 1 - View Speakers and Sessions    
def get_session(speaker_name):
    global conn
    if conn is None:
        connect_db()

    query = """
    SELECT 
        s.speakerName,
        s.sessionTitle,
        s.roomID,
        r.roomName
    FROM session AS s
    JOIN room AS r
        ON s.roomID = r.roomID
    WHERE s.speakerName LIKE %s;
"""

    cursor = conn.cursor()
    cursor.execute(query, ("%" + speaker_name + "%",))
    rows = cursor.fetchall()
    return rows

# Choice 2 - View Attendees by Company
def get_details(company_ID):
    
   
    global conn
    if conn is None:
        connect_db()
        
    cursor = conn.cursor()
    
    cursor.execute("SELECT companyName FROM company WHERE companyID = %s", (company_ID,))
    company = cursor.fetchone()

    if not company:
        return None, None   # company does not exist

    companyName = company['companyName']

    query = """
   SELECT 
    a.attendeeName,
    a.attendeeDOB,
    s.sessionTitle,
    s.speakerName,
    r.roomName,
    s.sessionDate, 
    c.companyName
FROM attendee a
JOIN company c          ON a.attendeeCompanyID = c.companyID
JOIN registration re    ON re.attendeeID = a.attendeeID
JOIN session s          ON s.sessionID = re.sessionID
JOIN room r             ON r.roomID = s.roomID
WHERE a.attendeeCompanyID LIKE %s;
"""


    cursor = conn.cursor()
    cursor.execute(query, ("%" + company_ID + "%",))
    rows = cursor.fetchall()
    return companyName, rows
    
# Choice 3  - Add New Attendee (ensuring attendee does not already exist)    
def get_attendees(attendee_ID):
    global conn
    if conn is None:
        connect_db()

    query = "SELECT attendeeID FROM attendee WHERE attendeeID = %s";


    cursor = conn.cursor()
    cursor.execute(query, (attendee_ID,))
    row = cursor.fetchone()
    return row is not None 
    
# Choice 3  - Add New Attendee to Database   
def insert_attendee(attendee_ID, attendee_name, dob_date, attendee_Gender, attendee_CompanyID):
    global conn
    if conn is None:
        connect_db()

    query = """
        INSERT INTO attendee (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (attendee_ID, attendee_name, dob_date, attendee_Gender, attendee_CompanyID))
    conn.commit()


# Choice 4 - 

def get_attendee_connections(attendee_ID):
    global driver
    if driver is None:
        connect_neo4j()

    query = """
    MATCH (a:Attendee {AttendeeID: $id})-[:CONNECTED_TO]->(b:Attendee)
    RETURN b.AttendeeID AS connectedID
    """

    with driver.session() as session:
        results = session.run(query, id=attendee_ID)
        return [record["connectedID"] for record in results]

def get_attendee_name(attendee_ID):
    global conn
    if conn is None:
        connect_db()

    query = "SELECT attendeeName FROM attendee WHERE attendeeID = %s"
    cursor = conn.cursor()
    cursor.execute(query, (attendee_ID,))
    row = cursor.fetchone()

    return row["attendeeName"] if row else None


