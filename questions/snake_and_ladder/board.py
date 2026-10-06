class Board:
    def __init__(self,size,entities):
        self.size = size
        self.snakes_and_ladder = {}

        for entity in entities:
            self.snakes_and_ladder[entity.get_start()] = entity.get_end()
    
    def get_size(self):
        return self.size
    
    def get_final_position(self,position):
        return self.snakes_and_ladder.get(position,position)