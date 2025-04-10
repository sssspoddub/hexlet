from datetime import datetime


class Booking:
    def __init__(self):
        self.bookings = []

    def booking(self, start, end):
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()

        if end_date <= start_date:
            return False

        for booked_start, booked_end in self.bookings:
            if start_date < booked_end and end_date > booked_start:
                return False

        self.booking.append(start_date, end_date)
        return True
