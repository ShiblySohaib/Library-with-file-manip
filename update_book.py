import csv
import os

def update_book():
    #get book data
    isbn = input("Enter ISBN of the book to update: ")


    exists = False
    with open("library.csv", "r") as oldlibrary, open("tmp.csv", "w", newline="") as newlibrary:
        reader = csv.reader(oldlibrary)
        writer = csv.writer(newlibrary)

        for book in reader:
            if book:
                #if book found, then get new info to update it
                if book[2] == isbn:
                    exists = True
                    print("\n\nEnter updated information: ")
                    print("--------------------------")
                    try:
                        title = input("Enter book title: ")
                        author = input("Enter author name: ")
                        isbn = int(input("Enter ISBN: "))
                        year = int(input("Enter publishing year: "))
                        price = float(input("Enter price: "))
                        quantity = int(input("Enter quantity: "))
                    except:
                        print("\033[31mInvalid input. Try again\033[0m")
                        newlibrary.close()
                        os.remove("tmp.csv")
                        return
                    
                    writer.writerow([title, author, isbn, year, price, quantity])
                else:
                    writer.writerow(book)

        if not exists:
            print("\033[31mBook not found\033[0m")
            newlibrary.close()
            os.remove("tmp.csv")
            return
    
    
    os.remove("library.csv")
    os.rename("tmp.csv", "library.csv")
    print("\033[32mBook updated successfully!\033[0m")

        