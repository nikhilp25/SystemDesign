from library_item import LibraryItem
class Magazine(LibraryItem):
    def __init__(self,item_id,title,publisher):
        super().__init__(item_id, title)
        self.publisher = publisher
        
    def get_author_or_publisher(self):
        return self.publisher