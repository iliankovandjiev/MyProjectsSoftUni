from project.meals.meal import Meal


class Dessert(Meal):

    def __init__(self, quantity=30):
        super().__init__(self.name, self.price, quantity)

    def details(self):
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"
