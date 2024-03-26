class Activity:
    def __init__(self, name, calories_per_hour):
        self.name = name
        self.calories_per_hour = calories_per_hour

class User:
    def __init__(self, name):
        self.name = name
        self.activities = {}

    def add_activity(self, activity):
        self.activities[activity.name] = activity

    def record_activity(self, activity_name, duration_minutes):
        if activity_name in self.activities:
            activity = self.activities[activity_name]
            calories_burned = (duration_minutes / 60) * activity.calories_per_hour
            print(f"{self.name} recorded {duration_minutes} minutes of {activity_name}. Calories burned: {calories_burned:.2f}")
        else:
            print(f"Activity {activity_name} is not available.")

class FitnessTracker:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.name] = user

    def display_user_activities(self, user_name):
        if user_name in self.users:
            user = self.users[user_name]
            print(f"{user.name}'s activities:")
            for activity_name, activity in user.activities.items():
                print(f"{activity_name}: {activity.calories_per_hour} calories/hour")
        else:
            print(f"User {user_name} not found.")

walking = Activity("Walking", 300)
running = Activity("Running", 600)
swimming = Activity("Swimming", 500)

user1 = User("Claudia")
user1.add_activity(walking)
user1.add_activity(running)

user2 = User("Sofia")
user2.add_activity(walking)
user2.add_activity(swimming)

# Create fitness tracker
tracker = FitnessTracker()
tracker.add_user(user1)
tracker.add_user(user2)

# Record activities
user1.record_activity("Walking", 30)
user1.record_activity("Running", 45)
user1.record_activity("Cycling", 60)

user2.record_activity("Walking", 20)
user2.record_activity("Swimming", 30)

# Display 
tracker.display_user_activities("Claudia")
tracker.display_user_activities("Sofia")
