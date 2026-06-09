# main.py
# Study Planner - Day 1
# Variables to store all data
# storage.py
# Handles saving and loading all data


from storage import save_data, load_data
from datetime import date, timedelta


def show_menu():
    print("\n===== Study Planner =====")
    print("1. Add a subject")
    print("2. Log a study session")
    print("3. View weekly summary")
    print("4. Check goals")
    print("5. View study streak")
    print("6. Search sessions")
    print("7. Delete a subject")
    print("8. View all subjects")
    print("0. Exit")

def add_subject(subjects):
    name = input("Enter subject name: ").strip()
    if name in subjects:
        print("This subject already exists!")
        return
    try:
        goal = float(input("Enter daily goal in hours: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    subjects[name] = goal
    print(f"Subject '{name}' added with goal {goal} hours per day.")

def log_session(subjects, sessions):
    if len(subjects) == 0:
        print("No subjects found! Add a subject first.")
        return
    name = input("Enter subject name: ").strip()
    if name not in subjects:
        print("Subject not found! Add it first.")
        return
    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        minutes = int(input("Enter minutes studied: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    if minutes <= 0:
        print("Minutes must be greater than zero!")
        return
    session = {
        "subject": name,
        "date": date,
        "minutes": minutes
    }
    sessions.append(session)
    print(f"Logged! You studied {name} for {minutes} minutes on {date}.")

def weekly_summary(sessions):
    if len(sessions) == 0:
        print("No sessions logged yet!")
        return
    totals = {}
    for session in sessions:
        name = session["subject"]
        mins = session["minutes"]
        if name in totals:
            totals[name] += mins
        else:
            totals[name] = mins
    print("\n--- Weekly Summary ---")
    for subject, total_mins in totals.items():
        hours = total_mins / 60
        print(f"{subject}: {total_mins} minutes ({hours:.1f} hours)")


def check_goals(subjects,sessions):
    if len(subjects) == 0:
        print("No subjects found! Add a subject first.")
        return

    studied = set()
    for session in sessions:
        studied.add(session["subject"])

    
    all_subjects = set(subjects.keys())
    not_studied = all_subjects - studied


    print("\n--- Goal Check ---")
    if len(not_studied) == 0:
        print("Great work! You studied all subjects.")
    else:
        print("Subjects you have not studied yet:")
        for subject in not_studied:
            print(f"  x {subject} (goal: {subjects[subject]} hrs/day)")

    print("\nSubjects you studied:")
    for subject in studied:
        print(f"  v {subject}")


def study_streak(sessions):
    if len(sessions) == 0:
        print("No sessions logged yet!")
        return

    dates_studied = set()
    for session in sessions:
        dates_studied.add(session["date"])

    streak = 0
    today = date.today()

    while True:
        day_str = str(today)
        if day_str in dates_studied:
            streak += 1
            today = today - timedelta(days=1)
        else:
            break

    print(f"\nCurrent study streak: {streak} days")
    if streak == 0:
        print("No streak yet — log a session for today to start one!")
    elif streak >= 7:
        print("Amazing! You have studied for a week straight.")
    elif streak >= 3:
        print("Good work! Keep it going.")



def search_sessions(sessions):
    if len(sessions) == 0:
        print("No sessions logged yet!")
        return

    keyword = input("Enter subject name to search: ").strip().lower()

    results = []
    for session in sessions:
        if session["subject"].lower() == keyword:
            results.append(session)

    if len(results) == 0:
        print(f"No sessions found for '{keyword}'.")
    else:
        print(f"\n--- Sessions for '{keyword}' ---")
        total_mins = 0
        for r in results:
            print(f"  Date: {r['date']} | Minutes: {r['minutes']}")
            total_mins += r['minutes']
        print(f"Total: {total_mins} minutes ({total_mins/60:.1f} hours)")


def delete_subject(subjects, sessions):
    if len(subjects) == 0:
        print("No subjects found!")
        return

    print("\nCurrent subjects:")
    for name in subjects:
        print(f"  - {name}")

    name = input("\nEnter subject name to delete: ").strip().lower()

    found = False
    for subject in subjects:
        if subject.lower() == name:
            found = True
            actual_name = subject
            break

    if not found:
        print(f"Subject '{name}' not found!")
        return

    confirm = input(f"Are you sure you want to delete '{actual_name}' and all its sessions? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    del subjects[actual_name]

    sessions[:] = [s for s in sessions if s["subject"] != actual_name]

    print(f"Deleted '{actual_name}' and all its sessions successfully.")



def view_subjects(subjects):
    if len(subjects) == 0:
        print("No subjects added yet!")
        return

    print("\n--- Your Subjects ---")
    for name, goal in subjects.items():
        print(f"  {name}: {goal} hrs/day goal")
    print(f"\nTotal subjects: {len(subjects)}")



def main():
    subjects, sessions = load_data()

    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_subject(subjects)
            save_data(subjects, sessions)
        elif choice == "2":
            log_session(subjects, sessions)
            save_data(subjects, sessions)
        elif choice == "3":
            weekly_summary(sessions)
        elif choice == "4":
            check_goals(subjects, sessions)
        elif choice == "5":
            study_streak(sessions)
        elif choice == "6":
            search_sessions(sessions)
        elif choice == "7":
            delete_subject(subjects, sessions)
            save_data(subjects, sessions)
        elif choice == "8":
            view_subjects(subjects)
        elif choice == "0":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
