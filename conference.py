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
        print(f"{s['speakerName']:20} |{s['sessionTitle']:30} | Room {s['roomID']}")

if __name__ == "__main__":
   main()