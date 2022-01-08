from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    
    def push(self, item: T) -> None:
        self._container.append(item)

    
    def pop(self) -> T:
        return self._container.pop()

    
    @property
    def empty(self) -> bool:
        return not self._container

    
    def __repr__(self):
        return repr(self._container)
