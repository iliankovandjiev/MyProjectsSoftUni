from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.5
    #
    # def __init__(self, booth_number: int,  capacity: int):
    #     super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        price_for_reservation = self.PRICE_PER_PERSON * number_of_people
        self.price_for_reservation = price_for_reservation
        self.is_reserved = True
