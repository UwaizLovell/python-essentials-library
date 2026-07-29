# Library Management System - Uwaiz Slade Lovell - Python Essentials 1

# To check the total number of copies and available copies in the library
def library_totals(books):

    # Keep track of the total number of copies 
    total_copies = 0

    # Keep track of the total number of available copies
    available_copies = 0 

    for book_id in books:

        # Add the total number of copies for this book
        total_copies += books[book_id]["total"]

        # Add the number of available copies for this book
        available_copies += books[book_id]["available"]

    # Return the total copies and available copies as a tuple
    return total_copies, available_copies  

# Shows the ID of the most borrowed book, or None is no books are borrowed 
def most_borrowed(books):

    # Check the current most borrowed book
    best_book_id = None

    # Check the highest borrow count of a book 
    most_times_borrowed = None 

    # Loop through every book in library
    for book_id in books:

        # Check if it is the first book or has it been borrowed before 
        if most_times_borrowed is None or books[book_id]["times_borrowed"] > most_times_borrowed:

            # Update the highest borrow count
            most_times_borrowed = books[book_id]["times_borrowed"]

            # Name the book that has the highest count 
            best_book_id = book_id 

    # Return the ID of the most borrowed book 
    return best_book_id

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

    # Return the valid number of copies
    return copies 

# To add new a new book or copies to an existing book by the same author 
def add_book(books, next_book_number):

    # Ask the user to enter the title of the book
    title = input("Title: ").strip() 

    # Check if the user entered a blank input
    if title == "":
        print("A title cannot be blank.")
        return next_book_number 

    # Ask the user to enter the author's name
    author = input("Author: ").strip()

    # Check if the user entered a blank input 
    if author == "":
        print("An author cannot be blank.")
        return next_book_number 

    # Ask the user for the number of copies 
    copies = read_valid_copies()

    # To stop the user if the input is invalid
    if copies is None:
        return next_book_number 

    # Check if the book already exists 
    for existing_book_id in books:

        existing_book = books[existing_book_id]

        if (existing_book["title"].lower() == title.lower() and
                existing_book["author"].lower() == author.lower()):

            existing_book["total"] += copies
            existing_book["available"] += copies 

            print("Added " + str(copies) + " more copies of " +
                  existing_book_id + ": " + existing_book["title"] + " by " + books[book_id]["author"] + 
                  " (now " + str(existing_book["total"]) + " total)") 

            return next_book_number 


    # Create the ID for the next book
    book_id = "B" + str(next_book_number) 

    # Add new book to library 
    books[book_id] = {
        "title": title,
        "author": author,
        "total": copies,
        "available": copies,
        "times_borrowed": 0
    }

    # Confirm the book was added
    print("Added " + book_id + ": " + title + " by " + author +
      " (" + str(copies) + " copies)")

    # Return the next available book number 
    return next_book_number + 1 

# To register a new member's ID 
def register_member(members, next_member_number):

    # Ask the user to enter the member's name
    name = input("Member name: ").strip()

    # Check if the user entered a blank name
    if name == "":
        print("A member name cannot be blank.")
        return next_member_number

    # Create ID for the next member
    member_id = "M" + str(next_member_number)

    # Register the member 
    members[member_id] = {
        "name": name, 
        "borrowed": []
    }

    # Confirm the member was registered
    print("Registered " + member_id + ": " + name)

    # Return the next available member number
    return next_member_number + 1 

# To see which books were borrowed, how many books were borrowed and by which member. This is used to update both dictionaries. 
def borrow_book(books, members):

    # Ask the user for the member ID 
    member_id = input("Member ID: ").strip() 

    # Ask the user for the book ID 
    book_id = input ("Book ID: ").strip() 

    # Check if the member exists 
    if member_id not in members:
        print("Member not fouund.")
        return 

    # Check if the book exists 
    if book_id not in books:
        print("Book not found.")
        return 

    # Check if the member has already borrowed 3 books 
    if len(members[member_id]["borrowed"]) >= 3:
        print("Member has already borrowed maximum number of books.")
        return 

    if book_id in members[member_id]["borrowed"]:
        print("Member has already borrowed this book.") 
        return

    # Check if there are copies available
    if books[book_id]["available"]== 0:
        print("No copies of this book are available.")
        return

    # To update the books dictionary 
    books[book_id]["available"] -= 1
    books[book_id]["times_borrowed"] += 1

    # To update the members dictionaries 
    members[member_id]["borrowed"].append(book_id)

    # Output message giving all the details
    print(member_id + " " + members[member_id]["name"] + " borrowed " + book_id + ": " +
      books[book_id]["title"] + " by " + 
      books[book_id]["author"] +
      " (" + str(books[book_id]["available"]) + " copies available)")

