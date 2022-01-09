from CSPTasks.csp import *
from typing import Dict, List, Optional


class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1 = place1
        self.place2 = place2

    
    def satisfied(self, assigment: Dict[V, D]) -> bool:
        if self.place1 not in assigment or self.place2 not in assigment:
            return True
        
        return assigment[self.place1] != assigment[self.place2]


def main():
    variables: List[str] = ['Western A', 'Northern T', 'South A', 'Queensland', 'New South Wales', 'Victoria', 'Tasmania']
    domains: Dict[str, List[str]] = {}

    for variable in variables:
        domains[variable] = ['red', 'green', 'blue']
    
    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(MapColoringConstraint(variables[0], variables[1]))
    csp.add_constraint(MapColoringConstraint(variables[0], variables[2]))
    csp.add_constraint(MapColoringConstraint(variables[2], variables[1]))
    csp.add_constraint(MapColoringConstraint(variables[3], variables[1]))
    csp.add_constraint(MapColoringConstraint(variables[3], variables[2]))
    csp.add_constraint(MapColoringConstraint(variables[3], variables[4]))
    csp.add_constraint(MapColoringConstraint(variables[4], variables[2]))
    csp.add_constraint(MapColoringConstraint(variables[5], variables[2]))
    csp.add_constraint(MapColoringConstraint(variables[5], variables[4]))
    csp.add_constraint(MapColoringConstraint(variables[5], variables[6]))

    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print('No sulution')
    else:
        print(solution)