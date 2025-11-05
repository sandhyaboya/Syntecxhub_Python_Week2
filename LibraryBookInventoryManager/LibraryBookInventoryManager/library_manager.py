import json

class Book:
    def __init__(self, title, author, issued=False):
        self.title = title
        self.author = author
        self.issued = issued

class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, book):
        if any(b["title"].lower() == book.title.lower() for b in self.books):
            print("❌ Book already exists!")
            return
        self.books.append({"title": book.title, "author": book.author, "issued": book.issued})
        self.save_books()
        print("✅ Book added successfully!")

    def search_book(self, keyword):
        found = [b for b in self.books if keyword.lower() in b["title"].lower()]
        if found:
            print("\n🔍 Search Results:")
            for b in found:
                status = "Issued" if b["issued"] else "Available"
                print(f"Title: {b['title']} | Author: {b['author']} | Status: {status}")
        else:
            print("❌ No book found with that title.")

    def issue_book(self, title):
        for b in self.books:
            if b["title"].lower() == title.lower():
                if b["issued"]:
                    print("⚠️ Book already issued!")
                else:
                    b["issued"] = True
                    self.save_books()
                    print("📚 Book issued successfully!")
                return
        print("❌ Book not found!")

    def return_book(self, title):
        for b in self.books:
            if b["title"].lower() == title.lower():
                if not b["issued"]:
                    print("⚠️ Book was not issued!")
                else:
                    b["issued"] = False
                    self.save_books()
                    print("✅ Book returned successfully!")
                return
        print("❌ Book not found!")

    def report(self):
        total = len(self.books)
        issued = sum(1 for b in self.books if b["issued"])
        available = total - issued
        print(f"\n📊 Library Report:\nTotal Books: {total}\nIssued: {issued}\nAvailable: {available}")
