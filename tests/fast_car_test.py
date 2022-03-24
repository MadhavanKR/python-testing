from base_car import AverageCar
from fast_car import FastCar

class TestFastCar:

    def test_attribute_value_correctness(self):
        averageCar = AverageCar()
        fastCar = FastCar()
        assert fastCar.maxSpeed == 3 * averageCar.maxSpeed and fastCar.accelarationRate == 2 * averageCar.accelarationRate and fastCar.brakeEfficiency == averageCar.brakeEfficiency
