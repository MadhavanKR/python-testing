import sys

from fancy_car import FancyCar
from fast_car import FastCar
from slow_car import SlowCar

def testSlowCar():
    print('simulating slow car')
    car_1 = SlowCar()
    car_1.on()
    car_1.gas(1)
    car_1.drive(10)
    car_1.brake(3)
    car_1.stats()
    car_1.off()

def testFastCar():
    print('simulating fast car')
    car_1 = FastCar()
    car_1.on()
    car_1.gas(1)
    car_1.drive(10)
    car_1.brake(3)
    car_1.stats()
    car_1.off()

def testFancyCar():
    print('simulating fancy car')
    car_2 = FancyCar()
    car_2.lights()
    car_2.on()
    car_2.gear('reverse')
    car_2.gas(1)
    car_2.drive(10)
    car_2.stats()

def simulateProblemStatement():
    slowCar, fastCar, fancyCar = SlowCar(), FastCar(), FancyCar()
    slowCar.on(), fastCar.on(), fancyCar.on()
    fastCar.lights(), slowCar.lights()
    slowCar.gas(11), fastCar.gas(11), fancyCar.gas(10)
    slowCar.drive(30), fastCar.drive(30), fancyCar.drive(30)
    fancyCar.brake(4), fancyCar.drive(3)
    slowCar.brake(6)
    fancyCar.brake(sys.maxsize), fancyCar.gear('reverse'), fancyCar.gas(20), fancyCar.drive(30)
    fancyCar.lights()
    fastCar.drive(30), fastCar.gas(20), fastCar.drive(60)
    slowCar.brake(sys.maxsize), slowCar.off()
    print('slow car dashboard:'), slowCar.stats()
    print('\nfast car dashboard:'), fastCar.stats()
    print('\nfancy car dashboard:'), fancyCar.stats()
    fancyCar.horn()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(
            'please provide an input: \n"slow" to simulate slow car\n"fast" to simulate fast car\n"fancy" to simulate fancy car\n"all" to simulate scenario described in problem statement')
        exit(1)
    if sys.argv[1] == 'slow':
        testSlowCar()
    elif sys.argv[1] == 'fast':
        testFastCar()
    elif sys.argv[1] == 'fancy':
        testFancyCar()
    elif sys.argv[1] == 'all':
        simulateProblemStatement()
    else:
        print(
            'please provide a valid input: \n"slow" to simulate slow car\n"fast" to simulate fast car\n"fancy" to simulate fancy car\n"all" to simulate scenario described in problem statement')
        exit(1)
