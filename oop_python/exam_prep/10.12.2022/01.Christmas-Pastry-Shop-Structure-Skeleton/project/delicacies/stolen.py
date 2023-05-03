from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):

    @property
    def gram_of_portion(self):
        return 250

    def __init__(self, name: str, price: float):
        super().__init__(name, self.gram_of_portion, price)

    def details(self):
        return f"Stolen {self.name}: {self.gram_of_portion}g - {self.price:.2f}lv."
