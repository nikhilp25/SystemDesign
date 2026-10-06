from typing import List
from loan import Loan
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from loan import Loan
    from library_item import LibraryItem

class Member:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.loans = []

    def addLoan(self,loan):
        self.loans.append(loan)
    
    def removeLoan(self,loan):
        self.loans.remove(loan)

    def update(self,libraryItem):
        """Observer update method"""
        print(f"NOTIFICATION for {self.name}: The book '{libraryItem.get_title()}' you placed a hold on is now available!")
    
    def add_loan(self, loan: 'Loan') -> None:
        self.loans.append(loan)

    def remove_loan(self, loan: 'Loan') -> None:
        if loan in self.loans:
            self.loans.remove(loan)

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_loans(self) -> List['Loan']:
        return self.loans