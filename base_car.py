class AverageCar:
    validGears = ['Park', 'Drive', 'Reverse']
    def __init__(self):
        self.maxSpeed = 50
        self.accelarationRate = 5
        self.brakeEfficiency = 10
        self.engineStatus = False
        self.speed = 0
        self.headlightStatus = -1
        self.distanceCovered = 0
        self.distanceFromHome = 0
        self.curGear = 'Park'

    def gas(self, time):
        if not self.engineStatus:
            raise Exception('cannot apply gas when engine is turned off')

        self.speed = min(self.maxSpeed, self.speed + time * self.accelarationRate)

    def lights(self):
        self.headlightStatus *= -1

    def drive(self, time):
        if not self.engineStatus:
            raise Exception('cannot drive when engine is turned off')

        self.distanceCovered += time * self.speed
        self.distanceFromHome = self.distanceCovered

    def brake(self, time):
        if not self.engineStatus:
            raise Exception('cannot brake when engine is turned off')
        self.speed = max(0, self.speed - self.brakeEfficiency * time)

    def on(self):
        if self.engineStatus:
            raise Exception('engine is already on')
        self.engineStatus = True

    def off(self):
        if self.speed == 0 and self.engineStatus:
            self.engineStatus = False
        elif self.speed > 0:
            raise Exception('cannot turn off when car is moving')
        else:
            raise Exception('engine already turned off')

    def stats(self):
        print('engine: {}'.format('On' if self.engineStatus else 'Off'))
        print('lights: {}'.format('On' if self.headlightStatus == 1 else 'Off'))
        print('speed: {} m/s'.format(self.speed))
        print('odometer: {} m'.format(self.distanceCovered))
        print('home: {} m'.format(self.distanceFromHome))
        print('gear: {}'.format(self.curGear))