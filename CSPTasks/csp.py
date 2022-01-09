from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') # тип variable для переменной
D = TypeVar('D') # тип domain для области определения


class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    
    @abstractmethod
    def satisfied(self, assigment: Dict[V, D]) -> bool:
        pass



class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError('Every variable should have a domain assigned to it')

    
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError('Variable in constraint not in CSP')
            else:
                self.constraints[variable].append(constraint)

    
    def consistent(self, variable: V, assigment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assigment):
                return False
            return True


    def backtracking_search(self, assigment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        if len(assigment) == len(self.variables):
            return assigment

        unassigned: List[V] = [v for v in self.variables if v not in assigment]

        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assigment = assigment.copy()
            local_assigment[first] = value
            if self.consistent(first, local_assigment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assigment)
                if result is not None:
                    return result
        return None

