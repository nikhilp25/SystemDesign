from item_states import AvailableState
class BookCopy:
    def __init__(self,copy_id,item):
        self.id = copy_id
        self.item = item
        self.current_state = AvailableState()
        item.add_copy(self)

    def checkout(self,member):
        self.current_state.checkout(self,member)
    
    def return_item(self):
        self.current_state.return_item(self)
    
    def place_hold(self,member):
        self.current_state.place_hold(self,member)
    
    def get_id(self):
        return self.id
    
    def get_item(self):
        return self.item
    
    def get_state(self):
        return self.current_state
    
    def set_state(self,state):
        self.current_state = state
    
    def get_member(self):
        return self.member
    
    def is_available(self):
        return isinstance(self.current_state,AvailableState)