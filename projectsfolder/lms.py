class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book_name):
        self.books.append(book_name)
        print(f"'{book_name}'added to library")
 library = Library()
 library.add_book("python book")
 library.add_book("java book")           
    
    