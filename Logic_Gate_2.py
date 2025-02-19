#from Compilation import *


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

#____________________________________________________________

class WIRE:
  exemplary = 1
  def __init__(self, name = None):
     self.id = "Wire" + str(WIRE.exemplary) # Iestata eksemplāram ID
     WIRE.exemplary += 1
     self.name = ""
     if isinstance(name, str) and (name is not None):
        self.name = name
        self.id = self.id + "_" + self.name
     self.status = False
     self.number = 0
     self.blocked = False
     self.ControlAdres = None
     self.time = 0
     self.corektTime = False
  def SetUp(self, value):
     self.status = value
  def Read(self):
     return self.status
  def Info(self, fulInfo = False):
     print("ID:     ", self.id)
     print("Status: ", str(self.status))
     print("Time:   ", str(self.time))
     print("")
#__________________________________________________________________________________________

class IO:
  exemplary = 1
  def __init__(self, name = None):
    self.id = "IO:" + str(IO.exemplary)
    IO.exemplary += 1
    self.name = ""
    if isinstance(name, str) and (name is not None):
        self.name = name
        self.id = self.id + "_" + self.name
    self.wireInt = None
    self.wireOut = None
    self.status = False
    self.key = ''
    self.number = 0
    self.blocked = False
  def setTime(self):
      if not (self.wireOut is None):
         self.wireOut.time += 1
  def StatusDebug(self):
       print("_______________________ ", self.id, " _________________________________")
       print("number:    ", self.number)
       print("blocked:   ", self.blocked, "\n")
  def setKey(self, key):
     self.key = key
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
            self.wireOut.time = -1
  def OFF(self):
      if self.wireInt is None:
        if self.status:
            self.status = False
            self.wireOut.SetUp(self.status)
            self.wireOut.time = -1
  def Run(self):
      if (self.wireOut is None) and (self.wireInt is not None):   # Ja pievienota tikai ieeja Kalpo kā IZEJA
          self.status = self.wireInt.status
      if (self.wireOut is not None) and (self.wireInt is not None):
         if self.wireInt.status != self.wireOut.status:
             self.wireOut.time = self.wireInt.time
             self.wireOut.corektTime = self.wireInt.corektTime
         self.wireOut.status = self.wireInt.status 

  def Read(self):
       return self.status
  def Info(self, fulInfo = False):
        print("___________________ ", self.id, "  Wire Ieejas izejas  ___________________________________")
        if self.wireInt is not None:
           print("wirw IN: ")
           self.wireInt.Info()
           print("")
        if self.wireOut is not None:
           print("wirw Out: ")
           self.wireOut.Info()
           print("")
        print("                      Ieksejais status")
        print("status: ", str(self.status))
 
#___________________________________________________________________________________________

