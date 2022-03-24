# Dependencies

1. python3
2. Using pytest to run test cases. (pip install pytest)
3. Using pytest-html plugin to generate a html report. (pip install pytest-html)

# Implementation Details

1. Average car implementation is present in **base_car.py**
2. Slow car implementation is present in **slow_car.py**
3. Fast car implementation is present in **fast_car.py**
4. Fancy car implementation is present in **fancy_car.py**
5. All tests are present in **tests/** folder

# Test cases

A total of **23** test cases have been implemented. Following are their brief description, grouped based on the functionality they test.

Following functionalities are tested on AverageCar.

<table>
<tr>
<th>Functionality</th> <th>test cases</th>
</tr>
<tr>
<td>Engine on</td> <td> 1. Positive case: Turn engine on from off state.

2. Negative case: Turn engine on when it is already on</td>
</tr>
<tr>
<td>Engine off</td> <td> 
1. Positive case: Turn engine off from on state.

2. Negative case: Turn engine off when it is already off
2. Negative case: Turn engine off when speed > 0 </td>
</tr>

<tr>
<td>Gas</td> <td> 
1. Gas when engine is on.

2. Gas when engine is off
2. Gas for long duration and validate speed against maxSpeed </td>
</tr>


<tr>
<td>Drive</td> <td> 
1. Drive when engine is on.

2. Drive when engine is off
</td>
</tr>

<tr>
<td>Brake</td> <td> 
1. Brake when engine is on.

2. Brake when engine is off
3. Apply brake for long duration and validate speed = 0
</td>
</tr>

<tr>
<td>Lights</td> <td> 
1. lights() must turn on the light when it is off.

2. lights() must turn off the light when it is on.
</td>
</tr>

</table>

Following functionalities are tested on SlowCar.
<table>
<tr>
<th>Functionality</th> <th>test cases</th>
</tr>
<tr>
<td>Attribute value correctness</td> <td>Validate that maxspeed, accelarationRate, brakeEfficiency of slowCar is 0.75, 0.75, 2 times that of AverageCar</td>
</tr>
</table>

Following functionalities are tested on FastCar.
<table>
<tr>
<th>Functionality</th> <th>test cases</th>
</tr>
<tr>
<td>Attribute value correctness</td> <td>Validate that maxspeed, accelarationRate, brakeEfficiency of slowCar is 3, 2, 1 times that of AverageCar</td>
</tr>
</table>

Following functionalities are tested on FancyCar.
<table>
<tr>
<th>Functionality</th> <th>test cases</th>
</tr>
<tr>
<td>Attribute value correctness</td> <td>Validate that maxspeed, accelarationRate, brakeEfficiency of slowCar is 2, 1, 1 times that of AverageCar</td>
</tr>
<tr>
<td>Gear</td> <td>1. Valid gear change operation

2. Change gear to an invalid gear i.e gear value not equal to 'Park', 'Drive' or 'Reverse'
2. Change gear when speed > 0
2. validate the distanceFromHome when gear is changed to Reverse and driven.</td>
</tr>
<tr><td>horn</td> <td>1. Validate horn functionality</td></tr>
</table>



# Execution

## Program execution

Program can be executed by running the main.py with following command

The program takes a single command line argument that specifies which simulation to run.
**slow, fast, fancy** values run a simulation for slow, fast and fancy cars respectively. Whereas
value **all** runs a scenario defined in problem statement.

```
python3 main.py all
or
python3 main.py slow
or
python3 main.py fast
or
python3 main.py fancy
```

## Test execution

All the tests are implemented in files residing in **tests/ folder**

**base_car_test.py** contains all tests regarding AverageCar (base class)

**slow_car_test.py** contains all tests regarding SlowCar

**fast_car_test.py** contains all tests regarding FastCar

**fancy_car_test.py** contains all tests regarding FancyCar


to run all the test cases, run the following command:

```commandline
python3 -m pytest -q tests
```

To generate a html report, run the following command. This will generate a **report.html** file in the directory from which command was run.
this html file can be opened from browser.

```commandline
python3 -m pytest --html=report.html --self-contained-html -q tests
```

