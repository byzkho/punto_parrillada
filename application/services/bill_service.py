from typing import List

from domain.entities.bill import Bill
from domain.repositories.bill_repository import BillRepository


class BillService:
    def __init__(self, bill_repository: BillRepository):
        self.bill_repository = bill_repository

    def create_bill(self, bill: Bill):
        bill_data = bill.model_dump(exclude={"shares"})
        billing_created = self.bill_repository.create(bill_data)
        for share_bill in bill.shares:
            share_bill_dict = share_bill.model_dump()
            share_bill_dict["bill_id"] = billing_created.id
            self.bill_repository.create_share(share_bill_dict)
        return billing_created

    def get_bill(self, bill_id: int) -> Bill:
        return self.bill_repository.get_one(bill_id)

    def get_all_bills(self) -> List[Bill]:
        return self.bill_repository.get_all()
    
    def get_bill_by_order(self, order_id: int) -> Bill:
        return self.bill_repository.get_by_order(order_id)
    
    def get_bill_by_user(self, user_id: int) -> List[Bill]:
        return self.bill_repository.get_bill_by_user(user_id)