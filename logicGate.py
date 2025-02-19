import random
import keyboard  

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#___________________________________________________________________________________________

class IO:
  exemplary = 0
  def __init__(self):
    self.id = "IO:" + str(IO.exemplary)
    IO.exemplary += 1
    self.wireInt = None
    self.wireOut = None
    self.status = False
    self.key = ''
  def setKey(self, key):
     self.key = key
  def Reset(self):
    self.status = False
    if not self.wireInt is None:
       self.wireInt.status = False  
    if not self.wireOut is None:
       self.wireOut.status = False 
  def addWireInt(self, obj):    # Pievieno vadu kurš ieiet no loģdiskajā elementā vai nak no interfeiz
      if not self.wireInt is None:
        raise Exception(bcolors.FAIL + "Pie Input var pievienot tikai vienu obj WIRE" + bcolors.ENDC)
      if isinstance(obj, WIRE):
        self.wireInt = obj
      else:
        raise Exception(bcolors.FAIL + "War pievienot tikai objektu WIRE" + bcolors.ENDC)
  def addWireOut(self, obj):    # Pievieno vadu kurš ieiet loģdiskajā elementā vai IO ieeja
      if not self.wireOut is None:
        raise Exception(bcolors.FAIL + "Pie Input var pievienot tikai vienu obj WIRE" + bcolors.ENDC)
      if isinstance(obj, WIRE):
        self.wireOut = obj
      else:
        raise Exception(bcolors.FAIL + "War pievienot tikai vienu objektu WIRE" + bcolors.ENDC)
  def on_off(self):                   # savu statusu maina uz pretējo tikai tad ja nav pievienots ieejas vads
      if self.wireInt is None:
         self.status = not self.status
         self.wireOut.SetUp(self.status)
  def SetUp(self, value):
       if self.wireInt is None:
         if not value == self.status:
           self.status = not self.status
           self.wireOut.SetUp(self.status)
  def ON(self):
      if self.wireInt is None:
        if self.status == False:
            self.status = True
            self.wireOut.SetUp(self.status)
  def OFF(self):
      if self.wireInt is None:
        if self.status:
            self.status = False
            self.wireOut.SetUp(self.status)
  def Run(self):
       if self.wireOut is None and (not self.wireInt is None):   # Ja pievienota tikai ieeja Kalpo kā IZEJA
          self.status = self.wireInt.status
          #a = self.status
       elif self.wireInt is None and (not self.wireOut is None): # Ja pievienota tikai izeja kalpo kā IEEJA
          self.wireOut.SetUp(self.status)
       else:
          self.wireOut.SetUp(self.wireInt.status)                # Ja pievienoti abi kalpo kā       CAUR
  def Read(self):
       return self.status
  def Info(self, fulInfo = False):
      result = ""
      if fulInfo:
        result = result + str(self)
      result = result + "\nid: " + self.id + "\nstatus:\t" + str(self.status)
      if not self.wireInt is None:
        result = result + "\nWire int: " + self.wireInt.Info(fulInfo)
      if not self.wireOut is None:
        result = result + "\nWire out: " + self.wireOut.Info(fulInfo) + "\n"
      return result
#___________________________________________________________________________________________

class WIRE:
  exemplary = 0
  def __init__(self):
     self.id = "Wire" + str(WIRE.exemplary) # Iestata eksemplāram ID
     WIRE.exemplary += 1                    #
     self.status = False
     self.time = 0
  def SetUp(self, value):
     self.status = value
  def Read(self):
     return self.status
  def Info(self, fulInfo = False):
     result = ""
     if fulInfo:
        result = result + str(self)
     result = result + "\nid: " + self.id + "\nstatus:\t" + str(self.status)
     result = result + "\nTime: " + str(self.time)
     return result

#__________________________________________________________________________________________


