class Child:
    def __init__(self, name, interests, goals, routine):
        self.name = name
        self.interests = interests
        self.goals = goals
        self.routine = routine

    def create_plan(self):
        # Functionality to create a personalized SLP practice plan
        pass

def gather_information():
    name = input("Enter your child's name: ")
    interests = input("Enter your child's interests: ")
    goals = input("Enter the SLP goals for your child: ")
    routine = input("Describe your child's typical routine: ")

    child = Child(name, interests, goals, routine)
    child.create_plan()

gather_information()
