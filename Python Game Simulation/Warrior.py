from Fighter import *
import random


class Warrior(Fighter):
    """
    This class is the Warrior class and has an additional functionality where there is a list he can use to store
    all challenge requests made to the Warrior.

    """
    def __init__(self, name: str, age: int, wealth: int, skills: dict):
        """
        This function is a constructor for the Warrior class

        :param name: The string representation of the name of the Warrior
        :param age: The integer value of the name of the Warrior
        :param wealth: The wealth of the Warrior
        :param skills: The dictionary of the information of the warriors skills
        """
        Fighter.__init__(self, name, age, wealth, skills)
        self.fight_list = list()
        self.fight_item = list()

    def challenge_request(self, challenger: Fighter, item: str):
        """
        This method is called by the challenge class in Fighter. It is used to store the information of that challenge
        until the Fighter decides to accept or decline.

        :param challenger: The Fighter that has challenged this warrior.
        :param item: The item used to challenge this warrior
        """
        self.fight_list.append(challenger)
        self.fight_item.append(item)

    def accept_first(self):
        """
        This function is used to accept the first challenge stored in the list
        """
        from Fight import Fight
        from KnightErrant import KnightErrant
        if isinstance(self, KnightErrant):
            if self.traveling:
                print("Knight is traveling cannot accept challenge")
                return
        request = self.fight_list.pop()
        item = self.fight_item.pop()
        print(self.name + " is a " + self.__class__.__name__ +
              " and " + request.name + " is a " + request.__class__.__name__)
        # First case if its a fighter we have to check if withdrawal is allowed
        # if not request.challenge_dict[self]:
        print(self.name + " accepted " + request.name + "'s challenge")
        fight2 = Fight(self, request, item)
        print("Winner:" + fight2.winner)
        # A fight has happened so change all the statuses of challenge so they can choose to challenge or not
        #    self.challenge_status_change()
        #    request.challenge_status_change()

    def accept_random(self):
        """
        This function is used to accept a random challenge stored in the list
        """
        from Fight import Fight
        from KnightErrant import KnightErrant
        if isinstance(self, KnightErrant):
            if self.traveling:
                print("Knight is traveling cannot accept challenge")
                return
        select = random.randrange(len(self.fight_list))
        request = self.fight_list.pop(select)
        item = self.fight_item.pop(select)
        print(self.name + " is a " + self.__class__.__name__ +
              " and " + request.name + " is a " + request.__class__.__name__)
        print(self.name + " accepted " + request.name + "'s challenge")
        fight2 = Fight(self, request, item)
        print("Winner:" + fight2.winner)
        # A fight has happened so change all the statuses of challenge so they can choose to challenge or not
        # self.challenge_status_change()
        # request.challenge_status_change()

    def decline_first(self):
        """
        This function is usd to decline the first challenge in the list
        """
        from KnightErrant import KnightErrant
        if isinstance(self, KnightErrant):
            if self.traveling:
                print("Knight is traveling cannot accept challenge")
                return
        request = self.fight_list.pop()
        self.fight_item.pop()
        print(request.name + "'s challenge has been declined by " + self.name)

    def decline_random(self):
        """
        This function is used to decline a random challenge in the list
        """
        from KnightErrant import KnightErrant
        if isinstance(self, KnightErrant):
            if self.traveling:
                print("Knight is traveling cannot accept challenge")
                return
        select = random.randrange(len(self.fight_list))
        request = self.fight_list.pop(select)
        self.fight_item.pop(select)
        print(request.name + "'s challenge has been declined by " + self.name)

    @property
    def __str__(self):
        """
        This function is used to return the string representation of the Warrior object.

        :return: The string containing the name and wealth.
        """
        return "The name of this Warrior is " + self.name + " and his money is " + str(self.wealth)