class Gates:
    exemplary = 0
    def __init__(self):
      self.delay = random.randint(5, 25)
      self.delay = 5
      #self.actualSignalTime = 0
      self.status = False
      self.wait = False
      self.vcc = False
      self.A = None
      self.B = None
      self.O = None
      self.first = False
    def addWireA(self, obj):
     if isinstance(obj, WIRE):
         if self.A is None:
           self.A = (obj)
     else:
        raise Exception(bcolors.FAIL + "Objektam " + self.id + " Ieeja A Var pievienot tikai objektu Wire" + bcolors.ENDC)
    def addWireB(self, obj):
     if isinstance(obj, WIRE):
         if self.B is None:
           self.B = (obj)
     else:
        raise Exception(bcolors.FAIL + "Objektam " + self.id + "Ieeja B Var pievienot tikai objektu Wire" + bcolors.ENDC)
    def addWireO(self, obj):
     if isinstance(obj, WIRE):
         if self.O is None:
           self.O = (obj)
     else:
        raise Exception(bcolors.FAIL + "Objektam " + self.id + "Ieeja O Var pievienot tikai objektu Wire" + bcolors.ENDC)
    def VCC(self, status):
      if status:
        self.first = True
        self.vcc = True
        self.wait = True
        self.actualSignalTime = 0
      else:
        self.first = False
        self.vcc = False
        self.wait = False
        self.actualSignalTime = 0
        self.status = False
    def Reset(self):
        self.delay = random.randint(5, 25)
        #self.delay = 5
        self.actualSignalTime = 0
        self.status = False
        self.wait = False
        self.vcc = True
        self.first = True
        if not self.A is None:
          self.A.status = False  
        if not self.B is None:
          self.B.status = False
        if not self.O is None:
          self.O.status = False
    def info(self, fulInfo = False):
      result = "___________________________ start __________________________\n"
      if fulInfo:
        result = result + str(self)
      result = result + "ID: " + str(self.id) + "\n" + "wait: " + str(self.wait) + "\n"
      result = result + "VCC: " + str(self.vcc) + "\n" + "delay: " + str(self.delay) + "\n"
      result = result + "actualSignalTime: " + str(self.actualSignalTime) + "\n" + "status: " + str(self.status)
      if not self.A is None:
        result = result + "\nIO input A: " + self.A.Info(fulInfo) + "\n"
      if not self.B is None:
        result = result + "\nIO input B: " + self.B.Info(fulInfo) + "\n"
      if not self.O is None:
        result = result + "\nIO output O: " + self.O.Info(fulInfo) + "\n"
      result = result + "____________________________ end ___________________________\n"

      return result

#__________________________________________________________________________________________

class XOR(Gates):
    def __init__(self):
      super().__init__()
      self.id = "xor:" + str(XOR.exemplary)
      XOR.exemplary += 1
    def Run(self):
      if self.vcc:
          if self.wait:
              if ((self.A.status ^ self.B.status) != self.status) or self.first:
                  if self.actualSignalTime >= self.delay:
                      self.status = self.A.status ^ self.B.status
                      self.O.status = self.status
                      self.actualSignalTime = 0
                      self.wait = False
                      self.first = False
                  else:
                      self.actualSignalTime += 1
              else:
                  if self.actualSignalTime <= 0:
                      self.wait = True
                      self.actualSignalTime = 0
                  else:
                      self.actualSignalTime -= 1
          else:
              if ((self.A.status ^ self.B.status) != self.status):
                  self.wait = True
                  self.actualSignalTime += 1

#__________________________________________________________________________________________


class OR(Gates):
    def __init__(self):
      super().__init__()
      self.id = "or:" + str(OR.exemplary)
      OR.exemplary += 1
    def Run(self):
      if self.vcc:
          if self.wait:
              if ((self.A.status or self.B.status) != self.status) or self.first:
                    if self.actualSignalTime >= self.delay:
                        self.status = self.A.status or self.B.status
                        self.O.status = self.status
                        self.actualSignalTime = 0
                        self.wait = False
                        self.first = False
                    else:
                        self.actualSignalTime += 1
              else:
                    if self.actualSignalTime <= 0:
                        self.wait = True
                        self.actualSignalTime = 0
                    else:
                        self.actualSignalTime -= 1
          else:
              if ((self.A.status or self.B.status) != self.status):
                  self.wait = True
                  self.actualSignalTime += 1

#___________________________________________________________________________________________________________

