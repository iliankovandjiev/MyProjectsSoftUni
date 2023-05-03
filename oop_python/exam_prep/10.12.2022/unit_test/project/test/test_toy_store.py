from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_correct__init(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_shelf_non_existing_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "Bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_is_already_on_shelf_raise_exception(self):
        self.store.add_toy("A", "Bear")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Bear")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_to_a_full_shelf_raise_exception(self):
        self.store.add_toy("A", "Bear")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Doll")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully_return_string(self):
        result = self.store.add_toy("A", "Bear")

        self.assertEqual("Toy:Bear placed successfully!", result)
        self.assertEqual("Bear", self.store.toy_shelf["A"])

    def test_remove_toy_from_non_existing_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "Bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_non_existing_toy_from_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Bear")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_correct(self):
        self.store.toy_shelf["A"] = "Bear"
        result = self.store.remove_toy("A", "Bear")

        self.assertIsNone(self.store.toy_shelf["A"])
        self.assertEqual("Remove toy:Bear successfully!", result)


if __name__ == "__main__":
    main()
