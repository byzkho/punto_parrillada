class SeatService:
    def __init__(self, seat_repository):
        self.seat_repository = seat_repository

    def get_seats(self):
        return self.seat_repository.get_seats()

    def get_seat(self, seat_id):
        return self.seat_repository.get_seat(seat_id)

    def add_seat(self, seat):
        return self.seat_repository.add_seat(seat)

    def update_seat(self, seat_id, seat):
        return self.seat_repository.update_seat(seat_id, seat)

    def delete_seat(self, seat_id):
        return self.seat_repository.delete_seat(seat_id)