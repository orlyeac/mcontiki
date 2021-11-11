from energy import *
import numpy as np
import matplotlib.pyplot as plt

N = 3

#Fijo
n1_fx, e = node_energy('Z1_EBP4_CH4_R2_75%', 1)
n2_fx, e1 = node_energy('Z1_EBP4_CH4_R2_75%', 2)
n3_fx, e2 = node_energy('Z1_EBP4_CH4_R2_75%', 3)
n4_fx, e3 = node_energy('Z1_EBP4_CH4_R2_75%', 4)
n5_fx, e4 = node_energy('Z1_EBP4_CH4_R2_75%', 5)

r1_fx = n2_fx + n3_fx + n4_fx + n5_fx

n6_fx, e5 = node_energy('Z1_EBP4_CH4_R2_75%', 6)
n7_fx, e6 = node_energy('Z1_EBP4_CH4_R2_75%', 7)
n8_fx, e7 = node_energy('Z1_EBP4_CH4_R2_75%', 8)
n9_fx, e8 = node_energy('Z1_EBP4_CH4_R2_75%', 9)
n10_fx, e9 = node_energy('Z1_EBP4_CH4_R2_75%', 10)
n11_fx, e10 = node_energy('Z1_EBP4_CH4_R2_75%', 11)

r2_fx = n6_fx + n7_fx + n8_fx + n9_fx + n10_fx + n11_fx

#0.8
n1_08, e0 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 1)
n2_08, e11 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 2)
n3_08, e12 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 3)
n4_08, e13 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 4)
n5_08, e14 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 5)

r1_08 = n2_08+ n3_08 + n4_08 + n5_08

n6_08, e15 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 6)
n7_08, e16 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 7)
n8_08, e17 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 8)
n9_08, e18 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 9)
n10_08, e19 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 10)
n11_08, e20 = node_energy('Z1_0.8_CH4_2-4_R2_75%', 11)

r2_08 = n6_08 + n7_08 + n8_08 + n9_08 + n10_08 + n11_08

#1.8
n1_18, e02 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 1)
n2_18, e21 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 2)
n3_18, e22 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 3)
n4_18, e23 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 4)
n5_18, e24 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 5)

r1_18 = n2_18+ n3_18 + n4_18 + n5_18

n6_18, e25 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 6)
n7_18, e26 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 7)
n8_18, e27 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 8)
n9_18, e28 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 9)
n10_18, e29 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 10)
n11_18, e30 = node_energy('Z1_1.8_CH4_2-4_R2_75%', 11)

r2_18 = n6_18 + n7_18 + n8_18 + n9_18 + n10_18 + n11_18

c = list(map(lambda x: x/1000, [n1_fx, n1_08, n1_18])) 
r1 = list(map(lambda x: x/1000, [r1_fx, r1_08, r1_18]))
r2 = list(map(lambda x: x/1000, [r2_fx, r2_08, r2_18]))

print (c)
print (r1)
print (r2)


#yt1 = list(map(lambda x: x/1000, [tA1, tB1, tC1]))

s1 = np.add(r1, r2)

ind = np.arange(N)  
width = 0.2

fig = plt.subplots(figsize =(10, 7))

p = plt.bar(ind, r2, width, color=(0.4, 0.6, 0.6, 0.4), hatch= '///')
p1 = plt.bar(ind, r1, width, bottom = r2, color=(0.2, 0.4, 0.6, 0.6), hatch= '\\')
p2 = plt.bar(ind, c, width, bottom = s1, color=(0.2, 0.6, 0.4, 0.6), hatch= '/')

plt.ylabel('Consumo de energía (J)', fontsize='12')
plt.xlabel('Configuración de Tx de EBs', fontsize='12')
plt.xticks(ind, ('minimal TiSCH', 'TDEB-TSCH con beta = 0.8', 'TDEB-TSCH con beta = 1.8'), fontsize='8')
plt.legend((p[0], p1[0], p2[0]), ('Segundo Anillo', 'Primer Anillo', 'Nodo coordinador'), fontsize='12')

plt.show()