from typing import List, Dict
from domain.entities.bill import Bill
from domain.repositories.bill_repository import BillRepository
from domain.repositories.order_repository import OrderRepository

class BillService:
    def __init__(self, bill_repository: BillRepository, order_repository: OrderRepository):
        self.bill_repository = bill_repository
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
        
        return billing_created

    def get_bill(self, bill_id: int) -> Bill:
        return self.bill_repository.get_one(bill_id)

    def get_all_bills(self) -> List[Bill]:
        return self.bill_repository.get_all()
    
    def get_bill_by_order(self, order_id: int):
        bill = self.bill_repository.get_by_order(order_id)
        if not bill:
            return None

        order = self.order_repository.get_one(order_id)
        
        total_amount, seat_totals = self._calculate_totals(order.order_items)
        
        if bill.is_split:
            return self._generate_split_billing(seat_totals)
        else:
            return self._generate_simple_billing(total_amount, seat_totals)
    
    def get_bill_by_user(self, user_id: int) -> List[Bill]:
        return self.bill_repository.get_bill_by_user(user_id)
    
    def _calculate_totals(self, order_items):
        total_amount = 0
        seat_totals = {}
        for item in order_items:
            item_total = item.product.price * item.quantity
            total_amount += item_total
            if item.seat_id not in seat_totals:
                seat_totals[item.seat_id] = {
                    "total_amount": 0,
                    "seat_number": item.seat.number,
                    "products": {}
                }
            seat_totals[item.seat_id]["total_amount"] += item_total
            if item.product.name not in seat_totals[item.seat_id]["products"]:
                seat_totals[item.seat_id]["products"][item.product.name] = {
                    "quantity": 0,
                    "total": 0
                }
            seat_totals[item.seat_id]["products"][item.product.name]["quantity"] += item.quantity
            seat_totals[item.seat_id]["products"][item.product.name]["total"] += item_total
        return total_amount, seat_totals
    
    def _generate_split_billing(self, seat_totals):
        return [
            {
                "seat_id": seat_id,
                "seat_number": total["seat_number"],
                "total_amount": total["total_amount"],
                "products": [
                    {
                        "name": product_name,
                        "quantity": product_info["quantity"],
                        "total": product_info["total"]
                    }
                    for product_name, product_info in total["products"].items()
                ]
            }
            for seat_id, total in seat_totals.items()
        ]

    def _generate_simple_billing(self, total_amount, seat_totals):
        return {
            "total_amount": total_amount,
            "seat_totals": [
                {
                    "seat_id": seat_id,
                    "seat_number": total["seat_number"],
                    "total_amount": total["total_amount"],
                    "products": [
                        {
                            "name": product_name,
                            "quantity": product_info["quantity"],
                            "total": product_info["total"]
                        }
                        for product_name, product_info in total["products"].items()
                    ]
                }
                for seat_id, total in seat_totals.items()
            ]
        }