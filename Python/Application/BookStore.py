# Assignemnt 6_1        
class BookStore:

    noOfBooks = 0

    def __init__(self):
        self.name = input("Enter Book's Name : ")
        self.author = input("Enter Author's Name : ")
        BookStore.noOfBooks = BookStore.noOfBooks + 1

    def Display(self):

        print("Name of Book is : ",self.name)
        print("Name of Author is : ",self.author)
        print("Number of Books : ",BookStore.noOfBooks)

def main ():

    Obj1 = BookStore()
    Obj1.Display()
    
    Obj2 = BookStore()
    Obj2.Display()
    

if __name__=="__main__":
    main()