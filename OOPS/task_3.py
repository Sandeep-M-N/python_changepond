class BookStore:
    NoOfbooks=0

    def __init__(self):
        self.name=input("Enter the Name of the book: ")
        self.author=input("enter the author name: ")
        BookStore.NoOfbooks+=1
    
    def display(self):
        print("Name of the book is : ",self.name)
        print("Name of the author is : ",self.author)
        print("No of books is : ",BookStore.NoOfbooks)

def main():
    while True:
        books=BookStore()
        books.display()

if __name__=="__main__":
    main()