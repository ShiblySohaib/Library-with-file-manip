import csv
import os

def remove_book():
    isbn = input("Enter ISBN of book to remove: ")

    exists = False
    with open("library.csv", "r") as oldlibrary, open("tmp.csv", "w", newline="") as newlibrary:
        reader = csv.reader(oldlibrary)
        writer = csv.writer(newlibrary)

        for book in reader:
            if book:
                #check by ISBN if books exists
                if book[2] == isbn:
                    exists = True
                    continue
                else:
                    writer.writerow(book)

        if not exists:
            print("\033[31mBook not found\033[0m")
            newlibrary.close()
            os.remove("tmp.csv")
            return
    
    
    os.remove("library.csv")
    os.rename("tmp.csv", "library.csv")
    print("\033[32mBook removed successfully!\033[0m")

        