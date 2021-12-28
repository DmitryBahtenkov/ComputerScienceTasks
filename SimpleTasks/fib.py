from typing import Dict, Generator
from functools import lru_cache


# Бесконечная рекурсия
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


# Рекурсия с базовым случаем
def fib2(n: int) -> int:
    # базовый случай
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


memo: Dict[int, int] = {0: 0, 1: 1}  # базовые случаи


# Реализация с мемоизацией
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


# реализация с автоматической мемоизацией
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


# Итеративная реализация
def fib5(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next

    return next


# Реализация с использованием генератора
def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next
