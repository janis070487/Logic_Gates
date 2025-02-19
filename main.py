from logicGate import *
import time  
#from logicGate import Gates
"""
________________________________________________________________________________ 


  L1          L2           L3.1     L3      L3.2        L4          L5
  _______   _______       ________________________    _______     _______
_| IO 1 |___| W1   |______| IO A |__(A)(O)_| IO O |___| W3   |____| IO Q |__
 |______|   |______|      |______|         |______|   |______|    |______| 
                          |              VCC = 0  | 
  _______   ______        |______        Wait = 0 | 
_| IO 2 |___| W2  |_______| IO B |__(B) Status = 0| 
 |______|   |_____|       |______|________________|

 ______________________        ____________________
 | IO input | I0 Outpu |       |  WIR              | 
 |__________|__________|       |  Status = 0       | 
 |  W xx    | W xx     |       |  Time Aktual = 0  |
 |      Name           |       |                   |
 |__________|__________|       |___________________|

 _________________________________________________________________________________|
           Circuit shēma
1. Shēma sastāv no trīju veidu elementiem
   Ports IO, Wire, un loģiskā elementa. 
2. Projekts var sastāvēt no daudzām shēmām "Circuit". Bet katrai shēmai jābūt Gan ieejas un izejas portam, portiem.
           
           IO
   IO objekti izmantoti kā shēmas ieejās un izejās kā arī elementu ieejām un izejām.
   Shēmai tie ir jaizveido atsevišķi, bet elementiem tie tiek izveidoti automātiski konstruktorā.
          Objekta parametri
      IO input  satur WIRE  objektu kas kalpo ieejas signāla pieņemšanā,  
      IO output satur WIRE  objektu kas kalpo izejas signāla nodošanā tālāk
          
          Objekta metodes
      addWireInt(obj) Pievieno vadu pie ieejas
      addWireOut(obj) Pievieno vadu pie izejas
      RUN() nolasa signālu no ieejas un ja tas ir izmainījies tad tad izejas vadam palaiž metodi SetUp(status) kas vada statusu iestata
          un nomet TimeAktual uz 0. Bet ja signāls nemainās tad palaiž metodi Run() Kas vadam palielina TimeAktual par viens   

        WIRE
   Objekts WIRE savieno IO interveisus kas nodod signālus starp tiem
        Objektu parameti
      status - satur divus iespējamos stāvokļus True vai False WIRE statusu var izmainīt tikai IO izeja, un kad IO maina statusu uz pretējo tad
        nomet otru parametru.
      TimeActualSignal - kurš norāda cik laiks pagājis kopš signāls ir nomainījies   
"""


# ioA = IO()
# ioB = IO()
# ioO = IO()

# and1 = AND()
# not1 = NOT()

# w1 = WIRE()
# w2 = WIRE()
# w3 = WIRE()
# w4 = WIRE()

# ioA.addWireOut(w1)
# ioB.addWireOut(w2)
# ioO.addWireInt(w4)
# and1.addWireA(w1)
# and1.addWireB(w2)
# and1.addWireO(w3)
# not1.addWireA(w3)
# not1.addWireO(w4)

# and1.VCC(1)
# not1.VCC(1)

# c = Circuit()
# c.addIOinput(ioA)
# c.addIOinput(ioB)
# c.addLogicGates(and1)
# c.addLogicGates(not1)
# c.addIOoutputs(ioO)

# tic = 100

# c.Run(tic)
# ioA.ON()
# c.Run(tic)
# ioB.ON()
# c.Run(tic)


# print(ioO.Info())


#____________________________________________________________________________________
#____________________________________________________________________________________



tic = 250

iod = IO()
ioc = IO()
ioQ = IO()
io_Q = IO()

# iod.setKey('d')
# ioc.setKey('c')

and1 = AND()
and2 = AND()
and3 = AND()
and4 = AND()
not1 = NOT()
not2 = NOT()
not3 = NOT()
not4 = NOT()


# and1.delay = 5
# and2.delay = 5
# and3.delay = 6  #6
# and4.delay = 6  #6
# not1.delay  = 5
# not2.delay = 5
# not3.delay = 5
# not4.delay = 6

