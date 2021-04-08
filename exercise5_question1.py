
class Book:
    bookshelf = []  # a list to store all instances made from Book class

    def __init__(self, title, publish_year, number_of_pages, language, price, *authors):
        self.title = title
        self.publish_year = publish_year
        self.number_of_pages = number_of_pages
        self.language = language
        self.price = price
        self.authors = authors
        self.readen_pages = 0
        self.status = None

    def read(self, pages):
        """
        it prints a message based on number of pages read by
        user and sets the value of readen_pages attribute.
        :param pages:
        :return:
        """
        if pages > self.number_of_pages:
            print(f"this book has just {self.number_of_pages} pages!")
        elif pages <= self.readen_pages:
            print("you have already read these pages!")
        elif pages == self.number_of_pages:
            print(f"congragulations! you have read {self.title} completely.")
            self.readen_pages = pages
        else:
            more_readen_pages = pages - self.readen_pages
            self.readen_pages = pages
            left_pages = self.number_of_pages - self.readen_pages
            print(
                f"you have read {more_readen_pages} more pages from {self.title}. There are {left_pages} pages left. ")

    def initialize_reading(self):
        """
        it is used when the user has read a book and wants to read it again.
        :return:
        """
        self.readen_pages = 0

    def get_status(self):
        if self.readen_pages == 0:
            self.status = "Unread"
        elif self.readen_pages == self.number_of_pages:
            self.status = "finished"
        else:
            self.status = "reading"
        return self.status

    @staticmethod
    def add_book(num_books):
        """
        creats a Book class instance based on user inputs and adds it to the bookshelf list.
        :param num_books:
        :return:
        """
        for num in range(num_books):
            title = input("enter book's title: ")
            publish_year = input("enter book's publish year: ")
            number_of_pages = int(input("enter book's number of pages: "))
            language = input("enter book's language: ")
            price = input("enter book's price: ")
            authors = list(map(lambda x: x.strip(), input("enter book's authors: ").split(',')))
            book = Book(title, publish_year, number_of_pages, language, price, *authors)
            Book.bookshelf.append(book)

    def __str__(self):
        return f"'{self.title}' written by {self.authors} published in {self.publish_year} in {self.language} language" \
               f" with the price of {self.price}$ and contains {self.number_of_pages} pages"


while (True):
    print('choose what you want to do:')
    print('1 add some new books')
    print('2 show my bookshelf')
    print('3 read a book')
    print('4 get status of a book')
    task = input()
    if task == '1':
        num_books = input('please enter number of books you want to add: ')  # user can enter several books
        Book.add_book(int(num_books))
    elif task == '2':
        for book in Book.bookshelf:
            print(book)
    elif task == '3':
        print('which book do you want to read:')
        for num, book in enumerate(Book.bookshelf):
            print(num + 1, book.title)
        num = int(input('book number: '))
        if Book.bookshelf[num - 1].readen_pages == Book.bookshelf[num - 1].number_of_pages:
            Book.bookshelf[num - 1].initialize_reading()
        num_read_pages = int(input('how many pages did  you read? '))
        Book.bookshelf[num - 1].read(num_read_pages)
    elif task == '4':
        print('which book do you want to read:')
        for num, book in enumerate(Book.bookshelf):
            print(num + 1, book.title)
        num = int(input('book number: '))
        status = Book.bookshelf[num - 1].get_status()
        print(status)
    else:
        print('wrong input! enter a number between 1 and 4:')
