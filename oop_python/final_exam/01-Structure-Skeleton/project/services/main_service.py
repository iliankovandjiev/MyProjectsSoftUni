from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = [r.name for r in self.robots]

        if not result:
            return f"{self.name} Main Service:\n" \
               f"Robots: none"

        return f"{self.name} Main Service:\n" \
               f"Robots: {' '.join(result)}"