# To see which books were returned, how many books were returned and which member returned them. The reverse of the borrow function but also updates both dictionaries 
def return_book(books, members):

    # Ask the user for the member ID 
    member_id = input("Member ID: ").strip()

    # Ask the user for the book ID
    book_id = input("Book ID: ").strip()

    # Check if the member exists 
    if member_id not in members: 
        print("Member not found. ")
        return 

    # Check if the member has borrowed this book 
    if book_id not in members[member_id]["borrowed"]:
        print(member_id + " " + members[member_id]["name"] +
               " does not have " + book_id + " " + books[book_id]["title"] + " by " + 
                     books[book_id]["author"] + ".")
        return 

    # Remove the book from the member's borrowed list 
    members[member_id]["borrowed"].remove(book_id) 

    # Increase the available copies of the book
    books[book_id]["available"] += 1

    # Output message giving all the details
    print(
    member_id + " " + members[member_id]["name"] +
    " returned " + 
    book_id + " " +
    books[book_id]["title"] +
    " by " +
    books[book_id]["author"]
    )

# To search for books in the library, by number of copies, title and author. 
def search_catalogue(books):

    # Check if the catalogue is empty
    if len(books) == 0:
        print("The catalogue is empty.")
        return

    # Ask the user for a keyword 
    keyword = input("Keyword: ").strip()

    # To track any matching books found 
    found = False 

    # Search through every book in the library
    for book_id in books:

        # Check if the keyword appears in the book title
        if keyword.lower() in books[book_id]["title"].lower():

            # Show a book following the keyword was found
            found = True 

            # Display the matching book details 
            print(
                book_id + ": " +
                books[book_id]["title"] + " by " +
                books[book_id]["author"] + " - " +
                str(books[book_id]["available"]) +
                " of " + str(books[book_id]["total"]) + " available"
            )

    # Final check that no books were matching the keyword 
    if found == False: 
        print("No books found matching that search.") 

# Member summary taken from both dictionaries to create a list of the member's ID, name, books currently being borrowed, the ID and title and author of each book as well as None if no books borrowed.
def member_summary(members, books):

    # Ask the user to a member ID 
    member_id = input("Member ID: ").strip()

    # Check if the member exists
    if member_id not in members:
        print("Member not found.")
        return

    # Display the member's details
    print("Member ID: " + member_id)
    print("Name: " + members[member_id]["name"])

    # Check if the member has borrowed any books 
    if len(members[member_id]["borrowed"]) == 0:
        print("No books have been currently borrowed.")
        return

    # Display the books currently borrowed by the member 
    print("Borrowed books:")

    for book_id in members[member_id]["borrowed"]:
        print(book_id + ": " + books[book_id]["title"] + " by " + books[book_id]["author"])
    
# A report showing all the information in the library.
def library_report(books, members):

    # Check if there are any books in the library 
    if len(books) == 0:
        print("The library catalogue is empty.")
        return 

    # Calculate how many different book titles there are in the library
    total_titles = len(books)

    # Unpack the tuple from the helper function 
    total_copies, available_copies =  library_totals(books)

    # To see how many copies are currently being borrowed 
    copies_being_borrowed = total_copies - available_copies

    # Recieve the ID of the most borrowed book
    most_borrowed_book = most_borrowed(books) 

    print("Library Report")
    print("Titles:", total_titles)
    print("Total copies:", total_copies)
    print("Available copies:", available_copies)
    print("Copies currently being borrowed:", copies_being_borrowed) 

    # To display the most borrowed book 
    if most_borrowed_book is None:
        print("Most borrowed book: None")
    else: 
        print(
            "Most borrowed book:", most_borrowed_book, "-", 
            books[most_borrowed_book]["title"], " by ", 
            books[most_borrowed_book]["author"], 
            "(" + str(books[most_borrowed_book]["times_borrowed"]) + " borrows)"
        )

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
        member_summary(members, books)
    elif choice == '7':
        library_report(books, members)
    elif choice == '8':
        print("Leaving the library, Goodbye.")
        break
    else:
        print("Invalid choice. Please enter 1-8.") 


    
    
