# Student Life Manager

## 📌 Project Overview
The Student Life Manager is a command-line Python application designed to help students
track their academic performance and evaluate financial feasibility for a celebration expense.

This project was developed as part of a programming assignment and follows strict constraints
such as avoiding global variables and ensuring proper data flow through functions.

---

## 🧠 Features
- Accepts an indefinite number of grades
- Calculates and rounds the average grade
- Evaluates academic performance based on predefined thresholds
- Checks whether a celebration expense is affordable
- Displays a final formatted report

---

## 🧩 Program Structure
The program is organized using modular functions:

- `user_grades()` – Collects grades and returns total and count
- `average_calculator()` – Computes the rounded average
- `performance_evaluation()` – Determines academic status
- `expense_checker()` – Checks affordability
- `controller()` – Coordinates program execution

All data is passed through function parameters and return values.
No global variables are used.

---

## 🔄 Flowchart
The flowchart below illustrates the logical flow of the program:

![Flowchart](flowchart.png)

---

## ▶️ How to Run
1. Clone the repository
2. Run the program using:
   ```bash
   python main.py
