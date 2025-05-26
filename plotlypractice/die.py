from random import randint

class Die:
    """A class to role dice."""

    def __init__(self, num_siddes=6):
        """Initialize rolling parameters for a six sided die."""
        self.num_sides = num_siddes

    def roll(self):
        """Rolling method."""
        return randint(1, self.num_sides)

six_sided_die = Die()

six_sided_die.roll()