class byte:
  bits = [0,0,0,0,0,0,0,0]
  def __init__(self, val):
    if not (type(val) is int):
      raise ValueError("Byte value not of type int")
    if (val < 0 or val > 255):
      raise ValueError("Byte value out of range (" + str(val) + ")")
    for i in range(8):
      if (val >= 2 ** (7 - i)):
        val = val - (2 ** (7 - i))
        self.bits[i] = 1
      else:
        self.bits[i] = 0
  
  def toString(self):
    string = ""
    for i in range(8):
      string = string + str(self.bits[i])
    return string

  def bit(self, num):
    if not (type(num) is int):
      raise ValueError("Byte index not of type int")
    if (num < 0 or num > 7):
      raise ValueError("Byte index out of range (" + str(num) + ")")
    return self.bits[num]

class i2c:
  clkpin = 0
  datpin = 0
  minpin = 0
  maxpin = 9
  def __init__(self, clkpin, datpin):
    if (clkpin == datpin):
      raise ValueError("Clock and data pin conflict")
    if (clkpin < self.minpin or clkpin > self.maxpin):
      raise ValueError("Clock pin does not exist (" + str(clkpin) + ")")
    if (datpin < self.minpin or datpin > self.maxpin):
      raise ValueError("Data pin does not exist (" + str(datpin) + ")")
    self.clkpin = clkpin
    self.datpin = datpin
  
  def send(self, data):
    if not (type(data) is byte):
      raise ValueError("Data is not of type 'byte'")
    for i in range(8):
      #set clkpin high
      #write current bit to data pin
      print("1" + str(data.bit(i)))
      #set clkpin low
      print("0")

      
newByte = byte(128)
newI2C = i2c(-1, 0)
newI2C.send(newByte)
