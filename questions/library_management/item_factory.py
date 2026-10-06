from item_type import ItemType
from book import Book
from magazine import Magazine

class ItemFactory:
    @staticmethod
    def create_item(item_type,item_id,title,author):
        if item_type == ItemType.BOOK:
            return Book(item_id,title,author)
        elif item_type == ItemType.MAGAZINE:
            return Magazine(item_id,title,author)
        else:
            raise ValueError("Invalid item type")
    