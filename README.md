## A port of the LiquidCrystal (HD44780)  Arduino library for the Raspberry Pi using Python

### Currently supports 4-bit mode only (8/26/17)

### Usage:

Wire LCD pins RS, E, D4 to D7 to any GPIO pins. Example: ![RPi LCD](http://www.teachmemicro.com/wp-content/uploads/2017/08/RPi-LCD.jpg)

 

Import LiquidCrystalPi and initiate class LCD:

```python
import LiquidCrystalPi

LCD = LiquidCrystalPi.LCD(<rs>,<enable>,<d4>,<d5>,<d6>,<d7>)
LCD.begin(<columns>, <lines>)
```

Write string:

```python
LCD.write("<string>")
```

Also needs RPi.GPIO as import


See [HelloWorldPi.py](https://github.com/kurimawxx00/LiquidCrystalPi/blob/master/HelloWorldPi.py) for complete code


### Available Commands (as of 8/26/2017):

 ```python
 command(value)                 #send a command

 write(string or character)     #write a string or character

 clear()                        #clear LCD screen

 home()                         #set cursor to row 1, col 1

 nextline()                     #set cursor to row 2

 moveright()                    #move cursor one position to the right

 moveleft()                     #move cursor one position to the left
 ```

### The contents of this library and README will be continuously updated.

# LiquidCrystalPi
