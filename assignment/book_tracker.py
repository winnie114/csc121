def dashboard():
    print("=" * 40)
    print("📚   YOUR LIBRARY")
    print("=" * 40)

def estimate_reading_time(pages):
    reading_time = pages / 40
    return round(reading_time,1)

def add_book():
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)

    print("\nBook added:\n")
    print(f"'{title}' by {author} -- approx.{hours} hours to read")

def main():
    dashboard()
    add_book()

if __name__ == "__main__":
    main()

