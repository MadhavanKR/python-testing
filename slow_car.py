import base_car

class SlowCar(base_car.AverageCar):
    def __init__(self):
        super().__init__()
        self.maxSpeed *= 0.75
        self.accelarationRate *= 0.75
        self.brakeEfficiency *= 2
