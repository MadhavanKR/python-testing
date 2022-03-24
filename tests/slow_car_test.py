from base_car import AverageCar
from fast_car import FastCar
from slow_car import SlowCar

class TestSlowCar:

    def test_attribute_value_correctness(self):
        averageCar = AverageCar()
        slowCar = SlowCar()
        assert slowCar.maxSpeed == 0.75 * averageCar.maxSpeed and slowCar.accelarationRate == 0.75 * averageCar.accelarationRate and slowCar.brakeEfficiency == 2 * averageCar.brakeEfficiency
