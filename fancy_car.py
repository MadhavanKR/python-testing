import base_car

class FancyCar(base_car.AverageCar):
    def __init__(self):
        super().__init__()
        self.maxSpeed *= 2
        self.hornSound = 'beep beep'

    def gear(self, newGear):
        if self.speed == 0 and newGear in [x.lower() for x in FancyCar.validGears]:
            self.curGear = newGear
        elif self.speed > 0:
            raise Exception('cannot change gear when car is moving')
        else:
            raise Exception('{} is not a valid gear'.format(newGear))

    def drive(self, time):
        if not self.engineStatus:
            raise Exception('cannot drive when engine is turned off')

        self.distanceCovered += time * self.speed
        if self.curGear.lower() == 'reverse':
            self.distanceFromHome = abs(self.distanceFromHome - self.speed * time)
        else:
            self.distanceFromHome += self.speed * time

    def horn(self):
        print(self.hornSound)