# Syntecxhub Python Internship Projects – Week 2

This repository contains **three Python CLI (Command Line Interface)** projects developed as part of the **Syntecxhub Python Programming Internship – Week 2 Task**.

Each project demonstrates strong understanding of **Object-Oriented Programming (OOP)**, **file handling**, and **real-world problem-solving using Python**.

---

## 📘 Project 1: Student Management System

### 🎯 Description
A simple CLI-based application to manage student records — add, list, and delete students.  
Data is stored in a JSON file for persistence.

### ⚙️ Features
- Add, update, delete, and list students  
- Unique ID validation  
- JSON-based file storage  
- Console-based interactive menu  

### ▶️ How to Run
```bash
cd StudentManagementSystem
python main.py

Example Output
=== Student Management System ===
1. Add Student
2. List Students
3. Delete Student
4. Exit
Enter your choice: 1
Enter Student ID: 101
Enter Name: Alice
Enter Grade: A
✅ Student added successfully!

Project 2: Library Book Inventory Manager
🎯 Description

A Python-based system to manage library books — including adding, searching, issuing, and returning books.
All records are saved to a JSON file.

⚙️ Features

Add books with title and author

Search for books by title

Issue and return books

Generate a summary report (total, issued, available)

Data persistence via JSON

▶️ How to Run
cd LibraryBookInventoryManager
python main.py

🧩 Example Output
=== Library Book Inventory Manager ===
1. Add Book
2. Search Book by Title
3. Issue Book
4. Return Book
5. Show Report
6. Exit
Enter your choice: 1
Enter book title: The Alchemist
Enter author name: Paulo Coelho
✅ Book added successfully!

Project 3: File Organizer Script
🎯 Description

A Python automation script that organizes files in a given folder by their extensions (PDF, JPG, DOCX, etc.).
It includes a dry-run mode to preview changes before execution and logs all file movements.

⚙️ Features

Organizes files by extension (creates subfolders automatically)

Dry-run mode (no files moved, just preview actions)

Handles duplicate file names safely

Logs all file operations to organizer.log

▶️ How to Run
cd FileOrganizerScript
python main.py

🧩 Example Output
=== File Organizer Script ===
Enter folder path to organize: C:\Users\Admin\Downloads
Enable dry-run mode? (yes/no): no
✅ Organization complete! 25 files moved.
