class BookStore:

    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1
    
    def display(self):
        print(f"#{self.Name} by {self.Author}. No of Books: {BookStore.NoOfBooks}")
        return
    
Obj1 = BookStore("Gulliver's Travels","Jonathan Swift")
Obj1.display()
Obj2 = BookStore("C Programming","Dennis Ritchie")
Obj2.display()
Obj3 = BookStore("Linux System Programming","Robert Love")
Obj3.display()
