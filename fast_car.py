import base_car

class FastCar(base_car.AverageCar):
    def __init__(self):
        super().__init__()
        self.maxSpeed *= 3
        self.accelarationRate *= 2
