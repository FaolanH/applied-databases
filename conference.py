# this is the link to the database
import conferenceDB
# this is used to format dates (see new_attendee DOB as an example)
from datetime import datetime

# the main section of the code, all the functions defined below lead into this
def main():
    while True:
      display_menu()
      choice = input("Please input your choice: ")
      
      # End the loop
      if (choice =="x"):
         break
      # Choice 1 - View Speakers and Sessions  
      elif (choice == "1"):
          speaker_name = input("Enter speaker name or title: ")
          conference_sessions(speaker_name)
      # Choice 2 - View Attendees by Company  
      elif (choice == "2"):
          company_ID = input("Enter the company ID of the attendee (or type x to cancel): ")
          if company_ID.lower() == "x":
            return
          attendee_details(company_ID)
      # Choice 3 - Add New Attendee
      elif (choice == "3"):
            new_record = print("Please fill in the new attendee details below: ")
            new_attendee()
      # Choice 4 - View Connected Attendees     
      elif (choice == "4"):
        attendee_ID = input("Please enter attendee ID to view connections: ")
        if attendee_ID.isdigit():
            view_connections(int(attendee_ID))
        else:
            print("Invalid ID - please try again")
      # Choice 5 - Add Attendee Connection     
      elif (choice == "5"):
           new_connection = print("Please detail new attendee connections below: ")
           attendee_connection()
           
      # Choice 6 - View Rooms
      elif (choice == "6"):
            print("These are the rooms where the sessions will be on: ")
            rooms()

# Overall Display Menu - what the user sees 
def display_menu():
   print ("\n-------------------------------------------------------------------------------")
   print ("Conference Management")
   print("----------------------------")
   print("")
   print("MENU")
   print("==========")
   print("1 - View Speakers and Sessions")
   print("2 - View Attendees by Company")
   print("3 - Add New Attendee")
   print("4 - View Connected Attendees")
   print("5 - Add Attendee Connection")
   print("6 - View Rooms")
   print("x - Exit Application")
   print("----------------------------")

# Choice 1 - View Speakers and Sessions function
def conference_sessions(speaker_name): 
# this links to queries into the database     
    sessions = conferenceDB.get_session(speaker_name)
    
    # if speaker not found, brings back to main display menu 
    if not sessions:
        print("\n No speakers found matching: ", speaker_name)
        return
    # returns list of session based on the user input (dr will return all session where the speaker is a dr.)    
    print("\nSESSION LIST OF SPECIFIED SPEAKERS")
    print("============")
    for s in sessions:
        print(f"{s['speakerName']:^20} |{s['sessionTitle']:^30} | Room {s['roomName']}")

# Choice 2 - View Attendees by Company function
def attendee_details(company_ID): 
    
        # ensuring users have several options to retry inputting company_ID is the first attempt is incorrect
        while True:
                       
            if company_ID.lower() == "x":
                print("\nReturning to main menu.")
                return
# this links to queries into the database
            companyName, details = conferenceDB.get_details(company_ID)  

            # If there is no such company, they can keep trying
            if companyName is None:
                print(f"\n Company with an ID of '{company_ID}' does not exist, please try again")
                company_ID = input("Enter a valid company ID (or x to cancel): ")
                continue

            # The company exists but there are no attendees at the conference.
            if len(details) == 0:
                print(f"\nCompany '{companyName}' exists but has no registered attendees.")
                company_ID = input("Enter another company ID (or x to cancel): ")
                continue
            
            break  
            # initial message            
            company_ID = input("Enter the company ID of the attendee (or type x to cancel): ")
        
        
        # adding the company name to the output
        print(f"\n {details[0]['companyName']} ATTENDEE DETAILS")
        print("============")
        for d in details:
            print(f"{d['attendeeName']:^20} |{d['attendeeDOB']} |{d['sessionTitle']:^40} |{d['speakerName']:^20}| Room {d['roomName']:^15} |{d['sessionDate']}")        