class D_TRIGER:
   exemplary = 1
   def __init__(self, name = None):
      self.id = "D_T:" + str(D_TRIGER.exemplary)
      D_TRIGER.exemplary += 1 
      self.name = ""
      if isinstance(name, str) and (name is not None):
        self.name = name
        self.id = self.id + "_" + self.name
      self.status = False
      self.D = False
      self.C = False
      self.A = None
      self.B = None
      self.Q = None
      self._Q = None
      self.number = 0
      self.numberA = 0
      self.numberB = 0
      self.blockedA = False
      self.blockedB = False
      self.blocked = False
      self.exceptionBlockFlage = False
   def StatusDebug(self):
       print("_______________________ ", self.id, " _________________________________")
       print("number  A: ", self.numberA)
       print("blocked A: ", self.blockedA)
       print("number  B: ", self.numberB)
       print("blocked B: ", self.blockedB)
       if self.Q is not None:
          print("number  Q: ", self.Q.number)
          print("blocked Q: ", self.Q.blocked)
       if self._Q is not None:
          print("number  _Q: ", self._Q.number)
          print("blocked _Q: ", self._Q.blocked)
       print("number:    ", self.number)
       print("blocked:   ", self.blocked, "\n")
   def addWireD(self, obj):
      if isinstance(obj, WIRE):
         if self.A is None:
            self.A = (obj)
      else:
          raise Exception(bcolors.FAIL + "Objektam " + self.id + " Ieeja D Var pievienot tikai objektu Wire" + bcolors.ENDC)
   def addWireC(self, obj):
      if isinstance(obj, WIRE):
         if self.B is None:
            self.B = (obj)
      else:
          raise Exception(bcolors.FAIL + "Objektam " + self.id + "Ieeja C Var pievienot tikai objektu Wire" + bcolors.ENDC)
   def addWireQ(self, obj):
      if isinstance(obj, WIRE):
          if self.Q is None:
            self.Q = (obj)
            self.Q.status = False
      else:
          raise Exception(bcolors.FAIL + "Objektam " + self.id + "Ieeja Q Var pievienot tikai objektu Wire" + bcolors.ENDC)
   def addWire_Q(self, obj):
      if isinstance(obj, WIRE):
          if self._Q is None:
            self._Q = (obj)
            self._Q.status = True
      else:
          raise Exception(bcolors.FAIL + "Objektam " + self.id + "Ieeja _Q Var pievienot tikai objektu Wire" + bcolors.ENDC)
   def Info(self, fulInfo = False):
        
        print("___________________ ", self.id, " Wire Ieejas Izejas  ___________________________________")
        if self.A is not None:
           print("wire D: ")
           self.A.Info()
           print("")
        if self.B is not None:
           print("wire C: ")
           self.B.Info()
           print("")
        if self.Q is not None:
           print("wire Q: ")
           self.Q.Info()
           print("")
        if self._Q is not None:
           print("wire _Q: ")
           self._Q.Info()
           print("")
        print("                      Ieksejais status")
        print("status: ", str(self.status))
        print("D: ", str(self.D))
        print("C: ", str(self.C))
        print("")
   def setTime(self):
       if self.Q is not None:
          self.Q.time += 1
          self.Q.corektTime = False
       if self._Q is not None:
          self._Q.time += 1
          self._Q.corektTime = False
   def compilation(self):
       # 1 - jau blokets galvenais
       # 2 - tiko blokeju galveno
       # 0 - bez izmainam
       # 3 - ir izmainas
       status = 0                           # Glabās statusu ko sanāca izdarit skatities atsifrejumu
       if self.blocked:                     # Ja blocked ir True tad nekas nav jadara un atgriez 1
          return 1                          # tad nekas nav jadara un atgriez 1
       if not self.blockedA:                # Pārbauda vai paša izeja A ir bloķēta ja nav tad
          if self.A.blocked:                # Parbauda vai pievienotajs vads ir bloķēts ja jā
             self.numberA = self.A.number   # tad saglabā vada numuru sev ieejā A
             self.blockedA = True           # Un Nobloķē ieeju A
             status = 3                     # Un pasaka kad kautko jaunu izdarīja
       if not self.blockedB:                # Pārbauda vai paša izeja B ir bloķēta ja nav tad
          if self.B.blocked:                # Parbauda vai pievienotajs vads ir bloķēts ja jā
             self.numberB = self.B.number   # tad saglabā vada numuru sev ieejā B
             self.blockedB = True           # Un Nobloķē ieeju B
             status = 3                     # Un pasaka kad kautko jaunu izdarīja
       if self.blockedA and self.blockedB:  # Parbauda vai ieejas A gan B ja jā
          self.blocked = True               # Tad nobloķē galveno un
          if self.A.number > self.B.number: # Ja sevi nobloķēja un A ieejas numurs ir lielāks par B ieejas numuru
              self.number = self.A.number   # tad iestata savu numuru kāds ir A ieejai numurs   
          else:                             # ja nē tad
              self.number = self.B.number   # Numurs ir vienāds ar B ieejas numuru
          if self.Q is not None:
            self.Q.number = self.number + 1   # Iestata vada numuru
            self.Q.blocked = True             # Nobloķē izejas vadu
          if self._Q is not None:
            self._Q.number = self.number + 1   # Iestata vada numuru
            self._Q.blocked = True             # Nobloķē izejas vadu

          return 2                          # atgriež rezultātu kad tiko sanāca nobloķēt kaut ko
       return status
   def Run(self):
      
      if (self.B.status) and (self.C == False) and (self.B.time == 0) and ((self.A.time > 0) or (self.A.corektTime)):
      #if (self.B.status) and (self.C == False) and (self.B.time == 0) and ( ((self.A.time > 0) and (self.A.number < 3)) or ((self.A.time >= 0) and (self.A.number > 2))):
         self.status = self.D
         if self.Q.status != self.status:
            if self.Q is not None:
                self.Q.time = 0
                self.Q.corektTime = True
            if self._Q is not None:
                self._Q.time = 0    
                self._Q.corektTime = True
         if self.Q is not None:       
            self.Q.status = self.status
         if self._Q is not None:
            self._Q.status = not self.Q.status
      self.D = self.A.status
      self.C = self.B.status

#__________________________________________________________________________________________

