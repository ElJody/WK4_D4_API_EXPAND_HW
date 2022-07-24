
import ApiFuncs
import BookFuncs
from getpass import getpass
import time
from IPython.display import clear_output


class UI():
    def login(email):
        clear_output()
        password = getpass("Password: ")
        user = ApiFuncs.login_user(email, password) 
        print(user)
        time.sleep(3)
        return user

    def delete_account(user):
        ApiFuncs.delete_user(user['token'])
        time.sleep(4)

    def register():
        clear_output()
        print("Registration:")
        email = input("Email: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        password = input("Password: ")
        
        user_dict={
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
            "password":password
        }
        return ApiFuncs.register_user(user_dict)

    def edit(user):
        prompt = input('Type in One of The Following Edit Options: First Name, Last Name, or Password to Edit.\n')
        if prompt.lower() == "first name":
            first = input('Enter a New First Name: \n')
            edit_payload={
            "first_name":first,           
            }
            return ApiFuncs.edit_user(user['token'], edit_payload)            
            
        elif prompt.lower() == 'last name':
            last = input('Enter a New Last Name: \n')
            edit_payload={
            "last_name":last,           
            }
            return ApiFuncs.edit_user(user['token'], edit_payload)

        elif prompt.lower() == 'password':
            password = input('Enter a New Password: \n')
            edit_payload={
            "password":password,           
            }            
            return ApiFuncs.edit_user(user['token'], edit_payload)

def main():
    reading_list = BookFuncs.ReadingList()
    books = ApiFuncs.get_books()
    user = {}
    
    while True:
        clear_output()
        print("Welcome to the Bookstore")
        email = input("Type Your Email to Login or Type `register` to Register ")
        if email == 'register':
            success_register = UI.register()
            if success_register:
                print(f"{user['first_name'].title()}, you have successfully registered")
                time.sleep(3)
                continue
            else:
                print("Failed to register")
                time.sleep(3)
        elif email.lower() == "quit":
            print(f"Goodbye {user['first_name'].title()}")
            break
        else:
            try:
                user = UI.login(email)
            except:
                print("Invalid Username/Password combo")
                time.sleep(2)
                continue
        # First Scene of our app (above)

        while True:
            clear_output()
            print("""
Welcome to the Repository            
You can:            
1. Browse All Books
2. Browse Book by Category
3. View Reading List
4. Remove Book From Reading List
5. Edit Account    
6. Delete Account
7. Quit
""")
            command = input(f"Hi, {user['first_name'].title()} - Please Choose an Option. ")
            if command == "1":
                BookFuncs.browse_books(books, reading_list)

            elif command == "2":
                while True:
                    print(" | ".join(BookFuncs.get_category_list(books)))
                    cat = input("Category: ").title()
                    if cat in BookFuncs.get_category_list(books):
                        BookFuncs.browse_books(books, reading_list, cat)
                        break
                    print("Invalid Category")
                    time.sleep(2)
                    continue

            elif command == "3":
                reading_list.show_book_list()
                input("Press Enter To Return")
                continue

            elif command == "4":
                while True:
                    clear_output()
                    reading_list.show_book_list()
                    garbage = input(f"What Book ID Would You Like to Remove, {user['first_name'].title()}? or Enter 'BACK' to back out ")
                    if garbage.lower() == "back":
                        break
                    elif garbage.isnumeric() and int(garbage) in map(lambda book: book['id'], reading_list.reading_list):
                        reading_list.remove_book(list(filter(lambda book: book['id']==int(garbage), reading_list.reading_list))[0])
                        print(f'{garbage} has been removed')
                        time.sleep(2)
                        break
                    else:
                        print(f"{user['first_name'].title()}, {garbage} is Not in Your Collection")
                        time.sleep(2)
                        break
                continue   
                    
            elif command == "5":
                if UI.edit(user):
                    print('Your Edit Was Successful.')
                    time.sleep(2)
                    continue

            elif command == "6":
                prompt = input("Type 'delete' to Delete Your Account.\n")
                if prompt.lower() == "delete":
                    prompt = input('Please Enter Email.\n')
                    if UI.delete_account(user):
                        print(f"Sorry to See You go {user['first_name'].title()}, Bye-Bye!")
                    break
                else:
                    continue

            elif command == "7":
                print("Goodbye")
                break
            else:
                print("Invalid Selection")
                time.sleep(2)
                continue
        break   


main() 