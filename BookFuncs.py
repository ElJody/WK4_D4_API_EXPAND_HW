import ApiFuncs
import time
from IPython.display import clear_output
from IPython.display import Image
from IPython.display import display


class BookFuncs():
    def get_book_by_id(books, id):
        return list(filter(lambda book: book['id']==id, books))[0]

    def get_category_list(books):
        return {book['subject'].title() for book in books}

    def get_book_by_category(books, category):
        return list(filter(lambda book: book['subject'].title()==category.title(),books))

    def display_book_cover(book):
        cover = Image(url=book['img'])
        display(cover)

    def display_book_short(book):
        print(f"{book['id']} \t| {book['title'][:50].ljust(50)} | \t{book['subject']}")

    def display_book_long(book):
        cover = ApiFuncs.Image(url=book['img'])
        ApiFuncs.display(cover)
        print(f'''
Title:\t {book['title']}
Author: {book['author']}
Pages:\t {book['pages']}
Subject: {book['subject']}
Summary: {book['summary']}
''')

    def show_small_book_list(self):
        if not self.reading_list:
            print("Your reading list is empty")
        else:
            for book in self.reading_list:
                BookFuncs.display_book_short(book)

    def browse_books(books, reading_list, subject=None):
        while True:
            clear_output()
            print(f'''
Welcome to the Book Browser
You are viewing {subject if subject else 'all'} books
[ID] \t| {"[TITLE]".ljust(50)} | [SUBJECT]
        ''')
            if subject:
                books= BookFuncs.get_book_by_category(books, subject)
            for book in books:
                BookFuncs.display_book_short(book)

            selection = input("Select your book by ID or Type 'BACK' to back out.")
            if selection.lower()=='back':
                return
            elif selection.isnumeric() and int(selection) in map(lambda book: book['id'], books):
                selection=int(selection)
                selected_book = BookFuncs.get_book_by_id(books, selection)
                while True:
                    print(f'''
You Selected: {selected_book['title']}
1. Add Book To Reading List
2. View More Information
3. Go Back
4. Go To Main Menu
''')
                    action = input("Action: ")
                    if action =="1":
                        reading_list.add_book(selected_book)
                        print("As you wish")
                        time.sleep(3)
                        break
                    elif action =="2":
                        clear_output()
                        BookFuncs.display_book_long(selected_book)
                        input("Press Enter To Continue")
                    elif action=="3":
                        break
                    elif action=="4":
                        return
                        
            else:
                print("Invalid ID")
                time.sleep(2)
                continue

class ReadingList():
    def __init__(self):
        self.reading_list=[]
        
    def add_book(self, book):
        if book not in self.reading_list:
            self.reading_list.append(book)
    
    def remove_book(self, book):
        self.reading_list.remove(book)
    
    def empty(self):
        self.reading_list=[]
    
    def show_book_list(self):
        clear_output()
        if not self.reading_list:
            print("Your reading list is empty")
        for book in self.reading_list:
            print(f'''
{"="*50}            
\n
Title:\t {book['title']}
Book ID: {book['id']}
Author:\t {book['author']}
Subject: {book['subject']}
Summary: {book['summary']}
\n
{"="*50}            
\n
''') 