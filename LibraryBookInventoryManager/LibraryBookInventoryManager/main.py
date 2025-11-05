from library_manager import Library, Book

def main():
    library = Library()
    while True:
        print("\n=== Library Book Inventory Manager ===")
        print("1. Add Book")
        print("2. Search Book by Title")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show Report")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(Book(title, author))
        elif choice == "2":
            keyword = input("Enter title to search: ")
            library.search_book(keyword)
        elif choice == "3":
            title = input("Enter title to issue: ")
            library.issue_book(title)
        elif choice == "4":
            title = input("Enter title to return: ")
            library.return_book(title)
        elif choice == "5":
            library.report()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
