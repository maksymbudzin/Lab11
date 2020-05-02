from models.AbstractTour import AbstractTour


class Family(AbstractTour):
    def __init__(self, name: str, operator: str, top_price: int, base_price, numbers_of_family):
        super().__init__(name, operator, top_price, base_price)
        self.numbers_of_family = numbers_of_family

    def __str__(self):
        return "name : " + str(self.name) + "\n" \
            "Operator is : " + str(self.operator) + "\n" \
            "Top price is : " + str(self.top_price) + "\n" \
            "Base price is: " + str(self.base_price) + "\n" \
            "The number of family member is: " + str(self.numbers_of_family) + "\n"