class Gates:
    exemplary = 1
    def __init__(self):
        self.status = False
        name = None
        self.name = ""
        # if isinstance(name, str) and (name is not None):
        #     self.name = name
        #     self.id = self.id + "_" + self.name
        self.A = None
        self.B = None
        self.O = None
        self.number = 0
        self.numberA = 0
        self.numberB = 0
        self.blockedA = False
        self.blockedB = False
        self.blocked = False
        self.exceptionBlockFlage = False
    def StatusDebug(self):
       print("_______________________ ", self.id, " _________________________________")
       print("number  A: ", self.numberA)
       print("blocked A: ", self.blockedA)
       print("number  B: ", self.numberB)
       print("blocked B: ", self.blockedB)
       print("number  O: ", self.O.number)
       print("blocked O: ", self.O.blocked)
       print("number:    ", self.number)
       print("blocked:   ", self.blocked, "\n")
    def setTime(self):
       self.O.time += 1
       self.O.corektTime = False   
    def compilation(self):
       # 1 - jau blokets galvenais
       # 2 - tiko blokeju galveno
       # 0 - bez izmainam
       # 3 - ir izmainas
       status = 0                           # Glabās statusu ko sanāca izdarit skatities atsifrejumu
       if self.blocked:                     # Ja blocked ir True tad nekas nav jadara un atgriez 1
          return 1                          # tad nekas nav jadara un atgriez 1
       if not self.blockedA:                # Pārbauda vai paša izeja A ir bloķēta ja nav tad
          if self.A.blocked:                # Parbauda vai pievienotajs vads ir bloķēts ja jā
             self.numberA = self.A.number   # tad saglabā vada numuru sev ieejā A
             self.blockedA = True           # Un Nobloķē ieeju A
             status = 3                     # Un pasaka kad kautko jaunu izdarīja
       if not self.blockedB:                # Pārbauda vai paša izeja B ir bloķēta ja nav tad
          if self.B.blocked:                # Parbauda vai pievienotajs vads ir bloķēts ja jā
             self.numberB = self.B.number   # tad saglabā vada numuru sev ieejā B
             self.blockedB = True           # Un Nobloķē ieeju B
             status = 3                     # Un pasaka kad kautko jaunu izdarīja
       if self.blockedA and self.blockedB:  # Parbauda vai ieejas A gan B ja jā
          self.blocked = True               # Tad nobloķē galveno un
          if self.A.number > self.B.number: # Ja sevi nobloķēja un A ieejas numurs ir lielāks par B ieejas numuru
              self.number = self.A.number   # tad iestata savu numuru kāds ir A ieejai numurs   
          else:                             # ja nē tad
              self.number = self.B.number   # Numurs ir vienāds ar B ieejas numuru
          self.O.number = self.number + 1   # Iestata vada numuru
          self.O.blocked = True             # Nobloķē izejas vadu

          return 2                          # atgriež rezultātu kad tiko sanāca nobloķēt kaut ko
       return status
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
    def Info(self, fulInfo = False):
        print("___________________ ", self.id, " Wire Ieejas Izejas  ___________________________________")
        if self.A is not None:
           print("wire A: ")
           self.A.Info()
           print("")
        if self.B is not None:
           print("wire B: ")
           self.B.Info()
           print("")
        if self.O is not None:
           print("wire O: ")
           self.O.Info()
           print("")
        print("                      Ieksejais status")
        print("status: ", str(self.status))
        print("")
#__________________________________________________________________________________________

class XOR(Gates):
    def __init__(self, name = None):
      super().__init__()
      self.id = "xor:" + str(XOR.exemplary)
      XOR.exemplary += 1
      if isinstance(name, str) and (name is not None):
        self.name = name
        self.id = self.id + "_" + self.name
    def Run(self):
      self.status = self.A.status ^ self.B.status
      if self.status != self.O.status:
         self.O.time = 0
         self.O.corektTime = True
      self.O.status = self.status

#__________________________________________________________________________________________

class OR(Gates):
    def __init__(self, name = None):
      super().__init__()
      self.id = "or:" + str(OR.exemplary)
      OR.exemplary += 1
      if isinstance(name, str) and (name is not None):
        self.name = name
        self.id = self.id + "_" + self.name
    def Run(self):
       self.status = self.A.status or self.B.status
       if self.status != self.O.status:
          self.O.time = 0
          self.O.corektTime = True
       self.O.status = self.status
                       
#___________________________________________________________________________________________________________

