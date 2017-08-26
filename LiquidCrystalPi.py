import RPi.GPIO as GPIO
import time as time

_rs_pin = None
_rw_pin = None
_enable_pin = None
_data_pins = [None]*4
_numlines = 0
_displayfunction = 0
_displaycontrol = 0
_row_offsets = [None]*4
#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def LCD_Init(rs, enable, d0, d1, d2, d3):
  global _rs_pin, _enable_pin, _data_pins

  _rs_pin = rs
  _enable_pin = enable
  _data_pins[0] = d0
  _data_pins[1] = d1
  _data_pins[2] = d2
  _data_pins[3] = d3
  
  GPIO.setup(_rs_pin, GPIO.OUT)
  GPIO.setup(_enable_pin, GPIO.OUT)
  LCD_Begin(16, 1)

def LCD_Begin(cols, lines):
  global _displayfunction, _numlines, _displacontrol, _displaymode
 
  if lines > 1:
   _displayfunction |= 0x08

  _numlines = lines
   
  LCD_setRowOffsets(0x00, 0x40, 0x00 + cols, 0x40 + cols)
   
  time.sleep(0.05)
  GPIO.output(_rs_pin, 0)
  GPIO.output(_enable_pin, 0)
   
  write4bits(0x03)
  time.sleep(0.0041)
  write4bits(0x03)
  time.sleep(0.0041)
  write4bits(0x03)
  time.sleep(0.00015)
  write4bits(0x02)
   
  command(0x20 | _displayfunction)
   
  _displaycontrol = 0x04 | 0x00 | 0x00
  LCD_display()
   
  LCD_clear()
   
  _displaymode = 0x02 | 0x00
  command(0x04 | _displaymode)
  
def LCD_setRowOffsets(row0,row1,row2,row3):
   _row_offsets[0] = row0;
   _row_offsets[1] = row1;
   _row_offsets[2] = row2;
   _row_offsets[3] = row3;
  
def LCD_clear():
  command(0x01)
  time.sleep(0.002)
  
def LCD_home():
  command(0x02)
  time.sleep(0.002)
 
def LCD_display():
  global _displaycontrol

  _displaycontrol |= 0x04
  command(0x08 | _displaycontrol)
 
def command(value):
  send(value, 0)

def LCD_write(value):
  char = list(value)
  for i in range (0, len(char)):
   send(ord(char[i]), 1)
  
def send(value, mode):
  global _rs_pin

  GPIO.output(_rs_pin, mode)
  write4bits(value >> 4)
  write4bits(value)
  
def pulseEnable():
  GPIO.output(_enable_pin, 0)
  time.sleep(0.000001)
  GPIO.output(_enable_pin, 1)
  time.sleep(0.000001)
  GPIO.output(_enable_pin, 0)
  time.sleep(0.0001)
 
def write4bits(value):
  for i in range(0,4):
    GPIO.setup(_data_pins[i], GPIO.OUT)
    GPIO.output(_data_pins[i], (value >> i) & 0x01)

  pulseEnable()
 
 
