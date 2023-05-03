from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Ilian", 33, 150.5)

    def test__init(self):
        assert self.tennis_player.name == "Ilian"
        assert self.tennis_player.age == 33
        assert self.tennis_player.points == 150.5
        assert isinstance(self.tennis_player.wins, list)

    def test_invalid_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_player.name = "il"

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_correct_name(self):
        assert self.tennis_player.name == "Ilian"

    def test_invalid_age_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_player.age = 10

        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_valid_age(self):
        assert self.tennis_player.age == 33

    def test_add_new_wins(self):
        self.tennis_player.add_new_win("Sofia")
        self.assertEqual(self.tennis_player.wins[0], "Sofia")

    def test_add_new_wins_tournament_added(self):
        self.tennis_player.add_new_win("Sofia")
        result = self.tennis_player.add_new_win("Sofia")

        assert result == f"Sofia has been already added to the list of wins!"

    def test__str(self):
        self.tennis_player.add_new_win("Sofia")
        self.tennis_player.add_new_win("Madrid")
        self.tennis_player.add_new_win("Solun")
        result = self.tennis_player.__str__()
        assert result == f"Tennis Player: Ilian\n" \
               f"Age: 33\n" \
               f"Points: 150.5\n" \
               f"Tournaments won: Sofia, Madrid, Solun"

    def test__lt_first_player_is_better(self):
        tennis_player2 = TennisPlayer("Ivan", 35, 130)
        result = self.tennis_player.__lt__(tennis_player2)

        assert result == f'Ilian is a better player than Ivan'

    def test__lt_second_player_is_better(self):
        tennis_player2 = TennisPlayer("Ivan", 35, 160)
        result = self.tennis_player.__lt__(tennis_player2)

        assert result == f'Ivan is a top seeded player and he/she is better than Ilian'


if __name__ == '__main__':
    main()

