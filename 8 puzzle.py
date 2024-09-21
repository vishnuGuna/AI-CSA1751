from collections import deque

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Puzzle:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_children(self):
        children = []
        x, y = self.find_zero()
        directions = {'up': (x-1, y), 'down': (x+1, y), 'left': (x, y-1), 'right': (x, y+1)}
        for direction, (new_x, new_y) in directions.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                children.append(Puzzle(new_state, self, direction, self.depth + 1))
        return children

    def is_goal(self):
        return self.state == goal_state

def bfs(start_state):
    start_puzzle = Puzzle(start_state)
    queue = deque([start_puzzle])
    visited = set()
    while queue:
        current_puzzle = queue.popleft()
        if current_puzzle.is_goal():
            return current_puzzle
        visited.add(str(current_puzzle.state))
        for child in current_puzzle.generate_children():
            if str(child.state) not in visited:
                queue.append(child)
    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    for step in reversed(path):
        for row in step.state:
            print(row)
        print()

start_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
solution = bfs(start_state)

if solution:
    print_solution(solution)
else:
    print("No solution found.")
