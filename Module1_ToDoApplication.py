#To Do Application
def task_menu():  #print To-Do List Menu
    print("\nTo-Do List Application")
    print("Enter 1 to ADD a task")
    print("Enter 2 to VIEW all tasks")
    print("Enter 3 to DELETE a task")
    print("Enter 4 to QUIT the application")

def add_task(tasks): #function to add a task in the tasks list
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task {task} added successfully.")

def view_task(tasks): #function to view list of tasks in the tasks list
    if not tasks:
        print("No tasks in your list.")
    else:
        print("\nTo-Do List:")
        for task in tasks:
            print(task)

def remove_task(tasks): #function to remove a task in the tasks list
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task {task} removed successfully.")
    else:
        print(f"Task {task} not found.")

def main(): #main function to run functions based on users input from display menu    
    print("Welcome!  Let's create your to-do list...")
    tasks = []
    while True:
        task_menu() #displays To-Do List Menu
        try:  #read input to see if value is 1-4
            choice = int(input("Enter your choice: "))
            if 1<= choice <=4:    
                if choice == 1:
                    add_task(tasks)
                elif choice == 2:
                    view_task(tasks)
                elif choice == 3:
                    remove_task(tasks)
                elif choice == 4:
                    print("Quit the application.")
                    break
            else: #error handling for any number not 1-4
                print(f"Invalid choice.  Please try again.")
        except ValueError: #Value Error exception if value is invalid
            print("Invalid input.  Please enter a valid choice.")
        finally: #prints each time main function runs
            print('Thank you!')
   
            
if __name__ == "__main__":
    main()  #run main when program starts