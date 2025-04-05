
def limited_depth_search(grid, pos, goal, current_depth, max_depth, explored, route):
    r, c = pos
    route.append(pos)
    explored.add(pos)

    if pos == goal:
        return True, route
    
    if current_depth == max_depth:
        route.pop()
        return False, None
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    total_rows, total_cols = len(grid), len(grid[0])
    
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        next_pos = (new_r, new_c)
        if 0 <= new_r < total_rows and 0 <= new_c < total_cols and grid[new_r][new_c] == 0 and next_pos not in explored:
            found, found_route = limited_depth_search(grid, next_pos, goal, current_depth + 1, max_depth, explored, route)
            if found:
                return True, found_route
    
    route.pop()
    return False, None


def iddfs_search(grid, start, goal, max_limit):
    for depth_limit in range(max_limit + 1):
        explored = set()
        route = []
        found, result_route = limited_depth_search(grid, start, goal, 0, depth_limit, explored, route)
        if found:
            return True, len(result_route) - 1, result_route  
    return False, max_limit, None

if __name__ == "__main__":
    try:
        rows, cols = map(int, input("Enter grid rows and columns: ").split())
        grid = []
        print("Input the grid rows (0 for open cell, 1 for wall):")
        for _ in range(rows):
            row_data = list(map(int, input().strip().split()))
            grid.append(row_data)
        
        start_data = input("Enter start position (row col): ").split()
        goal_data = input("Enter goal position (row col): ").split()
        start = (int(start_data[0]), int(start_data[1]))
        goal = (int(goal_data[0]), int(goal_data[1]))
        
        max_limit = rows * cols
        found, depth_found, route = iddfs_search(grid, start, goal, max_limit)
        
        if found:
            print(f"Path discovered at depth {depth_found} using IDDFS")
            print("Route:", route)
        else:
            print(f"No path found within maximum depth limit of {max_limit} using IDDFS")
    except ValueError:
        print("Invalid input format.")