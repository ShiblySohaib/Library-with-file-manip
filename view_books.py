import csv

def view_books():
    with open("library.csv", "r") as library:
        reader = csv.reader(library)
        count = 0

        for book in reader:
            if count == 0 and not book:
                print("\033[31mNo book found. Library empty!\033[0m")
                return
            count+=1
            if count == 1:
                print("\n\nBook list:")
                print("==========")
            print(f"Title: {book[0]} | Author: {book[1]} | ISBN: {book[2]} | Publishing year: {book[3]} | Price: {book[4]} | Quantity: {book[5]}")

