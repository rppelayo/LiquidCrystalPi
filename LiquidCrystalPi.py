_rs_pin = None
_rw_pin = None
_enable_pin = None
_data_pins = [None]*4
_numlines = 0
_displayfunction = 0
_displaycontrol = 0
_row_offsets = [None]*4

class LCD:
        import RPi.GPIO as GPIO
        import time as time

	def __init__(self, rs, enable, d0, d1, d2, d3):
		global _rs_pin, _enable_pin, _data_pins

		_rs_pin = rs
		_enable_pin = enable
		_data_pins[0] = d0
		_data_pins[1] = d1
		_data_pins[2] = d2
		_data_pins[3] = d3
  
		self.GPIO.setup(_rs_pin, self.GPIO.OUT)
		self.GPIO.setup(_enable_pin, self.GPIO.OUT)
		self.begin(16, 1)

	def begin(self, cols, lines):
		global _displayfunction, _numlines, _displacontrol, _displaymode
 
		if lines > 1:
		 _displayfunction |= 0x08

		 _numlines = lines
   
		 self.setRowOffsets(0x00, 0x40, 0x00 + cols, 0x40 + cols)
   
		 self.time.sleep(0.05)
		 self.GPIO.output(_rs_pin, 0)
		 self.GPIO.output(_enable_pin, 0)
   
		 self.write4bits(0x03)
		 self.time.sleep(0.0041)
		 self.write4bits(0x03)
		 self.time.sleep(0.0041)
		 self.write4bits(0x03)
		 self.time.sleep(0.00015)
		 self.write4bits(0x02)
   
		 self.command(0x20 | _displayfunction)
   
		 _displaycontrol = 0x04 | 0x00 | 0x00
		 self.display()
   
		 self.clear()
   
		 _displaymode = 0x02 | 0x00
		 self.command(0x04 | _displaymode)
  
	def setRowOffsets(self,row0,row1,row2,row3):
		_row_offsets[0] = row0;
		_row_offsets[1] = row1;
		_row_offsets[2] = row2;
		_row_offsets[3] = row3;
  
	def clear(self):
		self.command(0x01)
		self.time.sleep(0.002)
  
	def home(self):
		self.command(0x02)
		self.time.sleep(0.002)
  
	def nextline(self):
		self.command(0x0c)
		self.time.sleep(0.002)
 
	def display(self):
		global _displaycontrol

		_displaycontrol |= 0x04
		self.command(0x08 | _displaycontrol)
 
	def command(self,value):
		self.send(value, 0)

	def write(self,value):
		char = list(value)
		for i in range (0, len(char)):
			self.send(ord(char[i]), 1)
  
	def send(self,value, mode):
		global _rs_pin

		self.GPIO.output(_rs_pin, mode)
		self.write4bits(value >> 4)
		self.write4bits(value)
  
	def pulseEnable(self):
		self.GPIO.output(_enable_pin, 0)
		self.time.sleep(0.000001)
		self.GPIO.output(_enable_pin, 1)
		self.time.sleep(0.000001)
		self.GPIO.output(_enable_pin, 0)
		self.time.sleep(0.0001)
 
	def write4bits(self,value):
		for i in range(0,4):
			self.GPIO.setup(_data_pins[i], self.GPIO.OUT)
			self.GPIO.output(_data_pins[i], (value >> i) & 0x01)

		self.pulseEnable() 