class AND(Gates):
    def __init__(self, name = None):
      super().__init__()
      self.id = "and:" + str(AND.exemplary)
      AND.exemplary += 1
      if isinstance(name, str) and (name is not None):
            self.name = name
            self.id = self.id + "_" + self.name
    def Run(self):
        self.status = self.A.status and self.B.status
        if self.status != self.O.status:
           self.O.time = 0
           self.O.corektTime = True
        self.O.status = self.status

#___________________________________________________________________________________________________________

class NAND(Gates):
    def __init__(self, name = None):
      super().__init__()
      self.id = "nand:" + str(NAND.exemplary)
      NAND.exemplary += 1
      if isinstance(name, str) and (name is not None):
        self.name = name
        self.id = self.id + "_" + self.name
    def Run(self):
        self.status = not (self.A.status and self.B.status)
        if self.status != self.O.status:
           self.O.time = 0
           self.O.corektTime = True
        self.O.status = self.status
#___________________________________________________________________________________________________________

class NOT:
    exemplary = 1
    def __init__(self, name = None):
      self.id = "not:" + str(NOT.exemplary)
      NOT.exemplary += 1
      self.name = ""
      if isinstance(name, str) and (name is not None):
          self.name = name
          self.id = self.id + "_" + self.name
      self.status = False
      self.A = None
      self.O = None
      self.number = 0
      self.numberA = 0
      self.blockedA = False
      self.blocked = False
    def StatusDebug(self):
       print("_______________________ ", self.id, " _________________________________")
       print("number  A: ", self.numberA)
       print("blocked A: ", self.blockedA)
       print("number  O: ", self.O.number)
       print("blocked O: ", self.O.blocked)
       print("number:    ", self.number)
       print("blocked:   ", self.blocked, "\n")
    def compilation(self):
       # 1 - jau blokets galvenais
       # 2 - tiko blokeju galveno
       # 0 - bez izmainam
       # 3 - ir izmainas
       status = 0                           # Glabās statusu ko sanāca izdarit skatities atsifrejumu
       if self.blocked:                     # Ja blocked ir True tad nekas nav jadara un atgriez 1
          return 1                          # tad nekas nav jadara un atgriez 1
       if not self.blockedA:                # Pārbauda vai paša izeja A ir bloķēta ja nav tad
          if self.A.blocked:                # Parbauda vai pievienotajs vads ir bloķēts ja jā
             self.numberA = self.A.number   # tad saglabā vada numuru sev ieejā A
             self.blockedA = True           # Un Nobloķē ieeju A
             status = 3                     # Un pasaka kad kautko jaunu izdarīja
       if self.blockedA:                    # Parbauda vai ieejas A ir bloķēta
          self.blocked = True               # Tad nobloķē galveno un
          self.number = self.A.number       # Ja sevi nobloķēja tad iestata savu numuru
          self.O.number = self.number + 1   # Iestata vada numuru
          self.O.blocked = True             # Nobloķē izejas vadu
          return 2                          # atgriež rezultātu kad tiko sanāca nobloķēt kaut ko
       return status
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
    def setTime(self):
       self.O.time += 1
    def Run(self):
        self.status = (not self.A.status)
        if self.status != self.O.status:
          self.O.time = 0
          self.O.corektTime = True
        self.O.status = self.status
    def Info(self, fulInfo = False):
       def Info(self, fulInfo = False):
        print("___________________ ", self.id, " Wire Ieejas Izejas  ___________________________________")
        if self.A is not None:
           print("wire A: ")
           self.A.Info()
           print("")
        if self.O is not None:
           print("wire O: ")
           self.O.Info()
           print("")
        print("                      Ieksejais status")
        print("status: ", str(self.status))
        print("")
  #_________________________________________________________________


