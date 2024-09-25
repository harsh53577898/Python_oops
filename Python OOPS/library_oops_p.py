class LibraryBook:
    def __init__(self,book_name,author,assability):
        self.__book_name = book_name
        self.__author = author
        self.__assability = assability

    def get_book_name(self):
        return self.__book_name
    
    def get_author(self):
        return self.__author
    
    def is_assability(self):
        return self.__assability

    def borrow_books(self):
        if self.__assability :
            self.__assability = False
            print(f"you haved the borrowed the books {self.__book_name} by {self.__author}")
        else:
            print(f"This book is avaliable {self.__book_name} by {self.__author}")

    def return_books(self):
        if self.__assability:
            self.__assability = True
            print(f"You have returned the books {self.__book_name} by {self.__author}")
        else:
            print(f"You have not returned the books {self.__book_name} by {self.__author}")

book1 = LibraryBook("Harry potter","J.K.Rowling",True) 
book2 = LibraryBook("Games of Throne","George R.R.Martin",True)
book3 = LibraryBook("One Piece","Eiichiro Oda",True)

book1.borrow_books()
book2.borrow_books()
book3.borrow_books()
print()
book1.return_books()
book2.return_books()
book3.return_books()