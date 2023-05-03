from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = [r.name for r in self.robots]

        if not result:
            return f"{self.name} Secondary Service:\n" \
               f"Robots: none"

        return f"{self.name} Secondary Service:\n" \
               f"Robots: {' '.join(result)}"