class Circuit:
  exemplary = 1
  def __init__(self, name = None):
    self.testcounter = 1
    self.id = "Circuit" + str(Circuit.exemplary)
    Circuit.exemplary += 1
    self.name = ""
    if isinstance(name, str) and (name is not None):
         self.name = name
    self.iinputs = []
    self.ioutputs = []
    self.gates = []
    self.element = []
    self.wire = []
  #def addToFile(self, data):
     
  def Info(self, fin, fele, fout):
     if fin:
        for c in self.iinputs:
            c.Info()
     if fele:
        for c in self.element:
            c.Info()
     if fout:
        for c in self.ioutputs:
            c.Info()
  def StatusDebug(self):
      for c in self.iinputs:
         c.StatusDebug()
      for c in self.gates:
         c.StatusDebug()
      for c in self.ioutputs:
          c.StatusDebug()
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
     if isinstance(obj, OR) or isinstance(obj, AND) or isinstance(obj, NAND) or isinstance(obj, XOR) or isinstance(obj, NOT) or isinstance(obj, D_TRIGER):
        self.gates.append(obj)
     else:
       raise Exception(bcolors.FAIL + "Pievienot var tikai obj Logic Gates" + bcolors.ENDC) 
  def PrintOutput(self):
     for c in range(len(self.ioutputs)):
        print(str(self.ioutputs[c].id) + " status: " + str(self.ioutputs[c].status))   
     print("____________________________________________________")
  def toCompile(self, cik = 300):
     prevProgress = 0
     nowProgress = 0
     blockedCounter = 0
     counter = 0
     trayCounter = 0
     for c in self.iinputs:
        c.number = 1
        c.blocked = True
        c.wireOut.number = c.number + 1
        c.wireOut.blocked = True
     status = 0
     while not (blockedCounter == (len(self.gates))): # and (not ((counter > cik))):
        for c in self.gates:
          status = c.compilation()  
          # if c.id == "D_T:5":
          #    c.Info()
          if status == 2:
             nowProgress += 1
             blockedCounter += 1
             #print(blockedCounter)
             status = 0
        if nowProgress == prevProgress:                             # šis bloks ir ja nesanaca neko izdarit pa ciklu tad
           trayCounter += 1                                         # Mei'gin'ajumu sakits pieau par viens
        else:
           prevProgress = nowProgress
        if trayCounter == 1:                                        # Ja piecas reizes nekas nesanāca tad meiģinās vienam pieškirt pagaidu vērtību
           potObj = []
           for c in self.gates:                                     # Meklēs objektus par kuriem tālāk netiek un saglabās potObj
             if not isinstance(c, NOT):                             # Ja tas objekts nav NOT tad parbauda
                if not(c.blocked) and (c.blockedA or c.blockedB):   # vai nav objekts nobloķēts un vai vismaz viena izeja ir bloķēta
                   potObj.append(c)                                 # ja jā tad objektu pievieno pie saraksta kur ir pie kuriem iestrēga
           maxValue = 0                                             # Šeit glabāsies lielākais skaitlis
           objPot = None                                            # Bet te kuram objektam tas skaitlis ir
           for b in potObj:                                         # Ciklā meklēs potencjālajiem objektiem kuram ir vis lielākā                                      
              if b.numberA > maxValue:                              # Ieelas vērtība
                 objPot = b
                 maxValue = b.numberA
              if b.numberB > maxValue:
                 objPot = b
                 maxValue = b.numberB
           if objPot.numberA == 0:                                  # Ja neiestatītā vērtība bus ieeja A tad 
              objPot.numberA = objPot.numberB                       # A ieejas vērtību pielīdzinās ar ieejas B vērtību
              objPot.blockedA = True                                 # Nobloķēs ieeju A lai nebūtu pretrunā ar nākamo galvenā while cikla iterācīju
              objPot.number = objPot.numberB                        # Paš vērtību iestatīs
           if objPot.numberB == 0:                                  # Vis analoģiski kas ar ieeju A aprakstītu augstāk
              objPot.numberB = objPot.numberA
              objPot.blockedB = True
              objPot.number = objPot.numberA
          #  else:
          #     objPot.numberB = objPot.numberA
           objPot.blocked = True                                 # Pašu vērtību nobloķēs lai nerastos pretruna kas aprakstīta nedaudz augs'tāk
           blockedCounter += 1
           #print(blockedCounter)
           val = objPot.number
           val += 1
           objPot.O.number = val                               # Izejas vada vērtību iestata
           objPot.O.blocked = True                               # Un izejas vadu nobloķē
           nowProgress += 1                                      # Pasaka kad jaunu objektu atrada   
           trayCounter = 0
                                  
        counter += 1
               
     for c in self.ioutputs:
        c.number = c.wireInt.number

#______________________________________________________________________-

     length = len(self.gates)
     cnt = 0
     while len(self.element) < length:
        for c in self.gates:
           if c.number == cnt:
              self.element.append(c)
        cnt += 1
  def printElement(self):
     for c in self.element:
        print(c.id)
  def Run(self, value = 0):
     for c in self.iinputs:
        c.setTime()
     for c in self.element:
        c.setTime()
     for c in self.ioutputs:
        c.setTime()
     for c in self.iinputs:
        c.Run()
     for c in self.element:
        c.Run()
     for c in self.ioutputs:
        c.Run()