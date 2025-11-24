# Hieu---Final-IT-project---Extra-Task-A

## Overview
This is a Python-based command-line application designed to help students manage their course data. It allows users to add courses, trace credits and scores, calculate their GPA, and persistently save data between sessions using a JSON file.

## Functions
* Add a Course: Input course details (Code, Name, Credits, Semester, Score).
* View Gradebook: Display all stored courses in a list format.
* Update a Course: Modify details for an existing course.
* Delete a Course: Remove a course from the gradebook by its code.
* Calculate GPA: Compute the weighted GPA based on credits and scores.
* Data Persistence: Automatically saves data to `gradebook.json` on exit and loads it upon startup.

## Prerequisites
* Python 3 installed on your system.

## How to Run
1. Download the `Gradebook.py` file to a folder on your computer.
2. Open your terminal or command prompt (CMD/PowerShell).
3. Navigate to the folder where you saved the file.
4. Run the application using the following command:
    ```bash
    python Gradebook.py
    ```
    
## Usage Guide
Once the application starts, use the number keys to navigate the menu:
* Enter **1** to Add a new course.
* Enter **2** to View all courses.
* Enter **3** to Calculate your GPA.
* Enter **4** to Delete a course (you will need the Course Code).
* Enter **5** to Update a course (you will need the Course Code).
* Enter **6** to Save and Exit the program.
* Enter **0** to Save manually without exiting.

## File Structure
* `Gradebook.py`: The main source code for the application.
* `gradebook.json`: The data file created automatically to store your course records.
