import math

class Pizza:
    def __init__ (self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    @classmethod
    def margherita(cls):
        return cls([5], ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls( [10], ['mozzarella', 'tomatoes', 'ham'])

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
