from models.AbstractTour import AbstractTour


class Sports(AbstractTour):
    def __init__(self, name: str, operator: str, top_price: int, base_price, type_of_accomodation):
        super().__init__(name, operator, top_price, base_price)
        self.type_of_accomodation = type_of_accomodation

    def __str__(self):
        return "name : " + str(self.name) + "\n" \
            "Operator is : " + str(self.operator) + "\n" \
            "Top price is : " + str(self.top_price) + "\n" \
            "base price is: " + str(self.base_price) + "\n" \
            "Type of accomodation is: " + str(self.type_of_accomodation) + "\n"