import random
import pickle
import sys


# This program is a data storage program that allows the user to
# store information in a way similar to a library.

# Can easily be refactored to store info other than books.

class Library:
    dict_of_books = {}

    def __init__(self):
        try:
            with open("book_registry.txt", 'rb') as book_registry:
                self.dict_of_books = pickle.load(book_registry)
        except FileNotFoundError:
            with open("book_registry.txt", 'wb') as book_registry:
                pickle.dump(self.dict_of_books, book_registry)
            with open("book_registry.txt", 'rb') as book_registry:
                self.dict_of_books = pickle.load(book_registry)
        self.main()

    def see_whole_registry(self):
        for genre, books in self.dict_of_books.items():
            for book in range(len(books)):
                books[book] = books[book].title()
            print(str(genre).capitalize(), ' : ', books)
            for book in range(len(books)):
                books[book] = books[book].lower()
        self.main()

    def clear_registry(self):
        self.dict_of_books.clear()
        print("Registry cleared.")

    def update_registry(self):
        with open("book_registry.txt", 'wb') as book_registry:
            pickle.dump(self.dict_of_books, book_registry)
        self.main()

    def remove_entry(self):
        book_genre = input("What genre is it?: ").lower()
        book_name = input("What book would you like to remove?: ").lower()
        try:
            self.dict_of_books[book_genre].remove(book_name)
            if not self.dict_of_books[book_genre]:
                self.dict_of_books.pop(book_genre, None)
                print("The genre: {0} is empty and was deleted.".format(book_genre))

        except ValueError:
            print("Book does not exist.")
        except KeyError:
            print("This Genre does not exist.")

    def add_to_library(self):
        book_genre = input("What genre is it?: ").lower()
        book_name = input("What book would you like to add?: ").lower()
        try:
            self.dict_of_books[book_genre].append(book_name)
        except KeyError:
            self.dict_of_books[book_genre] = book_name
            self.dict_of_books[book_genre] = [self.dict_of_books[book_genre]]

        print("{0} has been added to the registry under the genre of {1}.".format(book_name.title(), book_genre.title()))

    def search_library(self):
        book_name = input("What book would you like to find?: ").lower()
        found_book = [book for book in self.dict_of_books.values() if book_name in book]
        if not found_book:
            print("Book does not exist here.")
        elif found_book:
            for book in found_book:
                print("These books match your search: {0}".format(str(book).title()))
        self.main()

    def suggest_book(self):
        try:
            found_book = random.choice(random.choice(list(self.dict_of_books.values())))
            print("Suggested Book: {0}".format(found_book.title()))
        except IndexError:
            print("Library is empty! add some books.")

        self.main()

    def main(self):
        add_find_suggest_choice = input("Add/Find/Suggest/Clear/Remove/All/Exit: ")

        if "add" in add_find_suggest_choice.lower():
            self.add_to_library()
            self.update_registry()
        elif "find" in add_find_suggest_choice.lower():
            self.search_library()
        elif "suggest" in add_find_suggest_choice.lower():
            self.suggest_book()
        elif "clear" in add_find_suggest_choice.lower():
            self.clear_registry()
            self.update_registry()
        elif "remove" in add_find_suggest_choice.lower():
            self.remove_entry()
            self.update_registry()
        elif "all" in add_find_suggest_choice.lower():
            self.see_whole_registry()
        elif "exit" in add_find_suggest_choice.lower():
            sys.exit()
        else:
            print("Please choose a valid answer.")
            self.main()


if __name__ == "__main__":
    Library()
