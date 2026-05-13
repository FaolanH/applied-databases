import conferenceDB
from datetime import datetime

def main():
    while True:
      display_menu()
      choice = input("Please input your choice: ")
      
      if (choice =="x"):
         break
      elif (choice == "1"):
          speaker_name = input("Enter speaker name or title: ")
          conference_sessions(speaker_name)
      elif (choice == "2"):
          company_ID = input("Enter the company ID of the attendee (or type x to cancel): ")
          if company_ID.lower() == "x":
            return
          attendee_details(company_ID)
      elif (choice == "3"):
            new_record = print("Please fill in the new attendee details below: ")
            new_attendee()

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
   
def conference_sessions(speaker_name):
    
    sessions = conferenceDB.get_session(speaker_name)
    
    if not sessions:
        print("\n No speakers found matching: ", speaker_name)
        return
        
    print("\nSESSION LIST OF SPECIFIED SPEAKERS")
    print("============")
    for s in sessions:
        print(f"{s['speakerName']:^20} |{s['sessionTitle']:^30} | Room {s['roomName']}")

def attendee_details(company_ID):
    
    
        while True:
            if company_ID.lower() == "x":
                print("\nReturning to main menu.")
                return

            companyName, details = conferenceDB.get_details(company_ID)


            if companyName is None:
                print(f"\nCompany ID '{company_ID}' does not exist.")
                company_ID = input("Enter a valid company ID (or x to cancel): ")
                continue

        # CASE 2: Company exists but has zero attendees
            if len(details) == 0:
                print(f"\nCompany '{companyName}' exists but has no registered attendees.")
                company_ID = input("Enter another company ID (or x to cancel): ")
                continue
            
            break  

            print(f"\nCompany with an ID of '{companyName}'does not exist, please try again")
            company_ID = input("Enter the company ID of the attendee (or type x to cancel): ")

        
        print(f"\n {details[0]['companyName']} ATTENDEE DETAILS")
        print("============")
        for d in details:
            print(f"{d['attendeeName']:^20} |{d['attendeeDOB']} |{d['sessionTitle']:^40} |{d['speakerName']:^20}| Room {d['roomName']:^15} |{d['sessionDate']}")        
 
def new_attendee():
    while True:
        try:
            attendee_ID = int(input("Please enter the new attendee ID: "))
        except ValueError:
            print("ID must be a number.")
            continue

        
        if conferenceDB.get_attendees(attendee_ID):
            print("That attendee ID already exists. Try again.")
            continue
        break


    while True:
        attendee_name = input("Please enter the new attendee name and surname: ").strip()
        if len(attendee_name.split()) < 2:
            print("Please enter both first and last name.")
        else:
            break

    while True:
        attendee_DOB = input("Please enter Date of Birth (YYYYMMDD): ").strip()

        try:
            # Try to parse the date
            dob_date = datetime.strptime(attendee_DOB, "%Y%m%d").date()
            break
        except ValueError:
            print("Invalid date. Please enter a real date in YYYYMMDD format.")

    # Gender validation
    while True:
        attendee_Gender = input("Please enter the new attendee sex (Male or Female): ")
        if attendee_Gender in ("Male", "Female"):
            break
        print("Invalid gender. Enter Male or Female.")

    # Company ID validation
    while True:
        try:
            attendee_CompanyID = int(input("Please enter the new attendee Company ID(1-9): "))
        except ValueError:
            print("Company ID must be a number.")
            continue

        if 1 <= attendee_CompanyID <= 9:
            break
        print("Company ID must be between 1 and 9.")

    # Insert into DB
    conferenceDB.insert_attendee(
        attendee_ID,
        attendee_name,
        dob_date,
        attendee_Gender,
        attendee_CompanyID
    )

    print("\nNew attendee added successfully.")

 
if __name__ == "__main__":
    main()