w1 = WIRE()
w2 = WIRE()
w3 = WIRE()
w4 = WIRE()
w5 = WIRE()
w6 = WIRE()
w7 = WIRE()
w8 = WIRE()
w9 = WIRE()
w10 = WIRE()

iod.addWireOut(w1)
ioc.addWireOut(w2)
ioQ.addWireInt(w9)
io_Q.addWireInt(w10)

and1.addWireA(w1)
and1.addWireB(w2)
and1.addWireO(w3)

and2.addWireA(w5)
and2.addWireB(w2)
and2.addWireO(w4)

and3.addWireA(w5)
and3.addWireB(w10)
and3.addWireO(w7)

and4.addWireA(w9)
and4.addWireB(w6)
and4.addWireO(w8)

not1.addWireA(w3)
not1.addWireO(w5)

not2.addWireA(w4)
not2.addWireO(w6)

not3.addWireA(w7)
not3.addWireO(w9)

not4.addWireA(w8)
not4.addWireO(w10)

and1.VCC(1)
and2.VCC(1)
and3.VCC(1)
and4.VCC(1)
not1.VCC(1)
not2.VCC(1)
not3.VCC(1)
not4.VCC(1)
#start_time = time.time()


cir = Circuit()

cir.addIOinput(iod)
cir.addIOinput(ioc)
cir.addLogicGates(and1)
cir.addLogicGates(and2)
cir.addLogicGates(not1)
cir.addLogicGates(not2)
cir.addLogicGates(and3)
cir.addLogicGates(and4)
cir.addLogicGates(not3)
cir.addLogicGates(not4)
cir.addIOoutputs(ioQ)
cir.addIOoutputs(io_Q)

#cir.KeyControl = True

ci = []

ci.append(iod)
ci.append(ioc)
ci.append(and1)
ci.append(not1)
ci.append(and2)
ci.append(not2)
ci.append(and3)
ci.append(not3)
ci.append(ioQ)
ci.append(and4)
ci.append(not4)
ci.append(io_Q)

for c in ci:
  c.Run()

print(str(ioQ.status))

print(str(io_Q.status))

#iod.ON()
#cir.Run(tic)
#ioc.ON()
#cir.Run(tic)

#_____________________
#ioc.OFF()
#cir.Run(tic)
#_____________________
# iod.OFF()
# cir.Run(tic)
# iod.ON()
# cir.Run(tic)
# iod.OFF()
# cir.Run(tic)



# print(ioQ.Info())
# print(io_Q.Info())


#end_time = time.time()


# execution_time = end_time - start_time  # Laika aprēķināšana  
# print(f'Koda izpildes laiks: {execution_time:.6f} sekunžu')  


#____________________________________________________________________________________
#____________________________________________________________________________________


# ia = IO()
# ib = IO()
# io = IO()

# g = OR()
# w1 = WIRE()
# w2 = WIRE()
# w3 = WIRE()

# ia.addWireOut(w1)
# ib.addWireOut(w2)
# io.addWireInt(w3)
# g.addWireA(w1)
# g.addWireB(w2)
# g.addWireO(w3)

# g.VCC(1)

# for c in range(4):
#   ia.Run()
#   ib.Run()
#   g.Run()
#   io.Run()

# ib.on_off()  # 0 1

# for c in range(2):
#   ia.Run()
#   ib.Run()
#   g.Run()
#   io.Run()
  
# ib.on_off()   # 0 0

# for c in range(4):
#   ia.Run()
#   ib.Run()
#   g.Run()
#   io.Run()

# ib.on_off()   # 0 1
# ia.on_off()   # 1 1

# for c in range(2):
#   ia.Run()
#   ib.Run()
#   g.Run()
#   io.Run()

# ib.on_off()   # 1 0

# for c in range(1):
#   ia.Run()
#   ib.Run()
#   g.Run()
#   io.Run()

# ia.on_off()   # 0 0

# for c in range(4):
#   ia.Run()
#   ib.Run()
#   g.Run()
#   io.Run()

#print(g.info())







