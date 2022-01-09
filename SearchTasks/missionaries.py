from __future__ import annotations
from typing import List, Optional
from SearchTasks.generic_search import *


MAX_NUM: int = 3


class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries # миссионеры с западного берега
        self.wc: int = cannibals # людоеды с западного берега
        self.em: int = MAX_NUM - self.wm # миссионеры с восточного берега
        self.ec: int = MAX_NUM - self.wc # людоеды с восточного берега
        self.boat = boat

    def __str__(self) -> str:
        return f'On the west bank there are {self.wm} missionaries and {self.wc} cannibals. \n' \
            + f'The boat on the {"west" if self.boat else "east"}.'


    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    
    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False 
        if self.em < self.ec and self.em > 0:
            return False 
        return True


    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        if self.boat:
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
            if (self.wm > 0) and (self.wc > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else:
            if self.em > 1:
                sucs.append(MCState(self.em - 2, self.ec, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.em - 1, self.ec, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.em, self.ec - 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.em, self.ec - 1, not self.boat))
            if (self.em > 0) and (self.ec > 0):
                sucs.append(MCState(self.em - 1, self.ec - 1, not self.boat))

        return [x for x in sucs if x.is_legal]


def display_solution(path: List[MCState]):
    if len(path) == 0:
        return
    old_state: MCState = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print(f'{old_state.em - current_state.em} missionaries and {old_state.ec - current_state.ec} cannibals' \
             + ' moved from the east to west bank\n')

        else:
            print(f'{old_state.wm - current_state.wm} missionaries and {old_state.wc - current_state.wc} cannibals' \
             + ' moved from the west to east bank\n')
        print(current_state)
        old_state = current_state