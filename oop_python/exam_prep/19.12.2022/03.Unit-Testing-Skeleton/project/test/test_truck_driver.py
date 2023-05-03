from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Test", 1)

    def test_init(self):
        assert self.driver.name == "Test"
        assert self.driver.money_per_mile == 1
        assert isinstance(self.driver.available_cargos, dict)
        assert self.driver.earned_money == 0
        assert self.driver.miles == 0

    def test_earned_money_can_not_be_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -3

        self.assertEqual("Test went bankrupt.", str(ex.exception))

    def test_earned_money(self):
        assert self.driver.earned_money == 0

        self.driver.earned_money = 1

        assert self.driver.earned_money == 1

    def test_add_cargo_offer_existing_cargo_location_raise_exception(self):
        self.driver.add_cargo_offer("place", 12)

        with self.assertRaises(Exception) as ex:

            self.driver.add_cargo_offer("place", 13)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_offer(self):
        result = self.driver.add_cargo_offer("place", 12)
        self.assertEqual("Cargo for 12 to place was added as an offer.", result)

    def test_drive_best_cargo_offer_no_offer_available_raise_exception(self):
        assert not self.driver.available_cargos

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_correct(self):
        self.driver.add_cargo_offer("place", 100)
        self.driver.add_cargo_offer("place1", 200)
        self.driver.add_cargo_offer("place2", 50)

        assert self.driver.earned_money == 0
        assert self.driver.miles == 0

        res = self.driver.drive_best_cargo_offer()
        assert res == "Test is driving 200 to place1."

        assert self.driver.earned_money == 200
        assert self.driver.miles == 200

    def test_drive_best_offer_with_activities(self):
        self.driver.earned_money = 11760

        needed_for_cargo = 11750
        money_to_earn = self.driver.money_per_mile * 10000

        self.driver.add_cargo_offer("place1", 10000)
        self.driver.drive_best_cargo_offer()

        expected_money_left = 11760 + money_to_earn - needed_for_cargo
        assert self.driver.earned_money == expected_money_left

    def test_check_for_activities(self):
        self.driver.earned_money = 11760

        result = self.driver.check_for_activities(10000)
        assert result is None

        assert self.driver.earned_money == 10

    def test_eat(self):
        self.driver.earned_money = 50

        self.driver.eat(250)

        assert self.driver.earned_money == 30

    def test_sleep(self):

        self.driver.earned_money = 50

        self.driver.sleep(1000)

        assert self.driver.earned_money == 5

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        assert self.driver.earned_money == 500

    def test_repair_truck(self):
        self.driver.earned_money = 7500
        self.driver.repair_truck(10000)
        assert self.driver.earned_money == 0

    def test__repl(self):
        result = self.driver.__repr__()
        assert result == f"Test has 0 miles behind his back."




