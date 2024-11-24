import csv
import os

def return_book():
    isbn = input("Enter ISBN of book to return: ")

    exists = False
    with open("library.csv", "r", newline="") as oldlibrary, open("tmp.csv", "w", newline="") as newlibrary:
        reader = csv.reader(oldlibrary)
        writer = csv.writer(newlibrary)

        for book in reader:
            if book:
                if book[2] == isbn:
                    exists = True
                    book[5] = int(book[5])+1
                    writer.writerow(book)
                else:
                    writer.writerow(book)

        if not exists:
            print("\033[31mBook not found\033[0m")
            newlibrary.close()
            os.remove("tmp.csv")
            return
    
    
    
    os.remove("library.csv")
    os.rename("tmp.csv", "library.csv")
    print("\033[32mBook returned successfully!\033[0m")
