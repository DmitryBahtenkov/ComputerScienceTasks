from SearchTasks.maze import *

if __name__ == '__main__':
    maze: Maze = Maze()
    print(maze)
    print('____________')
    solution: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    if solution is None:
        print("No solution")
    else:
        path: List[MazeLocation] = node_to_path(solution)
        maze.mark(path)
        print(maze)
