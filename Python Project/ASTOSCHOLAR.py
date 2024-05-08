"ASTROSCHOLAR"
"task management"
tasks = []

def add_task(task):
    tasks.append(task)
    print("Your task has added successfully.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(" Your task has removed successfully.")
    else:
        print("You didn't have any task")

def view_tasks():
    if len(tasks) > 0:
        print(" Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("You didn't have any task")

def main_menu():
    while True:
        print("\nTask Management\n")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Give your choice (1-4): ")

        if choice == "1":
            task = input("Give your task: ")
            add_task(task)
        elif choice == "2":
            task = input("Which task has to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Please try again.")

if __name__ == "__main__":
    main_menu()

"TMETABLE SCHEDULING"  
class Course:
    def __init__(self, name, days, start_time, end_time):
        self.name = name
        self.days = days
        self.start_time = start_time
        self.end_time = end_time

class Timetable:
    def __init__(self, month):
        self.month = month
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print("Course added successfully.")

    def schedule(self):
        timetable = [["" for _ in range(7)] for _ in range(12)]  # 5 days, 8 time slots

        for course in self.courses:
            for day in course.days:
                for i in range(course.start_time, course.end_time):
                    timetable[i][day - 1] = course.name

        return timetable

def print_timetable(timetable, month):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    times = ["01:00", "02:00", "03:00", "04:00", "05:00","06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00"]

    print(f"Timetable for {month}:")
    print("Time  | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday")
    print("-------------------------------------------------------------------------------")
    for i, time in enumerate(times):
        print(f"{time} |", end=" ")
        for j, day in enumerate(days):
            print(f"{timetable[i][j]:<8}|", end=" ")
        print()

# Example usage
if __name__ == "__main__":
    month = input("Enter the month: ")

    timetable = Timetable(month)

    while True:
        course_name = input("Enter the course name (or 'q' to quit): ")
        if course_name == "q":
            break

        days_input = input("Enter the days for the course (comma-separated, e.g., 1,2,3): ")
        days = [int(day.strip()) for day in days_input.split(",")]

        start_time = int(input("Enter the start time (in 24-hour format, e.g., 8, 13): "))
        end_time = int(input("Enter the end time (in 24-hour format, e.g., 10, 15): "))

        course = Course(course_name, days, start_time, end_time)
        timetable.add_course(course)

    generated_timetable = timetable.schedule()
    print_timetable(generated_timetable, month)



"NOTES TAKING"
class Note:
        def __init__(self, title, content):
            self.title = title
            self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        print("Note added successfully.")

    def view_notes(self):
        if self.notes:
            print("Notes:")
            for i, note in enumerate(self.notes):
                print(f"{i + 1}. {note.title}")
        else:
            print("No notes found.")

def main_menu():
    note_manager = NoteManager()

    while True:
        print("\nNote Taking\n")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Give your choice (1-3): ")

        if choice == "1":
            title = input("Note title: ")
            content = input("Note content: ")
            note = Note(title, content)
            note_manager.add_note(note)
        elif choice == "2":
            note_manager.view_notes()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Please try again.")

if __name__ == "__main__":
    main_menu()

"REMAINDER"

import time
import pickle

class Reminder:
    def __init__(self, task, duration):
        self.task = task
        self.duration = duration

def set_reminder():
    task = input("Enter the task you want to be reminded: ")
    duration_hours = int(input("Enter the duration in hours: "))
    duration_minutes = int(input("Enter the duration in minutes: "))
    duration_seconds = (duration_hours * 3600) + (duration_minutes * 60)
    reminder = Reminder(task, duration_seconds)

    # Save reminder to a file
    save_reminder(reminder)

def save_reminder(reminder):
    try:
        # Load existing reminders from file
        reminders = load_reminders()

        # Add the new reminder to the list
        reminders.append(reminder)

        # Save the updated list back to the file
        with open("reminders.pickle", "wb") as file:
            pickle.dump(reminders, file)
    except FileNotFoundError:
        # If the reminders file doesn't exist, create a new one
        with open("reminders.pickle", "wb") as file:
            pickle.dump([reminder], file)

def load_reminders():
    with open("reminders.pickle", "rb") as file:
        reminders = pickle.load(file)
    return reminders

def display_reminders():
    try:
        reminders = load_reminders()
        if reminders:
            print("Reminders:")
            for i, reminder in enumerate(reminders):
                duration_minutes, duration_seconds = divmod(reminder.duration, 60)
                duration_hours, duration_minutes = divmod(duration_minutes, 60)
                print("{}. Task: {}, Duration: {} hours, {} minutes".format(i+1, reminder.task, duration_hours, duration_minutes))
        else:
            print("No reminders found.")
    except FileNotFoundError:
        print("No reminders found.")

def delete_reminder():
    try:
        reminders = load_reminders()
        if reminders:
            display_reminders()
            index = int(input("Enter the index of the reminder to delete: "))
            if 1 <= index <= len(reminders):
                deleted_reminder = reminders.pop(index - 1)
                print("Deleted reminder: Task: {}, Duration: {} seconds".format(deleted_reminder.task, deleted_reminder.duration))
                with open("reminders.pickle", "wb") as file:
                    pickle.dump(reminders, file)
            else:
                print("Invalid index.")
        else:
            print("No reminders found.")
    except FileNotFoundError:
        print("No reminders found.")

def main():
    while True:
        print("\nReminder Application")
        print("1. Set a reminder")
        print("2. View reminders")
        print("3. Delete a reminder")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            set_reminder()
        elif choice == "2":
            display_reminders()
        elif choice == "3":
            delete_reminder()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

"REWARDS"
class User:
    def __init__(self, name):
        self.name = name
        self.strike_count = 0

    def add_strike(self):
        self.strike_count += 1
        self.check_strike_count()

    def reset_strikes(self):
        self.strike_count = 0

    def check_strike_count(self):
        if self.strike_count == 3:
            self.give_reward()
            self.reset_strikes()

    def give_reward(self):
        rewards = {
            1: "Bronze Badge",
            2: "Silver Badge",
            3: "Gold Badge"
        }
        reward = rewards.get(self.strike_count, "Unknown Reward")
        print(f"Congratulations, {self.name}! You've earned a {reward} for maintaining a strike count of {self.strike_count}.")

# Example usage
user1 = User("John")
user2 = User("Sarah")

user1.add_strike()
user1.add_strike()
user1.add_strike()

user2.add_strike()
user2.add_strike()
"QUOTES"
import requests
import random

def get_motivational_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote = response.json()
        return quote['content']
    else:
        return "Failed to fetch a quote"

def display_daily_quote():
    quote = get_motivational_quote()
    print("Daily Motivational Quote:")
    print(quote)

# Example usage
display_daily_quote()

