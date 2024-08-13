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

