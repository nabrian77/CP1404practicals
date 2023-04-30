CurrentYear = 2023
VintageAge = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year} : ${self.cost:,.2f}"


    def get_age(self):
        return CurrentYear - self.year


    def is_vintage(self):
        return self.get_age() >= VintageAge


    def __it__(selfself, other):
        return self.year < other.year



