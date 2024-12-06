from typing import List

from domain.entities.bill import Bill
from domain.repositories.bill_repository import BillRepository
from domain.repositories.order_repository import OrderRepository
from domain.repositories.reservation_repository import ReservationRepository


class BillService:
    def __init__(self, bill_repository: BillRepository, reservation_repository: ReservationRepository, order_repository: OrderRepository):
        self.bill_repository = bill_repository
        self.reservation_repository = reservation_repository
        self.order_repository = order_repository

    def create_bill(self, bill: Bill):
        bill_data = bill.model_dump()
        order_id = bill_data['order_id']
        order = self.order_repository.get_one(order_id)
        
        total_amount = 0
        seat_totals = {}
        for item in order.order_items:
            item_total = item.product.price * item.quantity
            total_amount += item_total
            if item.seat_id not in seat_totals:
                seat_totals[item.seat_id] = 0
            seat_totals[item.seat_id] += item_total
        
        bill_data['total'] = total_amount
        billing_created = self.bill_repository.create(bill_data)
        
        simple_billing = {
            "total_amount": total_amount,
            "seat_totals": seat_totals
        }
        
        split_billing = [
            {"seat_id": seat_id, "total_amount": total} for seat_id, total in seat_totals.items()
        ]
        
        return {
            "simple_billing": simple_billing,
            "split_billing": split_billing
        }

    def get_bill(self, bill_id: int) -> Bill:
        return self.bill_repository.get_one(bill_id)

    def get_all_bills(self) -> List[Bill]:
        return self.bill_repository.get_all()
    
    def get_bill_by_order(self, order_id: int) -> Bill:
        return self.bill_repository.get_by_order(order_id)
    
    def get_bill_by_user(self, user_id: int) -> List[Bill]:
        return self.bill_repository.get_bill_by_user(user_id)