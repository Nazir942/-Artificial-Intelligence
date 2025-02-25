import random

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class DFS:
    def __init__(self):
        self.directions = [
            (1, 0, "Down"),
            (-1, 0, "Up"),
            (0, 1, "Right"),
            (0, -1, "Left")
        ]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.path = []
        self.topological_order = []

    def init(self):
        self.N = random.randint(4, 7)
        graph = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.N)]
        
        while True:
            source_x, source_y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            goal_x, goal_y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if graph[source_x][source_y] == 1 and graph[goal_x][goal_y] == 1 and (source_x, source_y) != (goal_x, goal_y):
                break
        
        self.source = Node(source_x, source_y)
        self.goal = Node(goal_x, goal_y)
        
        print("\nGenerated Grid:")
        for row in graph:
            print(" ".join(map(str, row)))
        
        print(f"\nSource: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})")
        
        self.st_dfs(graph, self.source)
        
        if self.found:
            print("\nGoal found!")
            print("Path taken:")
            for move, coord in self.path:
                print(f"{move} -> ({coord[0]}, {coord[1]})")
            
            print("\nTopological Order of Node Traversal:")
            for node in self.topological_order:
                print(f"({node[0]}, {node[1]})", end=" -> ")
            print("END")
        else:
            print("\nGoal cannot be reached from the starting block.")

    def st_dfs(self, graph, current_node):
        stack = [(current_node, [])]
        
        while stack:
            u, path_so_far = stack.pop()
            
            self.topological_order.append((u.x, u.y))
            
            if u.x == self.goal.x and u.y == self.goal.y:
                self.found = True
                self.path = path_so_far + [("Goal", (u.x, u.y))]
                return
            
            if graph[u.x][u.y] == 0:
                continue
            graph[u.x][u.y] = 0
            
            for dx, dy, direction in self.directions:
                v_x, v_y = u.x + dx, u.y + dy
                
                if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                    stack.append((Node(v_x, v_y), path_so_far + [(direction, (v_x, v_y))]))

if __name__ == "__main__":
    dfs = DFS()
    dfs.init()