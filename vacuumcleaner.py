class VacuumEnvironment:
    def __init__(self):
        self.rooms = {'A': 'dirty', 'B': 'dirty'}
        self.vacuum_location = 'A'

    def is_dirty(self, location):
        return self.rooms[location] == 'dirty'

    def clean(self, location):
        self.rooms[location] = 'clean'

    def move(self, new_location):
        self.vacuum_location = new_location

    def all_clean(self):
        return self.rooms['A'] == 'clean' and self.rooms['B'] == 'clean'


class VacuumAgent:
    def __init__(self, environment):
        self.environment = environment

    def perceive_and_act(self):
        location = self.environment.vacuum_location
        if self.environment.is_dirty(location):
            self.environment.clean(location)
            print(f"Cleaning room {location}")
        else:
            if location == 'A':
                self.environment.move('B')
                print("Moving to room B")
            elif location == 'B':
                self.environment.move('A')
                print("Moving to room A")


environment = VacuumEnvironment()
agent = VacuumAgent(environment)

while not environment.all_clean():
    agent.perceive_and_act()

print("All rooms are clean!")
