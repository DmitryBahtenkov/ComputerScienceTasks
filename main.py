from SearchTasks.maze import *

if __name__ == '__main__':
    maze: Maze = Maze()
    print(maze)
    print('____________')

    distance: Callable[[MazeLocation], float] = manhattan_distance(maze.goal)
    solution: Optional[Node[MazeLocation]] = astar(maze.start, maze.goal_test, maze.successors, distance)
    if solution is None:
        print("No solution")
    else:
        path: List[MazeLocation] = node_to_path(solution)
        maze.mark(path)
        print(maze)
