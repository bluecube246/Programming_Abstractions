from Warrior import *
from random import randint


class KnightErrant(Warrior):
    """
    This class is the KnightErrant class that extends the warrior class.
    An additional functionality iis that the KnightErrant can travel and gain wealth after the travel by chance.
    """
    def __init__(self, name: str, age: int, wealth: int, skills: dict):
        """
        This is the constructor for the KnightErrant Class

        :param name: The string value of the name of the KnightErrant
        :param age:  The int value of the Age of the KnightErrant
        :param wealth: The wealth of the KnightErrant
        :param skills: The dictionary of skills
        """
        Warrior.__init__(self, name, age, wealth, skills)
        self.traveling = False
        self.treasure = 0

    def travel(self):
        """
        This function sets the traveling boolean to True
        It represents that the KnightErrant is currently Traveling
        """
        self.traveling = True
        print("KnightErrant is currently traveling")

    def return_from_travel(self):
        """
        This function sets the traveling boolean to False
        It represents that the KnightErrant has finished Traveling
        """
        self.traveling = False
        print("KnightErrant has returned from travels.")
        self.treasure = randint(0, 9)
        self.wealth += self.treasure
        print("The KnightErrant earned " + str(self.treasure) + " form his travels")

    def __str__(self):
        return "The name of this KnightErrant is " + self.name + " and his money is " + str(self.wealth)
