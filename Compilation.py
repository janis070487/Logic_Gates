from Logic_Gate_2 import *


class AllKeyWord:
    def __init__(self):
        self.keyWord = ['XOR', 'OR', 'AND', 'NAND', 'NOT', 'D_TRIGER']
    def add(self, data):
        for c in data[0]:
            self.keyWord.append(c.name)

#______________________________ Error ____________________________

class Error:
   def __init__(self):
      self.Mesage = []

#______________________________ CircuitData ________________________________________

class CircuitData:
   def __init__(self):
      self.name = None
      self.Input = None
      self.Output = None
      self.Elements = None
      self.Wire = None
      self.Test = None

#___________________________ Izdzēš komentārus _______________________________________

def DelComent(data):
    d = ""
    c1 = True
    counter = 0
    for c in data:
      if c == "/":
        if data[counter + 1] == "/":
            c1 = False
      if c == "\n":
         c1 = True
      if c1:
        d = d + c
      counter += 1
    return d

#_________________________ Izdzēšam simbolus __________________________________________

def DelChar(data, simbol):
    d = ""
    for c in data:
      if c != simbol:
          d = d + c
    return d

#____________________________ Formatē datus ___________________________________________

def FormatData(data):
   d = DelChar(data, ' ')
   e = DelComent(d)
   return DelChar(e, '\n')

#___________________________ Mekle sekciju ______________________________________________

def FindSektion(data, sektion_name, start, end, _error = 'Ignor'):
    value = ''
    count = data.find(sektion_name, start, end)
    if count == -1 and _error != 'Ignor':
       error = Error()
       error.Mesage.append(sms = 'section ' + _error + 'not found ' + sektion_name)
       return error
    count = count + len(sektion_name)
    while data[count] != '}':         # Meklē nosaukumu
        value = value + data[count]
        count += 1   
    return value   

#___________________________ Meklējam circuit ________________________________________


def FindCircuit(data):
    circuits = []
    main_position = data.find('Main')
    position = 0
    count = 0
    while position < main_position:
        position = data.find('Circuit', position, main_position)
        name = ''
        datasort = None
        datasort = CircuitData()
        if position == -1:
            break
        position += 7
        count = position
        while data[count] != '{':         # Meklē nosaukumu
           name = name + data[count]
           count += 1
        datasort.name = name
        #__________________ 'Inputs{' meklē _______________________________________
        datasort.Input = FindSektion(data, 'Inputs{', position, main_position, name)
        #__________________ 'Outputs{' meklē _______________________________________
        datasort.Output = FindSektion(data, 'Outputs{', position, main_position, name)
        #__________________ 'Elements{' meklē _______________________________________
        datasort.Elements = FindSektion(data, 'Elements{', position, main_position, name)
        #__________________ 'Wire{' meklē _______________________________________
        datasort.Wire = FindSektion(data, 'Wire{', position, main_position, name)

        circuits.append(datasort)
    return circuits

def FindMain(data):
   main_position = data.find('Main')
   if main_position == -1:
      error = Error()
      error.Mesage.append(sms = 'Not found section Main ')
      return error
   datasort = CircuitData()
   datasort.name = 'Main'
   #__________________ 'Inputs{' meklē _______________________________________
   datasort.Input = FindSektion(data, 'Inputs{', main_position, len(data), 'Main')
        #__________________ 'Outputs{' meklē _______________________________________
   datasort.Output = FindSektion(data, 'Outputs{', main_position, len(data), 'Main')
        #__________________ 'Elements{' meklē _______________________________________
   datasort.Elements = FindSektion(data, 'Elements{', main_position, len(data), 'Main')
        #__________________ 'Wire{' meklē _______________________________________
   datasort.Wire = FindSektion(data, 'Wire{', main_position, len(data), 'Main')
   #__________________ 'Test{' meklē _______________________________________
   datasort.Test = FindSektion(data, 'Test{', main_position, len(data), 'Ignor')

   return datasort



def Sorting(data):
   data_format = FormatData(data)
   data_ = []
   data_.append(FindCircuit(data_format))
   data_.append(FindMain(data_format))
   return data_