# Choice 3  - Add New Attendee function
def new_attendee():
    
    # setting the attendee ID
    while True:
        try:
            attendee_ID = int(input("Please enter the new attendee ID: "))
        except ValueError:
            print("ID must be a number.")
            continue

        # checking if the ID already exists
        if conferenceDB.get_attendees(attendee_ID):
            print("That attendee ID already exists. Try again.")
            continue
        break

    # adding in attendee name
    while True:
        attendee_name = input("Please enter the new attendee name and surname: ").strip()
        # ensuring there is at least two names
        if len(attendee_name.split()) < 2:
            print("Please enter both first and last name.")
        else:
            break
    # adding in the DOB, correctly ordered thanks to datetime
    while True:
        attendee_DOB = input("Please enter Date of Birth (YYYYMMDD): ").strip()

        try:
            # Try to parse the date
            dob_date = datetime.strptime(attendee_DOB, "%Y%m%d").date()
            break
        except ValueError:
            print("Invalid date. Please enter a real date in YYYYMMDD format.")

    # Setting the Male/Female Sex option (I tried to add 'Other' but this was not an option due to the original set-up
    while True:
        attendee_Gender = input("Please enter the new attendee sex (Male or Female): ")
        if attendee_Gender in ("Male", "Female"):
            break
        print("Invalid gender. Enter Male or Female.")

    # Ensuring the Company ID is correct
    while True:
        try:
            attendee_CompanyID = int(input("Please enter the new attendee Company ID(1-9): "))
        except ValueError:
            print("Company ID must be a number.")
            continue

        if 1 <= attendee_CompanyID <= 9:
            break
        print("Company ID must be between 1 and 9.")

    # Insert this new attendee into the database
    conferenceDB.insert_attendee(
        attendee_ID,
        attendee_name,
        dob_date,
        attendee_Gender,
        attendee_CompanyID
    )

    print("\nNew attendee added successfully.")

#Choice 4 - View Connected Attendees
def view_connections(attendee_ID):
    connections = conferenceDB.get_attendee_connections(attendee_ID)

    if not connections:
        print(f"\nAttendee {attendee_ID} has no connections.")
        return

    print("\nCONNECTED ATTENDEES")
    print("====================")
    print(f"{'ID':<10} | Name")
    print("-----------------------------")

    for cid in connections:
        name = conferenceDB.get_attendee_name(cid)
        print(f"{cid:<10} | {name}")        

# Choice 5 - Add Attendee Connection
def attendee_connection():
# setting the attendee 1 ID
    while True:
        try:
            attendee_1_ID = input("Please enter the first attendee ID you would like to connect: ")
            if not attendee_1_ID.isdigit() or len(attendee_1_ID) != 3:
                print("Error: Attendee ID must be a 3‑digit number, please try again")
                return
        except ValueError:
            print("ID must be a number.")
            continue

        # checking if the ID is already connected
        if conferenceDB.show_attendee_connections(attendee_1_ID):
            print("That attendee ID is already connected. Try again.")
            continue
        break
        
        # setting the attendee 2 ID
    while True:
        try:
            attendee_2_ID = input("Please enter the second attendee ID you would like to connect: ")
            if not attendee_2_ID.isdigit() or len(attendee_2_ID) != 3:
                print("Error: Attendee ID must be a 3‑digit number, please try again")
                return

        except ValueError:
            print("ID must be a number.")
            continue
        
        # checking if the ID is already connected
        if conferenceDB.show_attendee_connections(attendee_2_ID):
            print("That attendee ID is already connected. Try again.")
            continue
        break
        
    if attendee_1_ID == attendee_2_ID:
        print ("*** ERROR *** An attendee cannot be connected to themselves")
        
        
# Choice 6 - View Rooms function
def rooms(): 
# this links to queries into the database     
    rooms = conferenceDB.view_rooms()
    
        # returns list of session based on the user input (dr will return all session where the speaker is a dr.)    
    print("\nList of Rooms")
    print("============")
    for r in rooms:
        print(f"ID: {r['roomID']} | {r['roomName']} | Capacity: {r['capacity']}")
    
    
if __name__ == "__main__":
    main()