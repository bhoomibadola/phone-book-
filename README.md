# Phone book
Phone Book uses class-based structure to store and manage contacts during a session. The program focuses on simplicity and demonstrates fundamental OOP principles like class variables, instance methods, class methods, and static methods.

## Requirements
Python 3.x
No external libraries required

## Features
1. Enter as many contacts as you need in a single session
2. Automatically rejects invalid phone numbers before saving
3. View every saved contact in a clean, readable format
4. Look up a contact's phone number using their name (case-insensitive)
5. Built entirely with Python's standard features, no installs needed

## How to run
Make sure python 3.13 is installed 
1. Clone the repository
2. Navigate into the project folder
3. Run the code

## Algorithm
### 1.Program Initialization
The Contact class is loaded into memory
A class-level variable phone_directory = [] is created as an empty shared list
This list will hold all Contact objects created during the session
It belongs to the class itself, not any individual contact

### 2.Get Number of Contacts
The program prompts: "how many contacts do you want to add?"
The user inputs an integer n
This number controls how many times the input loop will run
If n = 0, the loop is skipped entirely

### 3. Display All Contacts
After the loop ends, Contact.show_all_contact() is called
It checks if phone_directory is empty:
If empty → prints "No contact found"
If not empty → prints "all contacts in directory" and loops through each Contact object, calling show_contact() which returns "{name} {phone_number}"

## limitations 
1. Contacts are lost as soon as the program closes. There is no file saving, database, or CSV export.
2. You can add the same name or phone number multiple times and the program won't warn you.
3.  Once a contact is saved, there is no way to update or remove it during the session.
4.  Any input is accepted as a name, including empty strings, numbers, or symbols like !!!.thus there is no name validation.
5.   The program always runs in one direction: add contacts → display all. There is no menu to choose what to do next.
6.    Every time you run the script, it starts completely fresh with zero contacts.
