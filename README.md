## A port of the LiquidCrystal (HD4470)  Arduino library for the Raspberry Pi using Python

### Currently supports 4-bit mode only (8/26/17)

### Usage:

Import LiquidCrystalPi and initiate class LCD:

```python
import LiquidCrystalPi

LCD = LiquidCrystalPi.LCD(<rs>,<enable>,<d4>,<d5>,<d6>,<d7>)
LCD.begin(16, 2)
```

Write string:

```python
LCD.write("Hello World")
```

See [HelloWorldPi.py](https://github.com/kurimawxx00/LiquidCrystalPi/blob/master/HelloWorldPi.py) for complete code


### Available Commands (as of 8/26/2017):

 command(int)

 write(string)

 clear()

 home()

 nextline()

### The contents of this library and README will be continuously updated.

# LiquidCrystalPi
