class Media:
    """
    Media class is the class from which all other classes inherit, it contains common
    attributes of classes Book, Magazine, PodcastEpisode and AudioBook.
    """
    def __init__(self, title, publish_year, language, price):
        self.title = title
        self.publish_year = publish_year
        self.language = language
        self.price = price
        self.status = "unread/unlistened"
        self.progress = 0

    def __str__(self):
        return f"title:{self.title}, publish_year:{self.publish_year}," \
               f" language:{self.language}, price:{self.price}$, status:{self.status}, progress:" \
               f"{self.progress}%"


class Book(Media):
    bookshelf = []     # a list to keep all instances instantiated from Book class

    def __init__(self, title, publish_year, language, price, pages, *authors):
        super().__init__(title, publish_year, language, price)
        self.pages = pages
        self.authors = authors
        self.readen_pages = 0

    def read(self, pages):
        """
        simulates user's reading action and updates the values of progress and
        readen_pages attributes
        :param pages:
        """
        if pages > self.pages:
            print(f"this book has just {self.pages} pages!")
        elif pages <= self.readen_pages:
            print("you have already read these pages!")
        elif pages == self.pages:
            print(f"congratulations! you have read {self.title} completely.")
            self.readen_pages = pages
        else:
            more_readen_pages = pages - self.readen_pages
            self.readen_pages = pages
            left_pages = self.pages - self.readen_pages
            print(
                f"you have read {more_readen_pages} more pages from {self.title}."
                f" There are {left_pages} pages left. ")
        self.progress = round(self.readen_pages / self.pages, 3) * 100

    def initialize_reading(self):
        """
        after a book is completely read and user wants to start reading it again, this method iniitiates
        the readen_pages attribute.
        """
        self.readen_pages = 0

    def get_status(self):
        if self.readen_pages == 0:
            self.status = "Unread"
        elif self.readen_pages == self.pages:
            self.status = "finished"
        else:
            self.status = "reading"
        return self.status

    @staticmethod
    def add_book():
        """
        inputs the attributes of a book from user and instantiates a Book class instance,
        then adds this instance to bookshelf list.
        """
        title = input("enter book's title: ")
        publish_year = input("enter book's publish year: ")
        language = input("enter book's language: ")
        price = input("enter book's price: ")
        number_of_pages = int(input("enter book's number of pages: "))
        authors = list(map(lambda x: x.strip(), input("enter book's authors: ").split(',')))
        book = Book(title, publish_year, language, price, number_of_pages, *authors)
        Book.bookshelf.append(book)

    def __str__(self):
        return f"{super().__str__()}, pages:{self.pages}, authors:{self.authors}"


class Magazine(Book):
    """
    Because of 6 common attributes between Book and Magazine classes, Magazine class
    inherits from Book class which itself inherits from Media class. it doesn't need
    to write get_status, read and initialize_reading methods because they are inherited.
    """
    magazines = []  # a list used to store all instances created from Magazine class

    def __init__(self, title, publish_year, language, price, pages, issue, *authors):
        super().__init__(title, publish_year, language, price, pages, *authors)
        self.issue = issue

    @staticmethod
    def add_magazine():
        """
        inputs the attributes of a magazine from user and instantiates a Magazine class
        instance. then adds it to the magazines list.
        """
        title = input("enter magazine's title: ")
        publish_year = input("enter magazine's publish year: ")
        language = input("enter magazine's language: ")
        price = input("enter magazine's price: ")
        number_of_pages = int(input("enter magazine's number of pages: "))
        issue = input("enter magazine's issue: ")
        authors = list(map(lambda x: x.strip(), input("enter book's authors: ").split(',')))
        magazine = Magazine(title, publish_year, language, price, number_of_pages, issue, *authors)
        Magazine.magazines.append(magazine)

    def __str__(self):
        return f"{super().__str__()}, issue:{self.issue}"


