import random  # Importing random

min_roll = 1   # Min roll value
max_roll = 10  # Max roll value

print("Welcome to the game.\n")  # This welcomes you to the game.

enter = input("Please press Enter to continue.")  # Press the Enter key to continue the game.

name = input("Choose your name.\n")  # Choose the name of your character.


class Warrior:  # The Warrior class values.
    Name = "warrior"
    HP = 10
    ATK = 10
    DEF = 10
    Damage = random.randint(1, 10)


class Mage:  # The Mage class values.
    Name = "mage"
    HP = 10
    ATK = 10
    DEF = 5
    Damage = random.randint(1, 10)


class Rogue:  # The Rogue class values.
    Name = "rogue"
    HP = 10
    ATK = 10
    DEF = 8
    Damage = random.randint(1, 10)


class Enemy:
    def __init__(self, Name, HP, ATK, DEF, Damage):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.Damage = Damage


def attack(attacker, attackee):  # The attack function
    hit = random.randint(min_roll, max_roll) + attacker.ATK
    death = 0

    if (hit > attackee.DEF):
        print(attacker.Name, "inflicts", attacker.Damage)

        attackee.HP = attackee.HP - attacker.Damage

        if attackee.HP <= 0:  # if the attackee's health drops below zero
            print("With a forceful attack,", attackee.Name, "dies.")
            death = 1

        else:
            print(attackee.Name, "has", attackee.HP, "HP remaining.")
            death = 0

    else:
        print("You missed. Better defend!")

    return death


def fight(attacker, enemy):  # The attack loop
    death = 0
    while death == 0:
        death = attack(attacker, enemy)

        if death == 0:
            death = attack(enemy, attacker)
        else:
            return "enemy"
    return "you"


def buff(player):  # Function for buffing the player
    print("\nYou've leveled up!")
    player.HP = player.HP + 5  # Increases player HP by 5
    player.ATK = player.ATK + 5  # Increases player Attack by 5
    player.DEF = player.DEF + 5  # Increases player Defense by 5

    print("HP", player.HP)
    print("Attack", player.ATK)
    print("Defense", player.DEF)


user_class = input("Choose a class between Warrior, Mage, or Rogue.\n")   # Input what class you want to be.

while(user_class != 'Warrior' and user_class != 'Mage' and user_class != 'Rogue'):  # If you input another class other than the 3 specified, it gives that print statement and re-runs the class input.
    print("You did not choose from the required classes, try again.")
    user_class = input()

if user_class.lower() == 'warrior':  # Sets the user input to the class
    theClass = Warrior()
elif user_class.lower() == 'mage':
    theClass = Mage()
elif user_class.lower() == 'rogue':
    theClass = Rogue()

print("You are now ready to play.\n")  # Tells the user that they are ready to play the game.

enter = input("Please press Enter to continue.\n")  # Press the enter key to continue the game.

while True:
    print("This is your HP.", theClass.HP)  # Tells you your HP value
    print("This is your Attack.", theClass.ATK)  # Tells you your Attack value
    print("This is your Defense.", theClass.DEF)  # Tells you your Defense value

    enter = input("Please press Enter to continue.\n")

    print("An old mage tells you to go to the Dungeon and kill a Skeleton to prove your worth.\n")  # NPC tells you to go kill a monster to prove your worth.

    enter = input("Please press Enter to continue.\n")

    skeleton1 = Enemy("The Skeleton", 10, 4, 5, 5)  # This creates a new Skeleton enemy. The order is the Name, HP, ATK, DEF, and Damage.

    if fight(theClass, skeleton1) == "enemy":
        print("The enemy is dead")
        buff(theClass)  # This calls the buff function to give the player a level up (of sorts)
    else:
        print("You're dead")
        enter = input("Please press Enter to continue.\n")
        continue  # Returns to the start of the loop
