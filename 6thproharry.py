class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def showBooks(self):
        if not self.books:
            print("No books in the library")
        else:
            for books in self.books:
                print(books)
    def showInfo(self):
        print(f"The library has {self.noBooks} books")
        
l1=Library()
l1.addBook("Harry Potter")
l1.addBook("Star Wars")
l1.addBook("Marvel Comics")
l1.addBook("DC Comics")
l1.addBook("Believe Me")

l1.showBooks()
l1.showInfo()


print("\nStopping the program...")
del l1  # delete the Library object

# Create a new Library object to demonstrate that books are not persisted
l2 = Library()
print("\nAfter restarting the program:")
l2.showBooks()  # this should print nothing
l2.showInfo()  # this should print "The library has 0 books"