class Node:  
    def __init__(self, value):
        #self.name = None  
        self.value = value  
        self.children = []  

    def add_child(self, child_node):  
        self.children.append(child_node)  

    def __repr__(self):  
        #return f"Node({self.value})"  
        return self.value

class Tree:  
    def __init__(self, root_value):  
        self.root = Node(root_value)  

    def add_node(self, parent_value, child_value):  
        parent_node = self.find_node(self.root, parent_value)  
        if parent_node:  
            parent_node.add_child(Node(child_value))  

    def find_node(self, node, value):  
        if node.value == value:  
            return node  
        for child in node.children:  
            found_node = self.find_node(child, value)  
            if found_node:  
                return found_node  
        return None  

    def display(self, node=None, level=0):  
        if node is None:  
            node = self.root  
        print(" " * level * 4 + str(node.value))  
        for child in node.children:  
            self.display(child, level + 1)  


def Data_Tree(data):
    data_format = FormatData(data)
    circuit = FindCircuit(data_format)
    main = FindMain(data_format)
    dt = Tree('Main')
    keyWord = []
    dd = main.Elements.split(';')
    for c in dd:
        ff = c.split('=')
        dt.add_node('Main', ff[0])
        gg = ff[1].split(',')
        for v in range(len(gg)):
            dt.add_node(ff[0], gg[v])
    return dt
    #dt.root.name = 'Main'


class Data_Strukt:
    def __init__(self, data):
        self.sttuct = Tree('Main')











 


#______________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________


# class Connections:
#    def __init__(self, wire):
#       self.wire = wire
#       #self.ToNameDevace = None
#       #self.ToDevaceOutput = None
#       self.InDevace = []
#       self.InConection = []


# def delChar(data, simbol):
#    d = ""
#    for c in data:
#       if c != simbol:
#          d = d + c
#    return d

# def delComent(data):
#    d = ""
#    c1 = True
#    counter = 0
#    for c in data:
#       if c == "/":
#          if data[counter + 1] == "/":
#             c1 = False
#       if c == "\n":
#          c1 = True
#       if c1:
#         d = d + c
#       counter += 1
#    return d

# def GetBlock(data, block):
#   A = data.find(block)
#   B = data.find("{", A)
#   C = data.find("}", B)
#   result = data[B + 1: C]
#   return result

# def getElements(data, element):
#     obj_element = []
#     #obj_element.append
#     for c in data:
#        el = ''
#        cnt = 0
#        while (len(c) > 0) and (c[cnt] != '='):
#           el = el + c[cnt]
#           cnt += 1
#        cnt = 0
#        if el == element:
#           if el == "AND":
#                dat = c.find('=')
#                dat1 = c[dat + 1:]
#                dat2 = dat1.split(',')
#                for b in dat2:
#                   obj_element.append(AND(b))  
#           elif el == "OR":
#                dat = c.find('=')
#                dat1 = c[dat + 1:]
#                dat2 = dat1.split(',')
#                for b in dat2:
#                   obj_element.append(OR(b)) 
#           elif el == "NOT":
#                dat = c.find('=')
#                dat1 = c[dat + 1:]
#                dat2 = dat1.split(',')
#                for b in dat2:
#                   obj_element.append(NOT(b)) 
#           elif el == "XOR":
#                dat = c.find('=')
#                dat1 = c[dat + 1:]
#                dat2 = dat1.split(',')
#                for b in dat2:
#                   obj_element.append(XOR(b))
#           elif el == "NAND":
#                dat = c.find('=')
#                dat1 = c[dat + 1:]
#                dat2 = dat1.split(',')
#                for b in dat2:
#                   obj_element.append(NAND(b)) 
#           elif el == "D_TRIGER":
#                dat = c.find('=')
#                dat1 = c[dat + 1:]
#                dat2 = dat1.split(',')
#                for b in dat2:
#                   obj_element.append(D_TRIGER(b))  
#     return obj_element    


# def GetIO(data):
#     outputs = []
#     for c in data:
#         value = ""
#         for a in range(len(c)):
#             f = ord(c[a])
#             if (f > 47 and f < 58) or ( f == 95) or (f > 64 and f < 91) or (f > 96 and f < 123):
#                 value = value + c[a]
#         outputs.append(IO(value))  
#     return outputs

