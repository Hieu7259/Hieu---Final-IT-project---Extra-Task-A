import json

Gradebook = []

def add_course():

    Course_code = input("Enter your course code here: ")

    Course_name = input("Enter your course name here: ")

    Credits = int(input("Enter your credits number: "))

    Semester = (input("Enter your semester: "))

    Score = float(input("Enter your score: "))

    Course = [Course_code, Course_name, Credits, Semester, Score]

    Gradebook.append(Course)
    
    print("Your course has been successfully added to the gradebook")

def view_gradebook():
    print("\n--- MY GRADEBOOK ---")
    for Course in Gradebook:
        print(Course)


def GPA_Calculation():
    print("\n--- Your GPA ---")
    total_points = 0
    total_credits = 0
    for Course in Gradebook:
        total_credits = total_credits + Course[2]
        total_points = total_points + (Course[2] * Course[4])
    
    if total_credits > 0:
        GPA = total_points / total_credits / 100 * 4
        print("Your GPA is:", GPA)
    else:
        print("No credits found. GPA is 0.0")


def delete_course():
    print("\n---Delete a saved course---")
    Delete = input("Enter the code of the course you want to delete here: ")
    for Course in Gradebook:
       
        if Delete == Course[0]:
            Gradebook.remove(Course)
            print("Your course has been successfully removed")
        else:
            print("No course found")

def update_course():
    print("\n--- Update a saved course ---")
    Update = input("Enter the code of the course you want to update here: ")
    for Course in Gradebook:

        if Update == Course[0]:
            Course[1] = input("Enter your new course name here: ")
            Course[2] = int(input("Enter your new course credits here: "))
            Course[3] = input("Enter your new course semester here: ")
            Course[4] = float(input("Enter your new course score here: "))
            print("Your course has been successfully updated")
        else: 
            print("No course found")

def save_gradebook():
    with open("gradebook.json", "w") as file:
        json.dump(Gradebook, file)
        print("Your course data has been succesfully saved to gradebook.json")

def load_gradebook():
    global Gradebook 

    try:
        with open("gradebook.json", "r") as file:
            Gradebook = json.load(file)
            print("Loading saved course data successfully.")
    except FileNotFoundError:
        print("No save file found. Starting with an empty gradebook.")

load_gradebook()

while True: 
    print("\n--- GRADEBOOK MENU ---")
    print("1. Add Course")
    print("2. View your Gradebook")
    print("3. Calculate your GPA")
    print("4. Delete a saved course")
    print("5. Update a saved course")
    print("6. Exit")
    print("0. Save your data to gradebook")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_course()  
    
    elif choice == "2":
        view_gradebook()
    
    elif choice == "3":
        GPA_Calculation()
    
    elif choice == "4":
        delete_course()
    
    elif choice == "5":
        update_course()
    
    elif choice == "0":
        save_gradebook()
        
    elif choice == "6":
        print("See you next time1!")
        break    
    else:
        print("Invalid choice.")
