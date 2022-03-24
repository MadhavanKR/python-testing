import pytest

from base_car import AverageCar

class TestAverageCar:

    def test_engine_on(self):
        averageCar = AverageCar()
        # turn on the engine
        averageCar.on()
        # assert that engine status is on
        assert averageCar.engineStatus

    def test_engine_on_negative(self):
        with pytest.raises(Exception) as e:
            averageCar = AverageCar()
            averageCar.on()
            # turn off the engine again
            averageCar.on()
        # assert that proper error message is shown
        assert str(e.value) == 'engine is already on'

    def test_engine_off(self):
        averageCar = AverageCar()
        # turn on the engine
        averageCar.on()
        # turn off the engine
        averageCar.off()
        # assert that engine status is off
        assert averageCar.engineStatus == False

    def test_engine_off_negative(self):
        with pytest.raises(Exception) as e:
            averageCar = AverageCar()
            averageCar.on()
            averageCar.off()
            # turn off the engine again
            averageCar.off()
        # assert that proper error message is shown
        assert str(e.value) == 'engine already turned off'

    def test_engine_off_when_running(self):
        with pytest.raises(Exception) as e:
            averageCar = AverageCar()
            averageCar.on()
            averageCar.gas(1)
            averageCar.drive(1)
            # turn off the engine again
            averageCar.off()
        # assert that proper error message is shown
        assert str(e.value) == 'cannot turn off when car is moving'

    def test_gas_when_on(self):
        averageCar = AverageCar()
        averageCar.on()
        averageCar.gas(2)
        assert averageCar.speed == 10

    def test_gas_when_off(self):
        with pytest.raises(Exception) as e:
            averageCar = AverageCar()
            averageCar.gas(2)
        # assert that proper error message is shown
        assert str(e.value) == 'cannot apply gas when engine is turned off'


    def test_gas_maxspeed(self):
        averageCar = AverageCar()
        averageCar.on()
        averageCar.gas(1000)
        assert averageCar.speed == averageCar.maxSpeed

    def test_drive_when_on(self):
        averageCar = AverageCar()
        averageCar.on()
        averageCar.gas(2)
        averageCar.drive(10)
        assert averageCar.distanceCovered == 100 and averageCar.distanceFromHome == 100

    def test_drive_when_off(self):
        with pytest.raises(Exception) as e:
            averageCar = AverageCar()
            averageCar.drive(1)
        # assert that proper error message is shown
        assert str(e.value) == 'cannot drive when engine is turned off'

    def test_brake_when_on(self):
        averageCar = AverageCar()
        averageCar.on()
        averageCar.gas(5)
        averageCar.brake(1)
        assert averageCar.speed == 15

    def test_brake_to_stop(self):
        averageCar = AverageCar()
        averageCar.on()
        averageCar.gas(5)
        averageCar.brake(100)
        assert averageCar.speed == 0

    def test_brake_when_off(self):
        with pytest.raises(Exception) as e:
            averageCar = AverageCar()
            averageCar.brake(1)
        # assert that proper error message is shown
        assert str(e.value) == 'cannot brake when engine is turned off'

    def test_lights_on(self):
        averageCar = AverageCar()
        # turn on lights
        averageCar.lights()
        assert averageCar.headlightStatus == 1

    def test_lights_off(self):
        averageCar = AverageCar()
        # turn on lights
        averageCar.lights()
        # turn off lights
        averageCar.lights()
        assert averageCar.headlightStatus == -1