class PodcastEpisode(Media):
    podcast_episodes = []  # a list to store all instances made from PodcastEpisode class

    def __init__(self, title, publish_year, language, price, speaker, time):
        super().__init__(title, publish_year, language, price)
        self.speaker = speaker
        self.time = time
        self.listened_time = 0

    def listen(self, time):
        """
        simulates the listening action of the user and updates the listened_time and progress
        attributes.
        :param time:
        """
        if time > self.time:
            print(f"this podcast episode is just {self.time} minutes!")
        elif time <= self.listened_time:
            print("you have already listened to this part!")
        elif time == self.time:
            print(f"congratulations! you have read {self.title} completely.")
            self.listened_time = time
        else:
            more_listened_time = time - self.listened_time
            self.listened_time = time
            left_time = self.time - self.listened_time
            print(
                f"you have listened {more_listened_time} more minutes from {self.title}."
                f" There are {left_time} minutes left.")
        self.progress = round(self.listened_time / self.time, 2) * 100

    def initialize_listening(self):
        """
        after a podcast is completely listened and wants to listen to it again, it initializes
        the listened_time attribute.
        """
        self.listened_time = 0

    def get_status(self):
        if self.listened_time == 0:
            self.status = "not listened"
        elif self.listened_time == self.time:
            self.status = "finished"
        else:
            self.status = "listening"
        return self.status

    @staticmethod
    def add_podcast_episode():
        """
        creates a PodcastEpisode class instance from user input and adds it to
        the podcast_episodes list.
        """
        title = input("enter podcast episode's title: ")
        publish_year = input("enter podcast episode's publish year: ")
        language = input("enter podcast episode's language: ")
        price = input("enter podcast episode's price: ")
        speaker = input("enter podcast episode's speaker: ")
        time = int(input("enter podcast episode's time: "))
        podcast_episode = PodcastEpisode(title, publish_year, language, price, speaker, time)
        PodcastEpisode.podcast_episodes.append(podcast_episode)

    def __str__(self):
        return f"{super().__str__()}, speaker:{self.speaker}, time:{self.time} minutes"


class AudioBook(PodcastEpisode):
    """
    because of the six common attributes between classes AudioBook and
    PodcastEpisode, AudioBook inherits from PodcastEpisode class which itself
    inherits from Media class.
    """
    audio_books = []  # a list to store all instances made from AudioBook class

    def __init__(self, title, publish_year, language, price, speaker, time, pages, audio_language, *authors):
        super().__init__(title, publish_year, language, price, speaker, time)
        self.pages = pages
        self.audio_language = audio_language
        self.authors = authors

    @staticmethod
    def add_audio_book():
        """
        creates an instance of AudioBook class based on user inputs and adds
        it to the audio_books list
        """
        title = input("enter audio book's title: ")
        publish_year = input("enter audio book's publish year: ")
        language = input("enter audio book's language: ")
        price = input("enter audio book's price: ")
        speaker = input("enter audio book's speaker: ")
        time = int(input("enter audio book's time: "))
        pages = int(input("enter audio book's pages: "))
        audio_language = input("enter audio book's audio language: ")
        authors = list(map(lambda author: author.strip(), input("enter audio book's authors: ").split(",")))
        audio_book = AudioBook(title, publish_year, language, price, speaker, time, pages,
                               audio_language, *authors)
        AudioBook.audio_books.append(audio_book)

    def __str__(self):
        return f"title:{self.title}, publish_year:{self.publish_year}, book-language:{self.language}," \
               f" price:{self.price}$, status:{self.status}, speaker:{self.speaker}, time:{self.time}" \
               f" minutes, pages:{self.pages}," \
               f" audio-language:{self.audio_language}, authors:{self.authors}, progress:{self.progress}%"


def sort_items():
    """
    this function is used to sort all media based on the progress of user
    """
    media = []
    media.extend(Book.bookshelf)
    media.extend(Magazine.magazines)
    media.extend(PodcastEpisode.podcast_episodes)
    media.extend(AudioBook.audio_books)
    sorted_media = sorted(media, key=lambda x: x.progress, reverse=True)
    return sorted_media


