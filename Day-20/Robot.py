class Robot:
    """
    This class is the tempalte for the robot Object.
    """
    population = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Robot.population += 1


    def setEnergy(self, energy):
        self.energy = energy

    def __del__(self):
        print(f'{self.name} is destroyed')

    def __add__(self, other):
        if isinstance(other, Robot):
            return self.price + other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Robot):
            return self.price < other.price
        return NotImplemented


r1 = Robot("Robo1", 1000)
print(f'Robot Name {r1.name} and Price {r1.price}')
r1.setEnergy(500)
print(r1.energy)

print(Robot.population)


r2 = Robot("Robo2", 10000)
print(f'Robot Name {r2.name} and Price {r2.price}')
r2.setEnergy(5000)
print(r2.energy)
#
print(Robot.population)
#
print(r1 + r2)
#
print(r1 < r2)
#
r3 = Robot("Robo3", 20000)
print(Robot.population)

