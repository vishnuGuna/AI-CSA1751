from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def is_valid(self):
        if 0 <= self.missionaries <= 3 and 0 <= self.cannibals <= 3:
            if self.missionaries == 0 or self.missionaries >= self.cannibals:
                if self.missionaries == 3 or 3 - self.missionaries >= 3 - self.cannibals:
                    return True
        return False

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_successors(self):
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        successors = []
        for m, c in moves:
            if self.boat == 1:
                new_state = State(self.missionaries - m, self.cannibals - c, 0, self)
            else:
                new_state = State(self.missionaries + m, self.cannibals + c, 1, self)
            if new_state.is_valid():
                successors.append(new_state)
        return successors

def bfs():
    initial_state = State(3, 3, 1)
    queue = deque([initial_state])
    visited = set()
    while queue:
        current_state = queue.popleft()
        if current_state.is_goal():
            return current_state
        visited.add((current_state.missionaries, current_state.cannibals, current_state.boat))
        for state in current_state.get_successors():
            if (state.missionaries, state.cannibals, state.boat) not in visited:
                queue.append(state)

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    for step in reversed(path):
        print(f"Missionaries: {step.missionaries}, Cannibals: {step.cannibals}, Boat: {step.boat}")

solution = bfs()
if solution:
    print_solution(solution)
