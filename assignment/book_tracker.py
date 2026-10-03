def dashboard():
    print("=" * 40)
    print("📚   YOUR LIBRARY")
    print("=" * 40)

def estimate_reading_time(pages):
    reading_time = pages / 40
    return round(reading_time,1)

def show_menu():
    print("\nWhat would you like to do?")
    print()
    print("1) View books")
    print("2) Add a book")
    print()
    print("q) Quit")
    print()

    choice = input("> ")
    return choice.strip().lower()

def add_book(library):
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)

    book = {
        "title": title,
        "author": author,
        "pages": pages,
        "hours": hours
    }

    library.append(book)

    print("\nBook added:\n")
    print(f"'{title}' - {author} ({pages} pages - approx. {hours} hours to read)")

def view_books(library):
    if not library:
        print("\nYour library is empty. Add a book first!")
    else:
        print("\nHere are your books:")

        for i in range(len(library)):
            book = library[i]
            print(f"{i + 1}. '{book['title']}' - {book['author']} ({book['pages']} pages - approx. {book['hours']} hours to read)")

def main():
    library = []
    dashboard()

    while True:
        choice = show_menu()
        if choice == "1":
            view_books(library)
        elif choice == "2":
            add_book(library)
        elif choice in ["q", "quit", "exit"]:
            print("Goodbye!")
            break
        else:
            print("Sorry, that option isn't available.")

if __name__ == "__main__":
    main()

