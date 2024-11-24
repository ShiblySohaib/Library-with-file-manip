import csv
import os

def save_book(new_book):
    with open("library.csv", "r", newline="") as oldlibrary, open("tmp.csv", "w", newline="") as newlibrary:
        reader = csv.reader(oldlibrary)
        writer = csv.writer(newlibrary)

        #check by ISBN if book already exits
        for book in reader:
            if book:
                if book[2] == str(new_book["isbn"]):
                    print("\033[96mBook already exists\033[0m")
                    newlibrary.close()
                    os.remove("tmp.csv")
                    return
                else:
                    writer.writerow(book)
        
        writer.writerow(list(new_book.values()))
    
    
    os.remove("library.csv")
    os.rename("tmp.csv", "library.csv")
    print("\033[32mBook added successfully!\033[0m")

        