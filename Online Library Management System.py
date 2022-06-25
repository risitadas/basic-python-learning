'''
Python Mini Project #1

Statement:-
The task is to create an “Online Library Management System”.
For this, we have to create a library class that includes the following methods:

Displaybook() : To display the available books
Lendbook(): To lend a book to a user
Addbook(): To add a book to the library
Returnbook(): To return the book to the library.

after creating a library class, now we will create an object and pass the following parameters in the constructor :-

NameofLibrary=Library(listofbooks, library_name)

After that, create a main function and run an infinite while loop that asks the users for their input
that whether they want to display, lend, add or return a book.

Optional:-
Maintain a dictionary for the users who own a book.
Dictionary should take book name as a key and name of the person as a value.
Whenever we lend a book to a user, we should maintain a dictionary.


'''


class Library:

    def __init__(self, listofbooks, lend_book):
        self.available_books = listofbooks
        self.lend_book = lend_book

    # Display Book Method

    def display_available_books(self):
        print("--- All Available Books are: ---")
        num = 1
        for books in self.available_books:
            print(f"{num}. {books}")
            num = num + 1

    # Lend Book Method

    def lend_books(self):
        lend_book_inp = str(input("Enter the Name of Book which you want to Lend: "))
        if lend_book_inp in self.available_books:
            print("The Book now has been lended which you requested.")
            self.available_books.remove(lend_book_inp)
            self.lend_book.append(lend_book_inp)

        else:
            print("Sorry! This Book is not available in THE MIDNIGHT LIBRARY which you requested.")

    # Add Book Method

    def add_book(self):
        add_book = str(input("Enter the Name of Book which you want to add in THE MIDNIGHT LIBRARY: "))
        if add_book not in self.available_books:
            self.available_books.append(add_book)
            print(f"Your '{add_book}' name Book successfully added in THE MIDNIGHT LIBRARY")
        else:
            print("This book is already added in THE MIDNIGHT LIBRARY, so you can not add this book.")

    # Return Book Method

    def return_book(self):
        if not self.lend_book:
            print("You do not Lend any Book yet.")

        elif not self.lend_book == False:
            return_book = input("Enter the Name of book you want to return: ")
            if return_book in self.lend_book:
                print("Thanks to returns the Book which you Lended.")
                self.lend_book.remove(return_book)
                self.available_books.append(return_book)
            else:
                print("You Enter Wrong Book Name, Please Enter correct Name.")


# Main Function -->

def main():
    library = Library(["Strangers on a Train by Patricia Highsmith, Paula Hawkins",
"Gone Girl by Gillian Flynn","The Silence of the Lambs by Thomas Harris",
"Misery by Stephen King","Talented Mr Ripley by Patricia Highsmith",
"Your House Will Pay by Steph Cha","Shutter Island by Dennis Lehane","Rebecca by Daphne du Maurier"],[])

    while True:
        print("\n--->THE MIDNIGHT LIBRARY <---")
        print("What do you want? \n \t1. Display All Books. \n \t2. Lend a Book. \n \t3. Add a Book. \n \t4. Return a Book.")

        user_inp = int(input("\nEnter your Choice: \n"))

        if user_inp == 1:
            library.display_available_books()

        elif user_inp == 2:
            library.lend_books()

        elif user_inp == 3:
            library.add_book()

        elif user_inp == 4:
            library.return_book()


main()