class Book:              #Contain attributes of book 


    def __init__(self,id,title,author,is_available=True):

        self.__id=id      #private attribute
        self.title=title
        self.author=author
        self.is_available=is_available


   
    def __str__(self):  #
        return f"ID: {self.__id}, Title: '{self.title}', Author: {self.author}\n"


    def get_id(self): # Encapsulation for ID => private attribute
        return self.__id
books = [
    Book(1, "The Hobbit", "J.R.R. Tolkien"),
    Book(2, "Harry Potter", "J.K. Rowling"),
    Book(3, "To Kill A Mockingbird", "Harper Lee"),
    Book(4, "Pride And Prejudice", "Jane Austen"),
    Book(5, "The Catcher In The Rye", "J.D. Salinger"),
    Book(6, "The Great Gatsby", "F. Scott Fitzgerald"),
    Book(7, "Moby Dick", "Herman Melville"),
    Book(8, "War And Peace", "Leo Tolstoy")
]
def isAvailable(bokTitle): # check if the book exist or no??

    for book in books:

           if book.title==bokTitle and book.is_available:
             
               return True

   
    return False

    


class User():

     def __init__(self,id_user,name): #this is the parent class to apply inheritance

        self.id_user=id_user

        self.name=name

     def getInfo(self):              # to get the info of user member or librarian

         return f"-Name is: {self.name}\n-User ID: {self.id_user}\n"


class Member(User):                 # This class responsible operations belong to the member 
                                    # borrow books and return it after end from it

      def __init__(self, id_user,name ):

         super().__init__( id_user,name)

         self.borrowed_books = [] 

      

      def borrowBook(self,bokkk):

          

        if isAvailable(bokkk):

           for i,b in enumerate (books):

               if b.title==bokkk:

                  self.borrowed_books.append(b)

                  del books[i]

                  return f"\nThis book {b.title} has been borrowed by you now"

       
        return f"\nThis book {bokkk} isnot exist now"

      def returnBook(self,Title):


          
          for book in self.borrowed_books:


                if book.title==Title:

                   self.borrowed_books.remove(book)

                   book.is_available=True

                   books.append(book)
       
                   return f"\nThis book {Title} has returned\nThank you my dear."

          return f"\nThis book {Title} already exist or it doesn't belong to our library \nPlease try again .."


class Librarian(User):                 # librarian responsible for adding and removing members and books 
                                       # and show available books and the members
                                       
    
    def __init__(self, id_user,name ):

        super().__init__( id_user,name)

        self.mmber=[User(0,"default")]

    def find_member_by_id(self, member_id):

        for member in self.mmber:

            if member.id_user == member_id:

                return member.name

        return None

    def addBook(self,idBook,nameBook,authorBook):

         f2=True
         for book in books:

             if book.get_id() == idBook:

                 f2=False

                 return f"\nThis ID {idBook} already exist..Enter the ID on the book "

         if f2:
             books.append(Book(idBook,nameBook,authorBook))
             return f"\nThis book {nameBook} has added "

    def removeBook(self,iddBook):

        f3=True

        for book in books:

             if book.get_id()==iddBook:

                 books.remove(book)

                 f3=False

                 return f"\nThis book {book.title} has removed"
                 
        if f3:

              return f"\nThis book with {iddBook} ID already not exist "

    
    def addMember(self,id_user,name):

          f1=True

          for userr in self.mmber:

             if userr.id_user==id_user:

                 f1=False

                 return "\nThis user already exist "
          if f1:
               
               self.mmber.append(User(id_user,name)) 

               return f"\nUser {name} with ID {id_user} has been added"

    def removeMember(self,id_user,name):

          

          for userr in self.mmber:

             if userr.id_user==id_user and userr.name==name:

                 self.mmber.remove(userr) 

                 return f"\nUser {name} with ID {id_user} has been removed"

                
          
          return "\nThis user isnot exist "
        
    def display_all_current_books(self):

         if not books:

             print("\nThere isnot books !!")
         else:
             print("\nAvailable books is: ")
             for Bok in books:

                 print(f"- ID = {Bok.get_id()} / Title = {Bok.title} by {Bok.author}")

         print("\n")
    def display_all_members(self):
         
         
         
         if not self.mmber:

             print("\nThere isnot members !!")

         else:
             print("\nMembers is: ")
             for Member in self.mmber:

                 if Member.id_user==0:
                     continue

                 print(f"-{Member.getInfo()}")
         
                 print("-" * 30)
                 print("\n")



