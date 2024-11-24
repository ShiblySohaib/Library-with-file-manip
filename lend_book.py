import csv
import os

def lend_book():
    isbn = input("Enter ISBN of book to lend: ")

    exists = False
    with open("library.csv", "r", newline="") as oldlibrary, open("tmp.csv", "w", newline="") as newlibrary:
        reader = csv.reader(oldlibrary)
        writer = csv.writer(newlibrary)

        for book in reader:
            if book:
                if book[2] == isbn:
                    exists = True
                    if int(book[5]) == 0:
                        print("\033[96mNo copies left to rent!\033[0m")
                        newlibrary.close()
                        os.remove("tmp.csv")
                        return
                    else:
                        book[5] = int(book[5])-1
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
    print("\033[32mBook lent successfully!\033[0m")