while True:
    print('choose what you want to do:')
    print('1 add some new Media')
    print("2 show all shelves' items ")
    print('3 use a media')
    print('4 sort all shelf items based on progress')
    task = input()
    if task == '1':
        while True:
            print('which media do you want to add: ')
            media = input("1 book   2 magazine   3 podcast episode   4 audio book (type 'quit' to stop): ")
            if media == '1':
                Book.add_book()
            elif media == '2':
                Magazine.add_magazine()
            elif media == '3':
                PodcastEpisode.add_podcast_episode()
            elif media == '4':
                AudioBook.add_audio_book()
            elif media == 'quit':
                break

    elif task == '2':
        print("book shelf:")
        if Book.bookshelf:
            for book in Book.bookshelf:
                print(book)
        else:
            print("empty")
        print("magazine shelf:")
        if Magazine.magazines:
            for magazine in Magazine.magazines:
                print(magazine)
        else:
            print("empty")
        print("podcast episode shelf:")
        if PodcastEpisode.podcast_episodes:
            for pod in PodcastEpisode.podcast_episodes:
                print(pod)
        else:
            print("empty")
        print("audio book shelf:")
        if AudioBook.audio_books:
            for audio in AudioBook.audio_books:
                print(audio)
        else:
            print("empty")
    elif task == '3':
        print('which media do you want to use:')
        media = input("1 book   2 magazine   3 podcast episode   4 audio book: ")
        if media == '1':
            for num, book in enumerate(Book.bookshelf):
                print(num + 1, book.title)
            num = int(input('book number: '))
            if Book.bookshelf[num - 1].readen_pages == Book.bookshelf[num - 1].pages:
                Book.bookshelf[num - 1].initialize_reading()
            num_read_pages = int(input('how many pages did  you read? '))
            Book.bookshelf[num - 1].read(num_read_pages)
        elif media == '2':
            for num, magazine in enumerate(Magazine.magazines):
                print(num + 1, magazine.title)
            num = int(input('magazine number: '))
            if Magazine.magazines[num - 1].readen_pages == Magazine.magazines[num - 1].pages:
                Magazine.magazines[num - 1].initialize_reading()
            num_read_pages = int(input('how many pages did  you read? '))
            Magazine.magazines[num - 1].read(num_read_pages)
        elif media == '3':
            for num, pod in enumerate(PodcastEpisode.podcast_episodes):
                print(num + 1, pod.title)
            num = int(input('podcast episode number: '))
            if PodcastEpisode.podcast_episodes[num - 1].listened_time == \
                    PodcastEpisode.podcast_episodes[num - 1].time:
                PodcastEpisode.podcast_episodes[num - 1].initialize_listening()
            listened_time = int(input('how many minutes did  you listen? '))
            PodcastEpisode.podcast_episodes[num - 1].listen(listened_time)
        elif media == '4':
            for num, audio in enumerate(AudioBook.audio_books):
                print(num + 1, audio.title)
            num = int(input('audio book number: '))
            if AudioBook.audio_books[num - 1].listened_time == AudioBook.audio_books[num - 1].time:
                AudioBook.audio_books[num - 1].initialize_listening()
            listened_time = int(input('how many minutes did  you listen? '))
            AudioBook.audio_books[num - 1].listen(listened_time)
    elif task == '4':
        sorted_media = sort_items()
        for medium in sorted_media:
            if isinstance(medium, Magazine):
                print(f"magazine, title:{medium.title}, progress:{medium.progress}%")
            elif isinstance(medium, Book):
                print(f"book, title:{medium.title}, progress:{medium.progress}%")
            elif isinstance(medium, AudioBook):
                print(f"audio book, title:{medium.title}, progress:{medium.progress}%")
            elif isinstance(medium, PodcastEpisode):
                print(f"podcast episode, title:{medium.title}, progress:{medium.progress}%")
    else:
        print('wrong input! enter a number between 1 and 4:')