class AND(Gates):
    def __init__(self):
      super().__init__()
      self.id = "and:" + str(AND.exemplary)
      AND.exemplary += 1
    def Run(self):
      if self.vcc:
        if self.wait:
            if ((self.A.status and self.B.status) != self.status) or self.first:
                  if self.actualSignalTime >= self.delay:
                      self.status = self.A.status and self.B.status
                      self.O.status = self.status
                      self.actualSignalTime = 0
                      self.wait = False
                      self.first = False
                  else:
                      self.actualSignalTime += 1
            else:
                  if self.actualSignalTime <= 0:
                      self.wait = True
                      self.actualSignalTime = 0
                  else:
                      self.actualSignalTime -= 1
        else:
            if ((self.A.status and self.B.status) != self.status):
                  self.wait = True
                  self.actualSignalTime += 1


#___________________________________________________________________________________________________________

class NAND(Gates):
    def __init__(self):
      super().__init__()
      self.id = "nand:" + str(NAND.exemplary)
      NAND.exemplary += 1
    def Run(self):
      if self.vcc:
          if self.wait:
              if (not(self.A.status and self.B.status) != self.status) or self.first:
                  if self.actualSignalTime >= self.delay:
                      self.status = not (self.A.status and self.B.status)
                      self.O.status = self.status
                      self.actualSignalTime = 0
                      self.wait = False
                      self.first = False
                  else:
                      self.actualSignalTime += 1
              else:
                  if self.actualSignalTime <= 0:
                      self.wait = True
                      self.actualSignalTime = 0
                  else:
                      self.actualSignalTime -= 1
          else:
              if (not (self.A.status and self.B.status) != self.status):
                  self.wait = True
                  self.actualSignalTime += 1

#___________________________________________________________________________________________________________

class NOT:
    exemplary = 0
    def __init__(self):
      self.id = "not:" + str(NOT.exemplary)
      NOT.exemplary += 1
      self.delay = random.randint(5, 25)
      #self.delay = 5
      self.actualSignalTime = 0
      self.status = False
      self.wait = False
      self.vcc = False
      self.A = None
      self.O = None
      self.first = False
    def addWireA(self, obj):
     if isinstance(obj, WIRE):
         if self.A is None:
           self.A = (obj)
     else:
        raise Exception(bcolors.FAIL + "Objektam " + self.id + " Ieeja A Var pievienot tikai objektu Wire" + bcolors.ENDC)
    def addWireO(self, obj):
     if isinstance(obj, WIRE):
         if self.O is None:
           self.O = (obj)
     else:
        raise Exception(bcolors.FAIL + "Objektam " + self.id + "Ieeja O Var pievienot tikai objektu Wire" + bcolors.ENDC)
    def VCC(self, status):
      if status:
        self.first = True
        self.vcc = True
        self.wait = True
        self.actualSignalTime = 0
      else:
        self.first = False
        self.vcc = False
        self.wait = False
        self.actualSignalTime = 0
        self.status = False
    def Run(self):
      if self.vcc:     # ______________________________________________  1
          if self.wait:  # ____________________________________________  2
              if (self.A.status == self.status) or self.first: # ______  3
                    if self.actualSignalTime >= self.delay: # _________  4
                        self.status = not self.A.status
                        self.O.status = self.status
                        self.actualSignalTime = 0
                        self.wait = False
                        self.first = False
                    else:
                        self.actualSignalTime += 1
              else:
                  if self.actualSignalTime <= 0: # __________________  6
                      self.wait = True
                      self.actualSignalTime = 0
                  else:
                      self.actualSignalTime -= 1
          else:
              if (self.A.status == self.status): # _________________  5
                  self.wait = True
                  self.actualSignalTime += 1
    def Reset(self):
        self.delay = random.randint(5, 25)
        #self.delay = 5
        self.actualSignalTime = 0
        self.status = False
        self.wait = False
        self.vcc = True
        self.first = True
        if not self.A is None:
          self.A.status = False  
        if not self.O is None:
          self.O.status = False
    def info(self, fulInfo = False):
      result = "___________________________ start __________________________\n"
      if fulInfo:
        result = result + str(self)
      result = result + "ID: " + str(self.id) + "\n" + "wait: " + str(self.wait) + "\n"
      result = result + "VCC: " + str(self.vcc) + "\n" + "delay: " + str(self.delay) + "\n"
      result = result + "actualSignalTime: " + str(self.actualSignalTime) + "\n" + "status: " + str(self.status)
      if not self.A is None:
        result = result + "\nIO input A: " + self.A.Info(fulInfo) + "\n"
      if not self.O is None:
        result = result + "\nIO output O: " + self.O.Info(fulInfo) + "\n"
      result = result + "____________________________ end ___________________________\n"

      return result
    

