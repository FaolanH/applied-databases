# Author: Faolán Hamilton
# Brief - Use a python file (.py) to interact with the appdbproj.sql database and the appdbprojNeo4j.json database

# Setting up user input and options for the menu
def main():
    speaker_name = "Enter speaker name: "
    while True:
        display_menu()
        choice = input("Please input your choice: ")

        if (choice == "x"):
            break
        elif (choice == "1"):
            speaker = get_name(speaker_name)
            print(speaker.upper())

# Defining the user options
def display_menu():
    print ("Conference Management")
    print("----------------------")
    print ("")
    print("MENU")
    print("====")
    print("1 - View Speakers and Sessions")
    print("2 - View Attendees by Company")
    print("3 - Add New Attendee")
    print("4 - View Connected Attendees")
    print("5 - Add Attendee Connection")
    print("6 - View Rooms")
    print("x - Exit application")

def get_name(n):
    name = input(n)
    return name

if __name__ == "__main__":
    main()