# def GetConection(data):
#    conection = []
#     #obj_element.append
#    for c in data:
#        el = ''
#        cnt = 0
#        while (len(c) > 0) and (c[cnt] != '>'):
#           el = el + c[cnt]
#           cnt += 1
#        a = c[cnt + 1:]
#        cnt = 0
#        b = el.split('.')  # attdala elementa vardu no tā izejas nosaukuma
#        f = WIRE(el)
#        g = Connections(f)
#        g.InDevace.append(b[0])
#        g.InConection.append(b[1])
#        h = a.split(',')
#        for p in h:
#           w = p.split('.')
#           g.InDevace.append(w[0])
#           g.InConection.append(w[1])
#        conection.append(g)   
#    return conection

# def Conekted(circuit, wire):
#    pass

# def GetCircuit(data):
    
#     circuit = Circuit()

#     f = delChar(data, ' ')
#     f1 = delComent(f)
#     f2 = delChar(f1, '\n')

#     input = delChar(GetBlock(f2, "Inputs"), ';').split(',')
#     output = delChar(GetBlock(f2, "Outputs"), ';').split(',')
#     element = GetBlock(f2, "Elements").split(';')
#     vire = GetBlock(f2, 'Wire').split(';')
#     print(vire)

#     Obj_input = GetIO(input)
#     Obj_output = GetIO(output)
#     Obj_AND = getElements(element, 'AND')
#     Obj_NAND = getElements(element, 'NAND')
#     Obj_OR = getElements(element, 'OR')
#     Obj_NOR = getElements(element, 'NOR')
#     Obj_D_TRIGER = getElements(element, 'D_TRIGER')
#     Obj_NOT = getElements(element, 'NOT')
#     Obj_Conektion = GetConection(vire)
    
#     for c in Obj_input:
#        circuit.addIOinput(c)
#     for c in Obj_output:
#        circuit.addIOoutputs(c)
#     for c in Obj_AND:
#        circuit.addLogicGates(c)
#     for c in Obj_NAND:
#        circuit.addLogicGates(c)
#     for c in Obj_OR:
#        circuit.addLogicGates(c)
#     for c in Obj_NOR:
#        circuit.addLogicGates(c)
#     for c in Obj_D_TRIGER:
#        circuit.addLogicGates(c)
#     for c in Obj_NOT:
#        circuit.addLogicGates(c)

#     for c in Obj_Conektion:
#        circuit.wire.append(c.wire)
#        faind = False
#        for cc in c.InDevace:
#           for e in circuit.iinputs:
#               if e.name == cc.ToNameDevace:
#                 if cc.ToDevaceOutput == 'I':
#                     e.addWireInt(c.wire)
#                 elif cc.ToDevaceOutput == 'D':
#                     e.addWireOut(c.wire)

#           for e in circuit.ioutputs:  
#               if e.name == cc.ToNameDevace:
#                 if cc.ToDevaceOutput == 'I':
#                     e.addWireInt(c.wire)
#                 elif cc.ToDevaceOutput == 'D':
#                     e.addWireOut(c.wire)
            
#           for e in circuit.gates:
#               if e.name == cc.ToNameDevace:
#                 if isinstance(e, D_TRIGER):
#                    if cc.ToDevaceOutput == 'D':
#                       e.addWireD(c.wire)
#                    elif cc.ToDevaceOutput == 'C':
#                       e.addWireC(c.wire)
#                    elif cc.ToDevaceOutput == 'Q':
#                       e.addWireQ(c.wire)
#                    elif cc.ToDevaceOutput == '_Q':
#                       e.addWire_Q(c.wire)
#                 elif isinstance(e, NOT):
#                    if cc.ToDevaceOutput == 'A':
#                       e.addWireA(c.wire)
#                    elif cc.ToDevaceOutput == 'O':
#                       e.addWireO(c.wire)
#                 else:
#                    if cc.ToDevaceOutput == 'A':
#                       e.addWireA(c.wire)
#                    elif cc.ToDevaceOutput == 'B':
#                       e.addWireB(c.wire)
#                    elif cc.ToDevaceOutput == 'O':
#                       e.addWireO(c.wire)