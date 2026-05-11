#author: Faolán Hamilton

# setting up the user input

# Defining the user options
def display_menu():
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

def get_name(n):
   name = input(n) 
   return name

def schedule():
    if (choice == "1"):
        session = appdbproj.get_session()
        print(session)


def main():
    speaker_name = "Enter speaker name: "
    while True:
      display_menu()
      choice = input("Please input your choice: ")
      
      if (choice =="x"):
         break
      elif (choice == "1"):
         return schedule

if __name__ == "__main__":
   main()