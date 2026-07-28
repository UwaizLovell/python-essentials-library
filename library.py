==== LIBRARY MANAGEMENT SYSTEM ====

def library_totals(books):
    pass 

# Shows the ID of the most borrowed book, or None is no books are borrowed 
def most_borrowed(books):
    pass

# Ask for number of copies, uses exception handling to validate the return as an integer or None 
def read_valid_copies():

    # Ask the user for the number of copies they would like to add 
    try:
        copies = int(input("Number of copies: "))

        # Handle any input that cannot be converted into an integer 
    except ValueError:
        print("That is not a valid number of copies.")
        return None

    # Check if the number of copies is atleast 1
    if copies < 1:
        print("That is not a valid number of copies.") 
        return None 

# To add new a new book or copies to an existing book by the same author 
def add_book(books, next_book_number):
    pass

# To register a new member's ID 
def register_member(members, next_member_number):
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
    print("\n===== Library Management System =====")
    print("1. Add a book")
    print("2. Register a member")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Search the catalogue")
    print("6. Member summary")
    print("7. Library Report")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == '1':
        next_book_number = add_book(books, next_book_number)
    elif choice == '2':
        next_member_number = register_member(members, next_member_number)
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
        print("Invalid choice. Please enter 1-8.") 


    
    
