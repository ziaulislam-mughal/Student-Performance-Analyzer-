# 🎓 Student Performance Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A robust, console-based application designed to manage student academic records, calculate complex grades, and visualize performance statistics using Object-Oriented Programming (OOP) principles.

---

## 🚀 Overview

This project is a modular **Student Performance Analyzer** built in Python. It allows instructors to efficiently manage student data, automate grade calculations based on weighted assessments, and generate insightful statistical reports.

The system features a **persistence layer** using CSV file handling, ensuring data is saved and loaded automatically. It also includes a **Bonus Visualization Dashboard** that uses ANSI escape codes to render colorful grade distribution charts directly in the terminal.

## ✨ Key Features

* **📚 CRUD Operations:** Add, Remove, Update, and Search specific student records instantly.
* **🧮 Automated Grading Engine:** Calculates Final Scores and Letter Grades based on custom weighted logic:
    * *Formula:* `(0.4 × Midterm) + (0.5 × Final) + (0.1 × Assignment)`
* **💾 Data Persistence:** Implements robust File I/O to load/save data from `students.csv` automatically on startup and exit.
* **📊 Statistical Reporting:** Generates a class report including:
    * Highest & Lowest scores.
    * Class Average.
    * Top Performers (Sorted List).


## 🛠️ Technical Implementation

This project demonstrates proficiency in the following core Computer Science concepts:

* **Object-Oriented Programming (OOP):** Encapsulation of student data and behaviors within a `Student` class.
* **Data Structures:** Usage of Lists and Dictionaries for efficient memory management.
* **File Handling:** CSV reading/writing with exception handling (`try/except`) for error-proof execution.
* **Algorithm Design:** Sorting algorithms and aggregation logic for generating statistical reports.

## ⚙️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ziaulislam-mughal/Student-Performance-Analyzer-.git
    ```
2.  **Navigate to the directory:**
    ```bash
    cd Student-Performance-Analyzer-
    ```
3.  **Run the application:**
    ```bash
    python student_analyzer.py
    ```



## 📝 Grading Logic

The system assigns letter grades based on the calculated Final Score:

| Score Range | Grade |
| :--- | :---: |
| **85 - 100** | A |
| **70 - 84** | B |
| **55 - 69** | C |
| **40 - 54** | D |
| **Below 40** | F |

## 👨‍💻 Author

**Zia ul islam Mughal**
* **Course:** Programming for AI
* **Instructor:** Professor Dr. Wajid Arshad Abbasi

---
*Developed as part of Assignment #01 for the Analysis of Algorithms/Programming module.*
