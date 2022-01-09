from typing import Dict, List
from CSPTasks.csp import *


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns


    def satisfied(self, assigment: Dict[int, int]) -> bool:
        for q1c, q1r in assigment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assigment:
                    q2r: int = assigment[q2c]
                    if q2r == q1r:
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):
                        return False
        return True


def main():
    columns: List[int] = [1,2,3,4,5,6,7,8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1,2,3,4,5,6,7,8]
    csp: CSP[int, int] = CSP(columns, rows)

    csp.add_constraint(QueensConstraint(columns))
    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    if solution is None:
        print('No solution')
    else:
        print(solution)