import conferenceDB

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
        print("\n No speakers found matching:", speaker_name)
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
  
if __name__ == "__main__":
    main()