from project.band_members.musician import Musician


class Guitarist(Musician):

    @property
    def skill(self):
        return ["play metal", "play rock", "play jazz"]
