from KnightErrant import*

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

print("1-------------------------------------------------------------------------")

# Fighter under 16
try:
    p0 = Fighter("Henry", 16, 30, dict(spear=1, unarmed_combat=1, mace=2, broadsword=3))
except ValueError as e:
    print(e.__str__())

print("2-----------------------------------------------------------------------------------")

# Fighter vs Fighter
print("Fighter vs Fighter")

p2 = Fighter("John", 21, 10, dict(spear=1, unarmed_combat=1, mace=2, broadsword=3))
p3 = Fighter("Paul", 21, 100, dict(spear=2, unarmed_combat=1, mace=4, broadsword=3))


print("Before fight {} wealth is {} and {} wealth is {}".format(p2.name, p2.wealth, p3.name, p3.wealth))

p2.challenge("spear", p3)

print("After fight {} wealth is {} and {} wealth is {}".format(p2.name, p2.wealth, p3.name, p3.wealth))

print("3------------------------------------------------------------------------------------------")

# Cannot fight with 0 wealth

p2.challenge("spear", p3)

print("4-------------------------------------------------------------------------")

# Warrior vs Fighter Warrior Wins wealth + 10
print("Warrior vs Fighter. Warrior wins")

p11 = Warrior("Jill", 21, 200, dict(spear=3, unarmed_combat=1, mace=0, broadsword=3))

print("Before fight {} wealth is {} and {} wealth is {}".format(p3.name, p3.wealth, p11.name, p11.wealth))

p3.challenge("spear", p11)

p11.accept_first()

print("After fight {} wealth is {} and {} wealth is {}".format(p3.name, p3.wealth, p11.name, p11.wealth))

print("5-------------------------------------------------------------------------")

# Warrior vs Fighter Warrior Wins wealth + 10

print("Warrior vs Fighter. Fighter wins")

print("Before fight {} wealth is {} and {} wealth is {}".format(p3.name, p3.wealth, p11.name, p11.wealth))

p3.challenge("mace", p11)

p11.accept_first()

print("After fight {} wealth is {} and {} wealth is {}".format(p3.name, p3.wealth, p11.name, p11.wealth))

print("6-----------------------------------------------------------")
# Warrior vs Fighter Draw

print("Warrior vs Fighter. Draw")

print("Before fight {} wealth is {} and {} wealth is {}".format(p3.name, p3.wealth, p11.name, p11.wealth))

p3.challenge("broadsword", p11)

p11.accept_first()

print("After fight {} wealth is {} and {} wealth is {}".format(p3.name, p3.wealth, p11.name, p11.wealth))

print("7-----------------------------------------------------------")
# KnightErrant vs Warrior. Warrior Wins

p12 = Warrior("Bill", 21, 100, dict(spear=10, unarmed_combat=1, mace=2, broadsword=3))

p111 = KnightErrant("Sam", 21, 150, dict(spear=10, unarmed_combat=1, mace=2, broadsword=0))

print("Before fight {} wealth is {} and {} wealth is {}".format(p12.name, p12.wealth, p111.name, p111.wealth))

p111.challenge("broadsword", p12)

p12.accept_first()

print("After fight {} wealth is {} and {} wealth is {}".format(p12.name, p12.wealth, p111.name, p111.wealth))

print("8 ------------------------------------------------")
# KnightErrant vs Fighter. Fighter Wins

p2 = Fighter("Chu", 23, 100, dict(spear=10, unarmed_combat=1, mace=2, broadsword=9))

print("Before fight {} wealth is {} and {} wealth is {}".format(p2.name, p2.wealth, p111.name, p111.wealth))

p111.challenge("broadsword", p2)

print("After fight {} wealth is {} and {} wealth is {}".format(p2.name, p2.wealth, p111.name, p111.wealth))

print("9 ------------------------------------------------")

print("KnightErrant vs Warrior. Warrior Wins + Travelling cases")

p111.travel()

p3.challenge("spear", p111)

p111.accept_first()

p111.challenge("spear", p3)

p111.return_from_travel()

print("Before fight {} wealth is {} and {} wealth is {}".format(p11.name, p11.wealth, p111.name, p111.wealth))

p11.challenge("spear", p111)

p111.accept_first()

p111.decline_first()

print("After fight {} wealth is {} and {} wealth is {}".format(p11.name, p11.wealth, p111.name, p111.wealth))

print("10 When a fighter has withdrawn--------------------------------------------------------")
# Fighter has withdrawn and accept/decline first/random case.

p13 = Warrior("Ben", 21, 100, dict(spear=10, unarmed_combat=1, mace=2, broadsword=3))

p3.challenge("spear", p13)
p3.challenge("mace", p13)
p3.challenge("mace", p111)
p3.challenge("spear", p111)

p13.accept_random()

p3.withdraw(p111, "spear")

p111.decline_random()

p13.decline_first()




