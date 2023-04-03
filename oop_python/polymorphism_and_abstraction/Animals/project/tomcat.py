from project.cat import Cat


class Tomcat(Cat):
    GENDER = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.GENDER)

    @staticmethod
    def make_sound():
        return "Hiss"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
