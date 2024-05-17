from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.Transaction import Transaction


class ITransactionRepository(ABC):
    @abstractmethod
    def get_all_transactions(self, transaction_id: int) -> List[Transaction]:
        '''
        Returns all the itens in the database 
        '''
        pass
    
    @abstractmethod
    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        '''
        Returns the item with the given id.
        If the item does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def create_transaction(self, transaction_id: int, transaction: Transaction) -> Transaction:
        '''
        Creates a new item in the database
        '''
        pass
    
    @abstractmethod
    def delete_transaction(self, transaction_id: int) -> Transaction:
        '''
        Deletes the item with the given id.
        If the item does not exist, returns None
        '''
        
    @abstractmethod
    def update_transaction(self, transaction_id: int,
                           transaction_type: TransactionTypeEnum = None,
                           value: float = None,
                           current_balance: float = None,
                           timestamp: float = None) -> Transaction:
        '''
        Updates the item with the given id.
        If the item does not exist, returns None
        '''
        pass
    
    