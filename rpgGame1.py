# 1. Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power of the goblin. Use a hero object in place of the variables hero_health and hero_power and use a goblin object in place of the variables goblin_health and goblin_power all through out the app.
# 2. Take the code for the hero attacking the goblin and extract it into a method (call it attack) of the Hero class. Replace the existing code with a call to the attack method. Hint: attack should take in the goblin (enemy) as a parameter: hero.attack(goblin)
# 3. Similarly, take the code for the goblin attacking the hero and extract it into a method (also call it attack) of the Goblin class. Replace the existing code with a call to the attack method. It should look like goblin.attack(hero).
# 4. Refactor the while condition:
# while goblin.health > 0 and hero.health > 0:
# to
# while goblin.alive() and hero.alive():
# The health checks should be moved to within the alive methods of Hero and Goblin respectively
# 5.Take the code for printing the health status of the hero and move it into a method called print_status of Hero. Do the same for the goblin.
# 6. Do you see a lot of duplicated or similar code between Hero and Goblin? What if you can share the duplicated code between them? You can by using inheritance! Create a new class called Character and make both Hero and Goblin inherit from it.
# 7a. The alive methods on Hero and Goblin should be identical. Move it into Character, and remove them from Hero and Goblin - now they can simply inherit it from Character.
# 7bonus. The methods attack and print_status method in Hero and Goblin look almost identical, but not quite. Is it possible to move them into the Character class as well? Give it a try.
# 8. Bonus Challenge: Create a zombie character that cannot die and have it fight the hero instead of the goblin. 

class Character:
    def __init__(self):
        self.name = ''
        self.health = 10
        self.power = 5
    
    def alive(self):
        while self.health > 0:
            return

    def attack(self, enemy):
        enemy.health -= self.power
        print("The %s does %d damage to the %s." % (self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("The %s is dead" % (enemy.name))

    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5

    # def attack(self, goblin):
    #     goblin.health -= self.power
    #     print("You do %d damage to the goblin." % self.power)
    #     if goblin.health <= 0:
    #         print("The goblin is dead.")
    
    # def alive(self):
    #     while self.health > 0:
    #         return
    
    # def print_status(self):
    #     print("The %s has %d health and %d power." % (self.name, self.health, self.power))


class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 6
        self.power = 2
    
    # def attack(self, hero):
    #     hero.health -= self.power
    #     print("The goblin does %d damage to you." % self.power)
    #     if hero.health <= 0:
    #         print("You are dead.")

    # def alive(self):
    #     while self.health > 0:
    #         return

    # def print_status(self):
    #     print("The %s has %d health and %d power." % (self.name, self.health, self.power))

# 8. Bonus Challenge: Create a zombie character that cannot die and have it fight the hero instead of the goblin.
class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.power = 1
    

kyle = Hero()
enemy1 = Goblin()

while kyle.health > 0 and enemy1.health > 0:
    kyle.print_status()
    enemy1.print_status()
    enemy1.attack(kyle)
    kyle.attack(enemy1)
    kyle.alive()
    enemy1.alive()


    
