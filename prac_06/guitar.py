class Guitar:
    def __init__(self, name, year, cost):
        if name == None:
            self.name = ""
        else:
            self.name = name
        if year == None:
            self.year =
        else:
            self.year = year
        if cost == None:
            self.cost = 0
        else:
            self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2020 - self.year

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        return False
