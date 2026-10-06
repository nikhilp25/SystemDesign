from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from book_copy import BookCopy
    from member import Member

class Loan:
    def __init__(self,copy:'BookCopy',member:'Member'):
        self.copy = copy
        self.member = member
        self.loan_date = datetime.today()
    
    def get_copy(self):
        return self.copy
    
    def get_member(self):
        return self.member
    