def display_main_menu():                 #show the menu
    print("\n======= Main menu =======")
    print("<1> Register as a librarian")
    print("<2> Register as a member")
    print("<3> Exit")
    choice=int(input("Enter your choice : "))
    return choice

def display_librarian_menu():           #show the menu of librarian and what he does

    print("\n===== Librarian's List =====")
    print("<1> Add Book")
    print("<2> Remove Book")
    print("<3> Add Member ")
    print("<4> Remove Member")
    print("<5> Display available books")
    print("<6> View members list")
    print("<7> Return to the main menu")
    choic=int(input("Enter your choice : "))
    return choic

def display_member_menu(member_name):               #show the menu of member and what he does

    print(f"\n===== Member list {member_name}  =====")
    print("<1> Borrow Book")
    print("<2> Return Book")
    print("<3> List of borrowed books")
    print("<4> view available books ")
    print("<5> return to the main menu ")
    choose = int(input("Enter your choice : "))
    return choose


print("=" * 60)
print("📚  WELCOME TO  📚".center(60))
print("✨ LIBRARY SYSTEM MANAGEMENT ✨".center(60))
print("=" * 60)


def run_library_app():

    librarian=Librarian(152,"Mayer Adel")
    members=Member(165,"Sara Kamel")
    librarian.addMember(165,"Sara Kamel")

    while True:

        main_menu=display_main_menu()

        if main_menu==1:

           print("\n===== Librarian login =====\n")

           while True:

                  i_d=int(input("\n-Enter your ID from 3 digits please : "))

                  if i_d==librarian.id_user:

                        print(f"\nHow are you mr/mrs {librarian.name}")

                        break
                  else:

                        print("\nInvalid ID try again !!")


        #display_librarian_menu()

           while True:

              librarian_menu=display_librarian_menu()

              if librarian_menu==1:

                  book_idd=int(input("\nEnter ID of The book : "))
                  
                  book_title=input("\nEnter title of The book : ").capitalize()
                  
                  book_author=input("\nEnter author of The book : ").title()
                  
                  print(librarian.addBook(book_idd,book_title,book_author))

              elif librarian_menu==2:

                  book_idd=int(input("\nEnter ID of the book to remove it : "))
                  
                  print(librarian.removeBook(book_idd))
                  
              elif librarian_menu==3:

                  idd_usr=int(input("\nEnter ID of the user to add : "))
                  
                  namme=input("\nEnter his/her first & second name to add : ").title()
                  
                  print(librarian.addMember(idd_usr,namme))

              elif librarian_menu==4:
               
                  idd_usr=int(input("\nEnter ID of the user to remove ! : "))
                  
                  namme=input("\nEnter his or her name, provided that the first letter is a capital letter : ").title()
                  
                  print(librarian.removeMember(idd_usr,namme))

              elif librarian_menu==5:

                  librarian.display_all_current_books()

              elif librarian_menu==6:

                  librarian.display_all_members()

              else:

                  break
        elif main_menu==2:

            print("\n========= Member Login =========")

            idd_Ysr=int(input("\nEnter your ID : "))

            current_mm=librarian.find_member_by_id(idd_Ysr)
        
            if current_mm:
               while True:
                
                        
                     member_menu=display_member_menu(librarian.find_member_by_id(idd_Ysr))

                     

                     if member_menu==1:

                        bok=input("\nEnter title of the book : ").title()

                        print(members.borrowBook(bok))

                     elif member_menu==2:

                         bokk=input("\nEnter title of the book you have : ").title()

                         print(members.returnBook(bokk))

                     elif member_menu==3:

                         if not members.borrowed_books:
                                print("\nNo books borrowed yet")
                         else:
                                print("\n Your borrowed books:")
                                for book in members.borrowed_books:
                                    print(f"- {book}")
  
                     elif member_menu==4:

                         librarian.display_all_current_books()

                     elif member_menu==5:
                         break

                     else:

                         print("\nInvalid choice Please try again..")

            else:

                      print("\nInvalid ID try again..")

        elif main_menu==3:

            print("\nThank you for using our system ^_^\n\nGood bye ..\n")
            break

        else:

            print("Invalid choice Please try again..\n")

run_library_app()