#__________________________________________________________________________________________

class Circuit:
  exemplary = 0
  def __init__(self):
    self.testcounter = 1
    self.id = "Circuit" + str(Circuit.exemplary)
    Circuit.exemplary += 1
    self.KeyControl = False
    self.iinputs = []
    self.ioutputs = []
    self.gates = []
    self.stop = True
  def Reset(self):
     for c in self.iinputs:
        c.Reset()
     for c in self.ioutputs:
        c.Reset()
     for c in self.gates:
        c.Reset()
  def addIOinput(self, obj):
     if isinstance(obj, IO):
        self.iinputs.append(obj)
     else:
       raise Exception(bcolors.FAIL + "Pievienot pie izejas var tiksi objektu IO" + bcolors.ENDC) 
  def addIOoutputs(self, obj):
     if isinstance(obj, IO):
        self.ioutputs.append(obj)
     else:
       raise Exception(bcolors.FAIL + "Pievienot pie izejas var tiksi objektu IO" + bcolors.ENDC) 
  def addLogicGates(self, obj):
     if isinstance(obj, OR) or isinstance(obj, AND) or isinstance(obj, NAND) or isinstance(obj, XOR) or isinstance(obj, NOT):
        self.gates.append(obj)
     else:
       raise Exception(bcolors.FAIL + "Pievienot var tikai obj Logic Gates" + bcolors.ENDC) 
  
  def on_off(self, status):
      for c in self.gates:
        c.VCC(status)
  def PrintOutput(self):
     for c in range(len(self.ioutputs)):
        print(str(self.ioutputs[c].id) + " status: " + str(self.ioutputs[c].status))   
     print("____________________________________________________")
     
  def Run(self, value = 0):

    if self.KeyControl:
      keyboard.on_press(self.on_key_event) 

      while self.stop:
        for c in self.iinputs:
            c.Run()
        for c in self.gates:
            c.Run()
        for c in self.ioutputs:
            c.Run()

      keyboard.unhook_all() 

    else:
       #while self.stop:
      for i in range(value):
        for c in self.iinputs:
            c.Run()
        for c in self.gates:
            c.Run()
        for c in self.ioutputs:
            c.Run()

  def on_key_event(self, keyboard_event): 
        keyName = keyboard_event.name

        if keyName == 'backspace': 
            self.stop = False 
            #raise KeyboardInterrupt  # Izmantojam izņēmumu, lai izkļūtu no cikla  
        for c in range(len(self.iinputs)):
           if keyName == self.iinputs[c].key:
             self.iinputs[c].on_off()
             self.PrintOutput()







  def testSelf(self, inputs, outputs):
    print(bcolors.OKBLUE +"\t\tstart test " + str(self.testcounter) + "\n" + bcolors.ENDC) 
    for c in range(len(inputs)):
      if inputs[c]:
        self.iinputs[c].SetUp(inputs[c])
    for c in range(len(outputs)):
        resultstr = ""
        result = []
        self.run()
        for d in self.ioutputs:
           result.append(d.status)
        resultstr = resultstr + str(result) + "\t\t" + str(outputs[c])
        r = result == outputs[c]
        resultstr = resultstr + "\t\t" + str(r) + "\n"
        textColor = ""
        if r:
           textColor = bcolors.OKGREEN
        else:
           textColor = bcolors.FAIL
        print(textColor + resultstr + bcolors.ENDC)
    #print(bcolors.OKBLUE + "\tend test " + str(self.testcounter) + "\n" + bcolors.ENDC) 

    self.testcounter += 1

  def testSelfD(self, inputs, outputs):
    result = [len(inputs) + len(outputs)]
    for c in result:
       pass
    if len(inputs) == len(self.iinputs):
      for c in range(len(inputs[0])):
         pass
    else:
      raise Exception(bcolors.FAIL + "Datu tesu ieeju skaits neatbilst shēmas ieeju skaitam" + bcolors.ENDC)
       
