from loan import Loan
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from book_copy import BookCopy
    from member import Member

class TransactionService:
    _instance: Optional['TransactionService'] = None
    
    def __init__(self):
        if TransactionService._instance is not None:
            raise Exception("This class is a singleton!")
        self.active_loan = {}
    
    @staticmethod
    def get_instance(cls):
        if TransactionService._instance is None:
            TransactionService._instance = TransactionService()
        return TransactionService._instance
    
    def create_loan(self,book_copy:'BookCopy',member:'Member') -> None:
        if book_copy.get_id() in self.active_loan:
            raise ValueError("This copy is already on loan.")
        
        loan = Loan(book_copy, member)
        self.active_loan[book_copy.get_id()] = loan
        member.add_loan(loan)
    
    def end_loan(self,book_copy:'BookCopy') -> None:
        loan = self.active_loans.pop(book_copy.get_id(), None)
        if loan is not None:
            loan.get_member().remove_loan(loan)