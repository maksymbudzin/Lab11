from models.Sports import Sports


class TourManager:

    def __init__(self):
        self.sports_in_tour = []

    def add_sports_to_tour(self, *sports_to_add: Sports):
        for sports in sports_to_add:
            self.sports_in_tour.append(sports)

    def remove_sports_from_tour(self, *sports_to_remove: Sports):
        for sports in sports_to_remove:
            self.sports_in_tour.remove(sports)

    def find_sports_price_lower_than(self, price_to_compare: int):
        """
        >>> water = Sports("Diving", "AccordTour", 300, 180, "hotel")
        >>> climbing = Sports("Climbing", "Join_up", 200, 140, "mountain")
        >>> driving = Sports("Driving", "Tour_Ukraine", 100, 90, "nature")
        >>> tour = TourManager()
        >>> tour.add_sports_to_tour(water, climbing, driving)
        >>> result = tour.find_sports_price_lower_than(150)
        >>> [sports.base_price for sports in result]
        [140, 90]
        """
        result: list = []
        for sports in self.sports_in_tour:
            if sports.base_price < price_to_compare:
                result.append(sports)
        return result

    def find_sports_top_bigger_than(self, top_price_to_compare: int):
        """
        >>> water = Sports("Diving", "AccordTour", 300, 180, "hotel")
        >>> climbing = Sports("Climbing", "Join_up", 200, 140, "mountain")
        >>> driving = Sports("Driving", "Tour_Ukraine", 100, 90, "nature")
        >>> tour = TourManager()
        >>> tour.add_sports_to_tour(water, climbing, driving)
        >>> result = tour.find_sports_top_bigger_than(120)
        >>> [sports.top_price for sports in result]
        [300, 200]
        """
        result: list = []
        for sports in self.sports_in_tour:
            if sports.top_price > top_price_to_compare:
                result.append(sports)
        return result

    def sort_sports_by_top_price(self, reverse=True):
        """
        >>> water = Sports("Diving", "AccordTour", 300, 180, "hotel")
        >>> climbing = Sports("Climbing", "Join_up", 200, 140, "mountain")
        >>> driving = Sports("Driving", "Tour_Ukraine", 100, 90, "nature")
        >>> tour = TourManager()
        >>> tour.add_sports_to_tour(water, climbing, driving)
        >>> tour.sort_sports_by_top_price(reverse=False)
        >>> [sports.top_price for sports in tour.sports_in_tour]
        [100, 200, 300]
        >>> tour.sort_sports_by_top_price(reverse=True)
        >>> [sports.top_price for sports in tour.sports_in_tour]
        [300, 200, 100]
        """
        self.sports_in_tour.sort(key=lambda sports: sports.top_price, reverse=reverse)

    def sort_flowers_by_price(self, reverse=False):
        """
        >>> water = Sports("Diving", "AccordTour", 300, 180, "hotel")
        >>> climbing = Sports("Climbing", "Join_up", 200, 140, "mountain")
        >>> driving = Sports("Driving", "Tour_Ukraine", 100, 90, "nature")
        >>> tour = TourManager()
        >>> tour.add_sports_to_tour(water, climbing, driving)
        >>> tour.sort_flowers_by_price()
        >>> [sports.base_price for sports in tour.sports_in_tour]
        [90, 140, 180]
        >>> tour.sort_flowers_by_price(reverse=True)
        >>> [sports.base_price for sports in tour.sports_in_tour]
        [180, 140, 90]
        """
        self.sports_in_tour.sort(key=lambda sports: sports.base_price, reverse=reverse)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=False, extraglobs={'tour': TourManager()})
