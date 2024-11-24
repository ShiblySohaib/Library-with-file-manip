import save_book

def add_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = int(input("Enter ISBN: "))
        year = int(input("Enter publishing year: "))
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except:
        print("\033[31mInvalid input. Try again\033[0m")
        return
    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "price" : price,
        "quantity" : quantity,
    }

    save_book.save_book((book))

