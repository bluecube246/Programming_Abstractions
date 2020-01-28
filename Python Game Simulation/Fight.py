import random
from random import randint
from Fighter import Fighter
from Warrior import Warrior
from KnightErrant import KnightErrant


class Fight:
    """
    This represents the fight class.
    This class will represent different scenarios in two fighters fighting and the results such as wealth and skill points change.
    """
    def __init__(self, f1: Fighter, f2: Fighter, skill: str):
        """
        This constructor is used to initialize the winner of this fight

        :param f1: The first fighter
        :param f2: The second fighter
        :param skill: The skill that is going to be used to fight
        """
        if (type(f1) is Warrior) & (type(f2) is Fighter):
            self.Winner = self.fight(f1, f2, skill, 10, 25, 1, 0)
        elif (type(f1) is KnightErrant) & (type(f2) is Fighter):
            self.Winner = self.fight(f1, f2, skill, 10, 40, 2, 0)
        elif (type(f1) is KnightErrant) & (type(f2) is Warrior):
            self.Winner = self.fight(f1, f2, skill, 10, 20, 1, 0)
        elif (type(f1) is Warrior) & (type(f2) is KnightErrant):
            self.Winner = self.fight(f1, f2, skill, 20, 10, 0, 1)
        else:
            self.Winner = self.fight(f1, f2, skill, 10, 10, 0, 0)

    @staticmethod
    def fight(f1: Fighter, f2: Fighter, skill: str, a: int, b: int, c: int, d: int):
        """
        This method is used to carryout the actual results of fight

        :param f1: The first fighter
        :param f2: The second fighter
        :param skill: The skill the two fighters would fight with
        :param a: The addition/subtraction of wealth depending on the match up
        :param b: The second scenario of the addition/subtraction of wealth depending on the match up
        :param c: The increase in amount of skill depending on a certain scenario
        :param d: The increase in the amount of skill depending on a certain scenario
        :return: The winner of the fight
        """

        fighter_1_random = randint(0, 1)
        fighter_2_random = randint(0, 1)
        if fighter_1_random == 1:
            if f1.skills[skill] == 10:
                f1.skills[skill] = 10
                print(f1.name + "'s " + skill + " skill is already maxed")
            else:
                f1.skills[skill] += fighter_1_random
                print("Random fight increase: " + f1.name + "'s " + skill + " has increased to " + str(f1.skills[skill]) + " (+" + str(1) + ")")

        if fighter_2_random == 1:
            if f2.skills[skill] == 10:
                f2.skills[skill] = 10
                print(f2.name + "'s " + skill + " skill is already maxed")
            else:
                f2.skills[skill] += fighter_2_random
                print("Random fight increase: " + f2.name + "'s " + skill + " has increased to " + str(f2.skills[skill]) + " (+" + str(1) + ")")

        if f1.skills[skill] > f2.skills[skill]:
            f1.wealth += a
            if f1.skills[skill] + d > 10:
                f1.skills[skill] = 10
                print(f1.name + "'s " + skill + " skill is already maxed")
            else:
                f1.skills[skill] += d
            if not d == 0:
                print("Victory increase: " + f1.name + "'s " + skill + " has increased to " + str(f1.skills[skill]) + " (+" + str(d) + ")")
            if (f2.wealth - a) < 0:
                f2.wealth = 0
            else:
                f2.wealth -= a
            return f1.name
        elif f1.skills[skill] < f2.skills[skill]:
            if (f1.wealth - b) < 0:
                f1.wealth = 0
            else:
                f1.wealth -= b
            f2.wealth += b
            if f2.skills[skill] + c > 10:
                f2.skills[skill] = 10
                print(f2.name + "'s " + skill + " skill is already maxed")
            else:
                f2.skills[skill] += c
            if not c == 0:
                print("Victory increase: " + f2.name + "'s " + skill + " has increased to " + str(f2.skills[skill]) + " (+" + str(c) + ")")
            return f2.name
        else:
            winner = random.choice([f1, f2])
            if winner == f1:
                f1.wealth += a
                if f1.skills[skill] + d > 10:
                    f1.skills[skill] = 10
                    print(f1.name + "'s " + skill + " skill is already maxed")
                else:
                    f1.skills[skill] += d
                if not d == 0:
                    print("Victory increase: " + f1.name + "'s " + skill + " has increased to " + str(f1.skills[skill]) + " (+" + str(d) + ")")
                if (f2.wealth - a) < 0:
                    f2.wealth = 0
                else:
                    f2.wealth -= a
                return f1.name
            else:
                if f1.wealth - b < 0:
                    f1.wealth = 0
                else:
                    f1.wealth -= b
                f2.wealth += b
                if f2.skills[skill] + c > 10:
                    f2.skills[skill] = 10
                    print(f2.name + "'s " + skill + " skill is already maxed")
                else:
                    f2.skills[skill] += c
                if not c == 0:
                    print("Victory increase: " + f2.name + "'s " + skill + " has increased to " + str(f2.skills[skill]) + " (+" + str(c) + ")")
                return f2.name

    @property
    def winner(self):
        """
        This is the getter method of the winner of this specific fight.

        :return: The winner of this fight.
        """
        return self.Winner

