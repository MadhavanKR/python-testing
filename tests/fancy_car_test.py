import pytest

from base_car import AverageCar
from fancy_car import FancyCar
from fast_car import FastCar
from slow_car import SlowCar

class TestFancyCar:

    def test_attribute_value_correctness(self):
        """This is a sample description"""
        averageCar = AverageCar()
        fancyCar = FancyCar()
        assert fancyCar.maxSpeed == 2 * averageCar.maxSpeed and fancyCar.accelarationRate == averageCar.accelarationRate and fancyCar.brakeEfficiency == averageCar.brakeEfficiency

    def test_gear_change(self):
        fancyCar = FancyCar()
        fancyCar.gear('reverse')
        assert fancyCar.curGear == 'reverse'

    def test_gear_change_invalid(self):
        with pytest.raises(Exception) as e:
            fancyCar = FancyCar()
            fancyCar.on()
            fancyCar.gear('invalid_gear')
        assert str(e.value) == 'invalid_gear is not a valid gear'

    def test_gear_change_when_moving(self):
        with pytest.raises(Exception) as e:
            fancyCar = FancyCar()
            fancyCar.on()
            fancyCar.gas(1)
            fancyCar.gear('reverse')
        assert str(e.value) == 'cannot change gear when car is moving'

    def test_reverse_gear_distance(self):
        fancyCar = FancyCar()
        fancyCar.on()
        fancyCar.gas(5), fancyCar.drive(10)
        fancyCar.brake(100)
        fancyCar.gear('reverse'), fancyCar.gas(5), fancyCar.drive(10)
        assert fancyCar.distanceFromHome == 0

    def test_horn(self):
        fancyCar = FancyCar()
        assert fancyCar.hornSound == 'beep beep'