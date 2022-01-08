from typing import TypeVar, Generic, List
from heapq import heappop, heappush


T = TypeVar('T')

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    
    def push(self, item: T) -> None:
        heappush(self._container, item)

    
    def pop(self) -> T:
        heappop(self._container)

    
    @property
    def empty(self) -> bool:
        return not self._container

    
    def __repr__(self):
        return repr(self._container)
