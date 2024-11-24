import add_book
import remove_book
import update_book
import view_books
import lend_book
import return_book
import os


def app():
    if not os.path.exists("library.csv"):
        open("library.csv", "w")
        
    while True:
        print("\t\tLibrary Management System")
        print("\t\t=========================\n")
        print("1. Add book")
        print("2. Remove book")
        print("3. Update book")
        print("4. Lend book")
        print("5. Return book")
        print("6. View all books")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        choice = int(choice) if choice.isnumeric() else None

        print("\n")

        if choice == 1:
            add_book.add_book()
        elif choice == 2:
            remove_book.remove_book()
        elif choice == 3:
            update_book.update_book()
        elif choice == 4:
            lend_book.lend_book()
        elif choice == 5:
            return_book.return_book()
        elif choice == 6:
            view_books.view_books()
        elif choice == 0:
            print("\033[32mThanks for using Library Management System\033[0m")
            exit()
        else:
            print("\033[31mInvalid Choice. Try again\033[0m")


        print("\n\n")

app()