# Library Management System - Uwaiz Lovell - Python Essentials 1

def library_totals(books):
    pass 

# Shows the ID of the most borrowed book, or None is no books are borrowed 
def most_borrowed(books):
    pass

# Ask for number of copies, uses exception handling to validate the return as an integer or None 
def read_valid_copies():
    pass

# To add new a new book or copies to an existing book by the same author 
def add_book(books, next_book_number):

    # Ask the user for the book details.
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    # Check that the user input is not blank 
    if title == "":
        print("The title cannot be blank.")
        return 
    
    # Check that the user input is not blank 
    if author == "":
        print("The author cannot be blank.")
        return 

    # How many copies the user would like to input
    try:
        copies = int(input("Number of copies: "))
    except ValueError:
        print("This is not a valid number of copies.")
        return

    # Make sure the number of copies start at 1
    if copies <= 0: 
        print("The number of copies must be more than 0.")
        return

    # Check if the book already exists
    for book_id, book in books.items():   

        #Check if the title and author match an existing book
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():

           # Add new copies of an existing book
           book["copies"] += copies
           print(" Copies added successfully.")
           return      

    # Create the next Book ID 
    book_id = "B" + str(next_book_number) 

    # Adding a new book to the dictionary 
    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies,
    }

    # To notify the user the book was added successfully
    print("Book was added successfully.") 

    # Increase the book number for the next new book 
    next_book_number += 1 

    # To return the updated counter to the main program 
    return next_book_number 


# To register a new member's ID 
def register_member(members):
    pass 

# To see which books were borrowed, how many books were borrowed and by which member. This is used to update both dictionaries. 
def borrow_book(books, members):
    pass


# To see which books were returned, how many books were returned and which member returned them. The reverse of the borrow function but also updates both dictionaries 
def return_book(books, members):
    pass

# To search for books in the library, by number of copies, title and author. 
def search_catalogue(books):
    pass

# Member summary taken from both dictionaries to create a list of the member's ID, name, books currently being borrowed, the ID and title and author of each book as well as None if no books borrowed.
def member_summary(books, members):
    pass


# A report showing all the information in the library.
def library_report(books, members):
    pass

# Main Program

# Create the dictionaries with empty lists and automatically generated ID's
books = {}
members = {}
next_book_number = 1
next_member_number = 1

# Keep the program running until the user decides to exit.
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Books")
    print("4. Return Books")
    print("5. Search Catalogue")
    print("6. Member Summary")
    print("7. Library Report")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == '1':
        next_book_number = add_book(books, next_book_number)
        print(books)  # Test feature in the main program 
    elif choice == '2':
        register_member(members)
    elif choice == '3':
        borrow_book(books, members)
    elif choice == '4':
        return_book(books, members)
    elif choice == '5':
        search_catalogue(books)
    elif choice == '6':
        member_summary(books, members)
    elif choice == '7':
        library_report(books, members)
    elif choice == '8':
        print("Leaving the library, Goodbye.")
        break
    else:
        print("Invalid choice. Please choose from 1-8.") 


    
    