#___________________________________________________________________________________________________________






# class IO_INPUT:
#   exemplary = 0
#   def __init__(self):
#      super().__init__()
#      self.id = "Iinput" + str(Ii.exemplary)
#      Ii.exemplary += 1
#      self.status = False
#   def addWire(self, obj):    # Pievieno vadu kurš ieiet loģdiskajā elementā vai IO ieeja
#      if isinstance(obj, WIRE):
#         self.wireOut = obj
#      else:
#         raise Exception(bcolors.FAIL + "War pievienot tikai objektu WIRE" + bcolors.ENDC)
#   def addWireInt(self, obj):    # Pievieno vadu kurš iznāk no
#      if isinstance(obj, WIRE):
#         self.wireInt = obj
#         #self.status = obj.status
#      else:
#         raise Exception(bcolors.FAIL + "War pievienot tikai objektu WIRE" + bcolors.ENDC)
#   def Set(self, value):
#      self.status = value
#   def on_off(self):
#      self.status = not self.status
#      for c in self.wire:
#         c.on_off()
#   def SetUp(self, value):
#      if not value == self.status:
#         self.status = not self.status
#         for c in self.wire:
#            c.SetUp(value)
#   def addWire(self, obj):
#      super().addWire(obj)
#      result = False
#      for c in self.wire:
#         result = result or self.status
#      self.status = result
#   def info(self, fulInfo = False):
#      result = ""
#      if fulInfo:
#         result = result + str(self)
#      result = result + "\nid: " + self.id + "\nstatus:\t" + str(self.status)
#      for c in self.wire:
#         c.info(fulInfo)
#         result = result + "\n      " + c.info(fulInfo) + "\n"
#      return result
  


           #c.on_off()
  # def run(self):
  #    for c in self.wire:
  #       c.status = self.status





# class GATES:
#   exemplary = 0
#   def __init__(self):
#     #self.TimeSignal = 0
#     self.delay = 3
#     self.wait = False
#     self.VCC = False
#     self.A = False
#     self.B = False
#     self.O = False
#   def addWireA(self, obj):
#     if isinstance(obj, WIRE):
#       self.WireA = obj
#       self.A = obj.status
#     else:
#        raise Exception(bcolors.FAIL + "Var pievienot objektu WIRE" + bcolors.ENDC)
#   def addWireB(self, obj):
#      if isinstance(obj, WIRE):
#         self.WireB = obj
#         self.B = obj.status
#      else:
#         raise Exception(bcolors.FAIL + "Var pievienot objektu WIRE" + bcolors.ENDC)
     
#   def ON_OFF(self, status):
#       if status:
#         self.VCC = True
#         self.wait = True
#         #self.WireO.status = self.O
#       else:
#         #self.O = False
#         self.VCC = False
#         elf.wait = False
#   def addWireO(self, obj):
#      if isinstance(obj, WIRE):
#         self.WireO = obj
#         self.WireO.status = self.O
#      else:
#         raise Exception(bcolors.FAIL + "Var pievienot objektu WIRE" + bcolors.ENDC)
               
     

# class OR (GATES):
#    def __init__(self):
#       super().__init__()
#       self.id = "or" + str(OR.exemplary)
#       OR.exemplary += 1
#    def Name(self, name):
#       self.name = name
#    def run(self):
#       if self.VCC:
#          self.A = self.WireA.status
#          self.B = self.WireB.status
#          if (self.WireA.timeActualSignal or self.WireB.timeActualSignal) < self.delay:     
#             self.wait = True
#          else:
#             if self.wait:
#                self.O = self.A or self.B
#                self.WireO.status = self.O
#                self.wait = False
# # Wire objektam stavokli var izmainīt tikai Loģiskā
# # elementa izeja kura pievienota vai pievienotais Ii interveis
# class WIRE:
#   exemplary = 0
#   def __init__(self):
#      self.id = "Wire" + str(WIRE.exemplary) # Iestata eksemplāram ID
#      WIRE.exemplary += 1                    # 
#      self.status = False
#      self.timeActualSignal = 0
#   def run(self):
#      self.timeActualSignal += 1
#   def on_off(self):                        #  Maaina stāvokli status WIRE uz pretējo un nomet laiku uz nulli
#      self.status = not self.status
#      self.timeActualSignal = 0
#   def SetUp(self, value):
#      if not value == self.status:
#         self.status = not self.status
#         self.timeActualSignal = 0


