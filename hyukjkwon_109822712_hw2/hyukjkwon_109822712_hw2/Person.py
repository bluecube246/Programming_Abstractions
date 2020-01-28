class Person:
    """
    This class is used to represent the person object. This class will be a superclass for all classes except Fight.

    """
    def __init__(self, name: str, age: int, wealth: int = 0):
        """
        This method initialises the person object.

        :param name: The name of the person
        :param age: The age of the person
        :param wealth: The wealth of the Person
        """
        self.name = name
        self.age = age
        self.wealth = wealth
        if age >= 18:
            self.adult = True
        else:
            self.adult = False


