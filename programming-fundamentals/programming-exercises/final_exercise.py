book1 = {
    "title": "Don Quijote",
    "availability": True
}
book2 = {
    "title": "Twelve rules for life",
    "availability": True
}
book3 = {
    "title": "Atomic Habits",
    "availability": True
}
book4 = {
    "title": "Sophie's Choice",
    "availability": True
}
bookshelf = [book1, book2, book3, book4]

while True:
    user_input: str = input("Write here the book you want: ")

    def check_book(book):
        if book["title"] == user_input and book["availability"] == True:
            book["availability"] = False
            return "You took this book"
        elif book["title"] == user_input and book["availability"] == False:
            return "This book is not available"
        elif user_input == f"return {book['title']}" and book["availability"] == False:
            book["availability"] = True
            return "The book was returned correctly"
        return None

    # book_filtered = next(filter(check_book, bookshelf), "The book written is not in the data base, sorry")

    book_found = "The book written is not in the data base, sorry"
    for book in bookshelf:
        result = check_book(book)
        if result:
            book_found = result
            break

    print(book_found)

    user_input_exit: str = input("Would you like to continue with the bookshelf?:(Y/N) ")
    if user_input_exit.lower() in ["y", "yes"]:
        break

