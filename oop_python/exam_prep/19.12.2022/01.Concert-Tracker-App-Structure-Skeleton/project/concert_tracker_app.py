from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN:
            raise ValueError("Invalid musician type!")

        valid_name = [n for n in self.musicians if n.name == name]

        if valid_name:
            raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIAN[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = [b.name for b in self.bands]

        if name in band:
            raise Exception(f"{name} band is already created!")

        b = Band(name)
        self.bands.append(b)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c.place for c in self.concerts]
        if place in concert:
            raise Exception(f"{place} is already registered for {concert[0].genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        musician = [m for m in self.musicians if m.name == musician_name]

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next(filter(lambda b: b.name == band_name, self.bands))

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician[0])
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        band = next(filter(lambda b: b.name == band_name, self.bands))

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next(filter(lambda m: m.name == musician_name, band.members))

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]

        singers = [s for s in band.members if isinstance(s, Singer)]
        drummers = [d for d in band.members if isinstance(d, Drummer)]
        guitarists = [g for g in band.members if isinstance(g, Guitarist)]

        if not (singers and drummers and guitarists):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        drummers_are_qualified = True
        for drummer in drummers:
            if concert.genre == "Rock":
                if "play the drums with drumsticks" not in drummer.skills:
                    drummers_are_qualified = False

            elif concert.genre == "Metal":
                if "play the drums with drumsticks" not in drummer.skills:
                    drummers_are_qualified = False

            elif concert.genre == "Jazz":
                if "play the drums with drum brushes" not in drummer.skills:
                    drummers_are_qualified = False

        guitarists_are_qualified = True
        for guitarist in guitarists:
            if concert.genre == "Rock":
                if "play rock" not in guitarist.skills:
                    guitarists_are_qualified = False

            elif concert.genre == "Metal":
                if "play metal" not in guitarist.skills:
                    guitarists_are_qualified = False

            elif concert.genre == "Jazz":
                if "play jazz" not in guitarist.skills:
                    guitarists_are_qualified = False

        singers_are_qualified = True
        for singer in singers:
            if concert.genre == "Rock":
                if "sing high pitch notes" not in singer.skills:
                    singers_are_qualified = False

            elif concert.genre == "Metal":
                if "sing low pitch notes" not in singer.skills:
                    singers_are_qualified = False

            elif concert.genre == "Jazz":
                if "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills:
                    singers_are_qualified = False

        if not singers_are_qualified or not drummers_are_qualified or not guitarists_are_qualified:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."