from ti_hub import *

class byte:
  bits = [0,0,0,0,0,0,0,0]
  __init__(self, val):
    for i in range(8):
      if (val >= 2 ** (7 - i)):
        val = val - (2 ** (7 - i))
        self.bits[i] = 1
      else:
        self.bits[i] = 0
      

