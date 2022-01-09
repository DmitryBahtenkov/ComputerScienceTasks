from SearchTasks.missionaries import *

if __name__ == '__main__':
    
    start: MCState = MCState(MAX_NUM, MAX_NUM, True)
    print(start)
    print('____________')
    
    solution: Optional[Node[MCState]] = bfs(start, MCState.goal_test, MCState.successors)

    if solution is None:
        print("No solution")
    else:
        path: List[MCState] = node_to_path(solution)
        display_solution(path)
