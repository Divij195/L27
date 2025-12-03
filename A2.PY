class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.maxspeed = max_speed
        self.mileage = mileage

obj=Vehicle("Audi Car",250, 19)
print("Vehicle name:", obj.name)
print("Speed:", obj.maxspeed)
print("Mileage:", obj.mileage)

obj2=Vehicle("BMW Car",230, 20)
print("Vehicle name:", obj2.name)
print("Speed:", obj2.maxspeed)
print("Mileage:", obj2.mileage)



