from Person import *


class Fighter(Person):
    """
    This class is used to represent the fighter class. The fighter will extend the person class.
    The fighter must accept challenges requested but can withdraw challenges if he has fought after a challenge was accepted.

    """
    def __init__(self, name: str, age: int, wealth: int, skills: dict):
        """
        This is the constructor for the fighter class

        :param name: The name of the Person
        :param age: The age of the Person
        :param wealth: The wealth of the Fighter
        :param skills: The information of the skills the person has
        """
        Person.__init__(self, name, age, wealth)
        if not self.adult:
            raise ValueError("Not an adult cannot be a fighter")
        self.__skills = skills
        # self.challenge_dict = dict()

    @property
    def skills(self):
        """
        The getter method of the skills attribute declared as private

        :return: The skills dictionary containing the skills
        """
        return self.__skills

    @skills.setter
    def x(self, skills):
        """
        The setter method for the private attribute skills

        :param skills: Sets the given skills attribute
        """
        self.__skills = skills

    # # This will change all the elements in challenge_dict to True
    # def challenge_status_change(self):
    #     for status in self.challenge_dict:
    #         self.challenge_dict[status] = True

    def challenge(self: 'Fighter', my_skill: str, opponent: 'Fighter'):
        """
        This class is used for a fighter to challenge another fighter.
        Different statements will be executed depending on the opponents status.
        For example if the opponent is a fighter the fight will happen immediately.
        If not the fight will be passed into list.

        :param my_skill: The skill that the player is challenging the opponent
        :param opponent: The Fighter to challenge.
        """
        from Fight import Fight
        from Warrior import Warrior
        from KnightErrant import KnightErrant
        if self.wealth == 0 or opponent.wealth == 0:
            print("Wealth is needed to start a challenge")
            return
        if isinstance(self, KnightErrant):
            if self.traveling:
                print("Cannot challenge while traveling")
                return
        if my_skill not in self.skills.keys():
            print(my_skill)
            print(self.skills.keys())
            print("Invalid skill")
            return
        if self == opponent:
            print("You cannot fight yourself")
        if isinstance(opponent, KnightErrant):
            # print("Opponent is a KnightErrant")
            opponent.challenge_request(self, my_skill)
            print(self.name + " Challenges " + opponent.name + " Pending decision")
            #    if isinstance(self, Fighter):
        #        self.challenge_dict[opponent] = False
        if isinstance(opponent, Warrior):
            if not isinstance(opponent, KnightErrant):
                # print("Opponent is a warrior")
                opponent.challenge_request(self, my_skill)
                print(self.name + " Challenges " + opponent.name + " Pending decision")
        #        if isinstance(self, Fighter):
        #            self.challenge_dict[opponent] = False
        else:
            print(self.name + " Challenges " + opponent.name)
            print(self.name + " is a " + self.__class__.__name__ +
                  " and " + opponent.name + " is a " + opponent.__class__.__name__)
            fight1 = Fight(self, opponent, my_skill)
            print("Winner:" + fight1.winner)

    def withdraw(self, opponent: 'Fighter', item: str):
        """
        This function is used so that a fighter can withdraw a fight he has requested.

        :param opponent: The opponent to withdraw the request
        :param item: The item to be withdrawn
        """
        a = opponent.fight_list.index(self)
        b = [i for i, x in enumerate(opponent.fight_list) if opponent.fight_item[i] == item]
        opponent.fight_list.pop(b[0])
        c = opponent.fight_item.pop(b[0])
        print(self.name + " withdrew the challenge with " + opponent.name + " with the item " + "\"" + c + "\"")

    def __str__(self):
        """
        This method is used to return the string representation of the classes information

        :return: The string value containing the name and the wealth
        """
        return "The name of this Fighter is " + self.name + " and his wealth points is " + str(self.wealth)