# class Interface:
#   exemplary = 0
#   def __init__(self):
#     self.wire = []
#     self.status = False
#   def addWire(self, obj):
#      if isinstance(obj, WIRE):
#         self.wire.append(obj)
#         self.status = obj.status
#      else:
#         raise Exception(bcolors.FAIL + "War pievienot tikai objektu WIRE" + bcolors.ENDC)


# class Ii (Interface):
#   def __init__(self):
#      super().__init__()
#      self.id = "Iinput" + str(Ii.exemplary)
#      Ii.exemplary += 1
#   def on_off(self):
#      for c in self.wire:
#         c.on_off()
#   def SetUp(self, value):
#      if not value == self.status:
#         for c in self.wire:
#            c.SetUp(value)
#            #c.on_off()
#   # def run(self):
#   #    for c in self.wire:
#   #       c.status = self.status
     


# class Io (Interface):
#   def __init__(self):
#      super().__init__()
#      self.id = "Ioutput" + str(Io.exemplary)
#      Io.exemplary += 1
#   def run(self):
#      value = False
#      for c in self.wire:
#         value = value or c.status
#      self.status = value

# class Circuit:
#   exemplary = 0
#   def __init__(self):
#     self.testcounter = 1
#     self.id = "Circuit" + str(Circuit.exemplary)
#     Circuit.exemplary += 1
#     self.iinputs = []
#     self.ioutputs = []
#     self.gates = []
#     self.wire = []
#   def addObj(self, obj):
#       if isinstance(obj, WIRE):
#         self.wire.append(obj)
#       elif isinstance(obj, Ii):
#         self.iinputs.append(obj)
#       elif isinstance(obj, Io):
#         self.ioutputs.append(obj)
#       elif isinstance(obj, OR):
#         self.gates.append(obj)
#       else:
#         raise Exception(bcolors.FAIL + "Pievienot var tikai obj WIRE, Ii, Io, NAND" + bcolors.ENDC)
#   def on_off(self, status):
#       for c in self.gates:
#         c.ON_OFF(status)
      
#   def run(self):
#     #  for c in self.iinputs:
#     #     c.run()
#      for c in self.wire:
#         c.run()
#      for c in self.gates:
#         c.run()
#      for c in self.ioutputs:
#         c.run()
#   # inputs 1 norada kad vajag mainīt konkrēto ieeju uz pretējo bet 0 nevaig mainit uz pretējo
#   # outputs ir masivs ar masiviem kādai rezultāti gaidāmi
#   def testSelf(self, inputs, outputs):
#     print(bcolors.OKBLUE +"\t\tstart test " + str(self.testcounter) + "\n" + bcolors.ENDC) 
#     for c in range(len(inputs)):
#       if inputs[c]:
#         #self.iinputs[c].on_off()
#         self.iinputs[c].SetUp(inputs[c])
#     for c in range(len(outputs)):
#         resultstr = ""
#         result = []
#         self.run()
#         for d in self.ioutputs:
#            result.append(d.status)
#         resultstr = resultstr + str(result) + "\t\t" + str(outputs[c])
#         r = result == outputs[c]
#         resultstr = resultstr + "\t\t" + str(r) + "\n"
#         textColor = ""
#         if r:
#            textColor = bcolors.OKGREEN
#         else:
#            textColor = bcolors.FAIL
#         print(textColor + resultstr + bcolors.ENDC)
#     #print(bcolors.OKBLUE + "\tend test " + str(self.testcounter) + "\n" + bcolors.ENDC) 

#     self.testcounter += 1

#   def testSelfD(self, inputs, outputs):
#     result = [len(inputs) + len(outputs)]
#     for c in result:
#        pass
#     if len(inputs) == len(self.iinputs):
#       for c in range(len(inputs[0])):
#          pass
#     else:
#       raise Exception(bcolors.FAIL + "Datu tesu ieeju skaits neatbilst shēmas ieeju skaitam" + bcolors.ENDC)
       