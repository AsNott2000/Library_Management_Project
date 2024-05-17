class Library:
    def __init__(self, filename='books.txt'):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def __del__(self):  
        if hasattr(self, "file"):
            self.file.close
    
    def listBooks(self):
        self.file.seek(0)
        lines = self.file.readlines()
        for i in lines:
            booksInfo = i.strip().split(',')
            booksName = booksInfo[0]
            booksAuthor = booksInfo[1]
            print("**************************")
            print("Name of the book:", booksName)
            print("Name of the author:", booksAuthor)
            
    def addBooks(self):
        booksName = input("Please enter the Book Name: ")
        booksAuthor = input("Please enter the Author's Name: ")
        relaseYear = input("Please enter the Release Year: ")
        pageNumber = input("Please enter the Number of Pages: ")
        booksInfo = f"{booksName},{booksAuthor},{relaseYear},{pageNumber}\n"
        self.file.write(booksInfo)
        print("Congratulations book added!")


    def removeBook(self):
        whichBook = input("Please enter the book you want to remove: ")
        self.file.seek(0)
        lines = self.file.readlines()
        books = [line.strip() for line in lines]
        count = None
        for i, book in enumerate(books):
            if whichBook in book:
                count = i
                break
        if count is not None:
            del books[count]

            self.file.seek(0)
            self.file.truncate()

            for book in books:
                self.file.write(book + "\n")
            print("Congratulations book removed!")
        else:
            print("Book not found!")

lib = Library()

while True:

    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Please enter your choice (1-4): ")

    if choice == "1":
        lib.listBooks()
    elif choice == "2":
        lib.addBooks()
    elif choice == "3":
        lib.removeBook()
    elif choice == "4":
        print("Exiting the program. See you soon!..")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")