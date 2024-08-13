class StudyTimetable:
    def __init__(self): # Initialize the study timetable with an empty schedule.
               
               self.schedule = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    def add_activity(self, day, time, activity):#
        
        if day in self.schedule:
            self.schedule[day].append((time, activity))  # Add the activity as a tuple of time and activity
            print(f"Added '{activity}' on {day} at {time}.")
        else:
            print("Invalid day. Please enter a valid day of the week.")

    def remove_activity(self, day, time):# Remve activities
        
        if day in self.schedule:
            for activity in self.schedule[day]:
                if activity[0] == time:
                    self.schedule[day].remove(activity)
                    print(f"Removed activity at {time} on {day}.")
                    return
            print(f"No activity found at {time} on {day}.")
        else:
            print("Invalid day. Please enter a valid day of the week.")

    def view_schedule(self):# Allows user to view the schedule
        
        print("\nStudy Timetable:")
        for day, activities in self.schedule.items():
            print(f"{day}:")
            if activities:
                for time, activity in activities:
                    print(f"  {time}: {activity}")
            else:
                print("  No activities scheduled.")

def main():# Main function to run the study timetable application.
   
    timetable = StudyTimetable()  # Create an instance of StudyTimetable


    while True:
        print("\nStudy Timetable")
        print("1. Add Activity")
        print("2. Remove Activity")
        print("3. View Schedule")
        print("4. Exit")


        choice = input("Choose an option: ")


        if choice == '1':
            day = input("Enter the day of the week: ")
            time = input("Enter the time (e.g., '10:00 AM'): ")
            activity = input("Enter the activity: ")
            timetable.add_activity(day, time, activity)  # Add a new activity


        elif choice == '2':
            day = input("Enter the day of the week: ")
            time = input("Enter the time of the activity to remove: ")
            timetable.remove_activity(day, time)  # Remove an activity


        elif choice == '3':
            timetable.view_schedule()  # View the complete schedule


        elif choice == '4':
            print("Exiting the Study Timetable application. Goodbye!")
            break  # Exit the loop


        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()  # Run the main function
