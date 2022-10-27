class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []
        self.product_list = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        for product in self.products:
            if first_letter == product[0]:
                self.product_list.append(product)
        return self.product_list

    def __repr__(self):
        element = '\n'.join(item for item in (sorted(self.products)))
        return f"Items in the {self.name} catalogue:\n{element}"


