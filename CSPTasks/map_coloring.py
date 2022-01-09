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