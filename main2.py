from Logic_Gate_2 import *
from Compilation import *
import re 
data = r'''Name = Test
Module{
}

Inputs{
D1, D2, D3, D4, adres, clk, rw
}

Outputs{
Q1, Q2, Q3, Q4
}

Elements{
   // Jgddgyrdhutdhf
AND = andQ11, andQ12, andQ13, andQ14;
D_TRIGER = D11, D12, D13, D14;
AND = andD11, andD12, andD13, andD14;
AND = and1Cont1, and1Cont2, and1Cont3;
//hfsfjhg jgdfh uyfghh
NOT = not1;
AND = andQ21, andQ22, andQ23, andQ24;
D_TRIGER = D21, D22, D23, D24;
AND = andD21, andD22, andD23, andD24;
AND = and2Cont1, and2Cont2, and2Cont3;
NOT = not2;
OR = or_O1, or_O2, or_O3, or_O4;   //test test
AND = and_O1, and_O2, and_O3, and_O4
}

Wire{
D1.O > andQ11.A, andQ21.A;  // Test koent
D2.O > andQ12.A, andQ22.A;
D3.O > andQ13.A, andQ23.A;  // Test jgddyjd
D4.O > andQ14.A, andQ24.A;
clk.O > and1Cont2.A, and2Cont2.A;
and1Cont1.O > and1Cont2.B, andD11.B, andD12.B, andD13.B, andD14.B;
and2Cont1.O > and2Cont2.B, andD21.B, andD22.B, andD23.B, andD24.B;
and1Cont2.O > D11.C, D12.C, D13.C, D14.C;
and2Cont2.O > D21.C, D22.C, D23.C, D24.C;
and1Cont3.O > andD11.B, andD12.B, andD13.B, andD14.B;
and2Cont3.O > andD21.B, andD22.B, andD23.B, andD24.B;
not2.O > and2Cont3.B, and1Cont3.B, and_O1.B, and_O2.B, and_O3.B, and_O4.B;
adres.O > not1.A, and2Cont1.A, and2Cont3.A;
rw.O > not2.A, and1Cont1.B, and2Cont1.B;
not1.O > and1Cont1.A, and1Cont3.A;
andD11.O > or_O1.B; andD12.O > or_O.B; andD13.O > or_O3.B; andD14.O > or_O4.B;
andD21.O > or_O1.A; andD22.O > or_O.A; andD23.O > or_O3.A; andD24.O > or_O4.A;
andQ11.O > D11.D; andQ12.O > D12.D; andQ13.O > D13.D; andQ14.O > D14.D;
andQ21.O > D21.D; andQ22.O > D22.D; andQ23.O > D23.D; andQ24.O > D24.D;
D11.Q > andD11.A; D12.Q > andD12.A; D13.Q > andD13.A; D14.Q > andD14.A;
D21.Q > andD21.A; D22.Q > andD22.A; D23.Q > andD23.A; D24.Q > andD24.A;
or_O1.O > and_O1.A; or_O2.O > and_O2.A; or_O3.O > and_O3.A; or_O4.O > and_O4.A;
or_O1.O > Q1.I; or_O2.O > Q2.I; or_O3.O > Q3.I; or_O4.O > Q4.I
}


Test{

D1    => 111
D2    => 111
D3    => 000
D4    => 000
Adres => 000
clk   => 001
rw    => 000

D1    => __/"""\______=
D2    => __/"""\______=
D3    => _____________=
D4    => _____________=
clk   => ___/"""\_____=
rw    => _/"""""""""\_=
Adres =>______________=

}
'''


