from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }
    VALID_ROBOT = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,
    }
    VALID_MAtCHES = {
        "MaleRobot": "MainService",
        "FemaleRobot": "SecondaryService",
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOT[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        for key, item in self.VALID_MAtCHES.items():
            if not robot.__class__.__name__ == key or not service.__class__.__name__ == item:
                return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        robot = next(filter(lambda r: r.name == robot_name, service.robots))
        if robot not in service.robots:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        robot_fed = 0
        service = next(filter(lambda s: s.name == service_name, self.services))
        for robot in service.robots:
            robot.eating()
            robot_fed += 1
        return f"Robots fed: {robot_fed}."

    def service_price(self, service_name: str):
        total_price = 0
        service = next(filter(lambda s: s.name == service_name, self.services))
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return "\n".join(result)
