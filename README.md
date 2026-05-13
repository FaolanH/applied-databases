# Applied Databases Project for ATU Data Analytics Summer 2026
# Author: Faolán Hamilton

## Interacting with this repository
There are seven different files (excluding .gigignore) within this repository as part of my submission: 
- This README.md
- appdbproj.sql (the first database used in this project, containing the majority of the conference information)
- appdbprojNeo4j.json (the second database used in this project, containing attendee connection information)
- conference.py (the main file used to create the user interface)
- conferenceDB.py (a file used to connect to the two databases in the background, feeding into the main conferece.py file)
- GitLink.txt (a text file containing a link to the repository)
- innovation.doc (includes user instructions, references and workarounds/additional inputs)

A brief summary of what this project is about:
There is a conference coming up and this program has been designed to better understand what to expect there. You can find information on:
- The Speakers and Sessions on over the conference
- The expected Attendees, their personal information and the company they represent
- Adding any New Attendee you expect to be there
- Connections between expected attendees
- Adding new Attendee connections.

The main file (conference.py) within this repository works with user input and have strict input mechanisms - please closely check inputs and the existing database to ensure the program runs smoothly.