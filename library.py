# Library Management System - Uwaiz Lovell - Python Essentials 1

# To return the totals (total_copies, copies available) from the whole library as a tuple
def library_totals(books):
    pass 

# Shows the ID of the most borrowed book, or None is no books are borrowed 
def most_borrowed(books):
    pass

# Ask for number of cpoies, uses exception handling to vaidate the return as an integer or None 
def read_valid_copies():
    pass

# To add new a new book or copies to an existing book by the same author 
def add_book(books):
    pass

# To register a new member's ID 
def register_member(members):
    pass 

# To see which books were borrowed, how many books were borrowed and by which member. This is used to update both dictionaries. 
def borrow_books(books, members):
    pass


# To see which books were returned, how many books were returned and which memeber returned them. The reverse of the borrow function but also updates both dictionaries 
def return_books(books, members):
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

   
    if choice == '8':
        print("Leaving the library, Goodbye.")
        break
    
    