data1 = r'''
//_______________________ bit _____________________________________
Circuit bit{
Inputs{
  set, w, r, d }

Outputs{
 d    }

Elements{
AND = iand, oand;
D_TRIGER = D

}
Wire{
d > iand.A;
w > iand.B;
iand.O > D.D;
set > D.C;
D.Q > oand.A;
r > oand.B;
oand.O > d
}}

//_______________________ Register _____________________________________

Circuit Register{
Inputs{
D1, D2, D3, D4, R, W, CS
}

Outputs{
Q1, Q2, Q3, Q,4
}
Elements{
bit = b1, b2, b3, b4;
AND = and_read, and_write
}
Wire{
D1 > b1.d; D2 > b2.d; D3 > b3.d; D4 > b4;
R > and_read.A; W > and_write.A; CS > and_read.B, and_write.B;
and_read.O > b1.r, b2.r, b3.r, b4.r;
and_write.O > b1.w, b2.w, b3.w, b4.w;
b1.d > Q1; b2.d > Q2; b3.d > Q3; b4.d > Q4
}}

//______________________ Adress ______________________________________

Circuit Adress{
Inputs{
A1, A2
}
Outputs{
R1, R2, R3, R4
}
Elements{
AND = and_R1, and_R2, and_R3, and_R4;
NOT = not_A1, not_A2
}
Wire{
A1 > not_A1.A, and_R2.A, and_R4.B;
A2 > not_A2.A, and_R3.A, and_R4.A;
not_A1.O > and_R1.A, and_R3.B;
not_A2.O > and_R1.B, and_R2.B;
and_R1.O > R1;
and_R2.O > R2;
and_R3.O > R3;
and_R4.O > R4;
}
}
//_________________________ OR_4X ___________________________________

Circuit OR_4X{
Inputs{I1, I2, I3, I4
}
Outputs{
O
}
Elements{
OR = or1, or2, or3
}
Wire{
I1 > or1.A; I2 > or1.B; I3 > or2.A; I4 > or2.B;
or1.O > or3.A;
or2.O > or3.B;
or3.O > O 
}

}
//____________________ Main ________________________________________
Main{
Inputs{
D1, D2, D3, D4, R, W, A1, A2
}
Outputs{
Q1, Q2, Q3, Q4
}
Elements{
Adress = adres;
Register = R1, R2, R3, R4;

OR_4X = or_4X1, or_4X2, or_4X3, or_4x4

}

Wire{
or_4X1.O > Q1;
or_4X2.O > Q2;
or_4X3.O > Q3;
or_4X4.O > Q4;

R1.Q1 > or_4X1.I1;
R2.Q1 > or_4X1.I2;
R3.Q1 > or_4X1.I3;
R4.Q1 > or_4x1.I4;

R1.Q2 > or_4X2.I1;
R2.Q2 > or_4X2.I2;
R3.Q2 > or_4X2.I3;
R4.Q2 > or_4x2.I4;

R1.Q3 > or_4X3.I1;
R2.Q3 > or_4X3.I2;
R3.Q3 > or_4X3.I3;
R4.Q3 > or_4x3.I4;

R1.Q4 > or_4X4.I1;
R2.Q4 > or_4X4.I2;
R3.Q4 > or_4X4.I3;
R4.Q4 > or_4x4.I4;

D1 > R1.D1, R2.D1, R3.D1, R4.D1;
D2 > R1.D2, R2.D2, R3.D2, R4.D2;
D3 > R1.D3, R2.D3, R3.D3, R4.D3;
D4 > R1.D4, R2.D4, R3.D4, R4.D4;

A1 > adres.A1; A2 > adres.A2;
adres.R1 > R1.CS;
adres.R2 > R2.CS;
adres.R3 > R3.CS;
adres.R4 > R4.CS;

R > R1.R, R2.R, R3.R, R4.R;
W > R1.W, R2.W, R4.W, R4.W

}

}
Test{

D1    > 111
D2    > 111
D3    > 000
D4    > 000
Adres > 000
clk   > 001
rw    > 000

D1    > __/"""\______=
D2    > __/"""\______=
D3    > _____________=
D4    > _____________=
clk   > ___/"""\_____=
rw    > _/"""""""""\_=
Adres >______________=

}
}
'''

def FindTheCreated(data, key):
    dd = data.split(';')
    atbilde = []
    for c in dd:
       a = c.split('=')
       if(a[0] == key):
          kk = a[1].split(',')
          for s in kk:
              atbilde.append(s)
    return atbilde



dd = Sorting(data1)
# kw = AllKeyWord()
# kw.add(dd)
kw = []
for c in dd[0]:
  kw.append(c.name)


ta = []

for c in range(len(kw)):
  ta.append(FindTheCreated(dd[1].Elements, kw[c]))



tree = Tree('Main')


print('\n')
print(mm)
print('\n')



# # cc = bb[1].Elements.split(';')
# # dd = cc
# cc = Data_Tree(data1)
# cc.display()
# #ds = Data_Tree(data1)




# # Adress=adres;Register=R1,R2,R3,R4;OR_4X=or_4X1,or_4X2,or_4X3,or_4x4




# #print(bb)
# # a = None
# # for c in bb[0]:
# #   if c.name == 'bit':
# #     a = c

# # print(a)








# # # Izveido koku un pievieno mezglus  
# # my_tree = Tree("Root")  
# # my_tree.add_node("Root", "Child 1")  
# # my_tree.add_node("Root", "Child 2")  
# # my_tree.add_node("Child 1", "Grandchild 1")  
# # my_tree.add_node("Child 1", "Grandchild 2")  
# # my_tree.add_node("Child 2", "Grandchild 3")  

# # # Parāda koka struktūru  
# # my_tree.display()
 

