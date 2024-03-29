from calendar import month_name


class DVD:

    def __init__(self, name: str, id_dvds: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_dvds
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, id_dvds: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(x) for x in date.split(".")]

        return cls(name, id_dvds, year, month_name[month], age_restriction)

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
