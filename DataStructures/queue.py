from typing import Deque, TypeVar, Generic, List

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()


    def push(self, item: T) -> None:
        self._container.append(item)

    
    def pop(self) -> T:
        return self._container.popleft()

    
    @property
    def empty(self) -> bool:
        return not self._container

    
    def __repr__(self):
        return repr(self._container)    