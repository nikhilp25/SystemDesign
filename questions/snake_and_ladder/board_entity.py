from abc import ABC,abstractmethod
class BoardEntity(ABC):
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end    
    
class Snake(BoardEntity):
    def __init__(self,start,end):
        super().__init__(start,end)
        if start <= end:
            raise ValueError("Snake head must be at a higher position than its tail.")
    

class Ladder(BoardEntity):
    def __init__(self,start,end):
        super().__init__(start,end)
        if start >= end:
            raise ValueError("Ladder bottom must be at a lower position than its top.")