from fastapi import APIRouter, Depends, Request
from app.schemas.order_schema import OrderSchema
from application.dto.order_dto import OrderDto
from application.services.order_service import OrderService
from application.services.reservation_service import ReservationService
from infrastructure.providers.provider_module import get_order_service, get_reservation_service

router = APIRouter()

@router.post("/orders/")
def create_order(order: OrderDto, order_service: OrderService = Depends(get_order_service), reservation_service: ReservationService = Depends(get_reservation_service)):
    order.reservation_id = reservation_service.get_confirmed_reservations_by_user(order.waiter_id).id
    order_created = order_service.create_order(order)
    return order_created

@router.get("/orders/{order_id}")
def get_order(order_id: int, order_service: OrderService = Depends(get_order_service)):
    return order_service.get_order(order_id)

@router.get("/orders/")
def get_orders(order_service: OrderService = Depends(get_order_service)):
    return order_service.get_all_orders()

@router.post("/orders/{order_id}/preparing")
def update_is_preparing(order_id: int, order_service: OrderService = Depends(get_order_service)):
    return order_service.update_is_preparing(order_id)

@router.post("/orders/{order_id}/prepared")
def update_is_prepared(order_id: int, order_service: OrderService = Depends(get_order_service)):
    return order_service.update_is_prepared(order_id)

@router.post("/orders/{order_id}/served")
def update_is_served(order_id: int, order_service: OrderService = Depends(get_order_service)):
    return order_service.update_is_served(order_id)

@router.get("/orders/status/not-prepared")
def get_not_prepared_orders(order_service: OrderService = Depends(get_order_service)):
    return order_service.get_not_prepare_orders()

@router.get("/orders/status/not-preparing")
def get_not_preparing_orders(order_service: OrderService = Depends(get_order_service)):
    return order_service.get_not_preparing_orders()

@router.get("/orders/auth/user", response_model=list[OrderSchema])
def get_orders_by_user(request: Request, order_service: OrderService = Depends(get_order_service)):
    return order_service.get_orders_by_user(request.state.user.id)