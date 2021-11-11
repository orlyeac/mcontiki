from energy import *
import numpy as np
import matplotlib.pyplot as plt

N = 3

n4_fx, e_fx = node_energy('Z1_EBP4_CH16_L3', 4)
n4_08, e_08 = node_energy('Z1_0.8_CH16_2-4_L3', 4)
n4_18, e_18 = node_energy('Z1_1.8_CH16_2-4_L3', 4)

c = [n4_fx, n4_08, n4_18]
e = [e_fx, e_08, e_18]

n3_fx, e1_fx = node_energy('Z1_EBP4_CH16_L3', 3)
n3_08, e1_08 = node_energy('Z1_0.8_CH16_2-4_L3', 3)
n3_18, e1_18 = node_energy('Z1_1.8_CH16_2-4_L3', 3)

c1 = [n3_fx, n3_08, n3_18]
e1 = [e1_fx, e1_08, e1_18]

n2_fx, e2_fx = node_energy('Z1_EBP4_CH16_L3', 2)
n2_08, e2_08 = node_energy('Z1_0.8_CH16_2-4_L3', 2)
n2_18, e2_18 = node_energy('Z1_1.8_CH16_2-4_L3', 2)

c2 = [n2_fx, n2_08, n2_18]
e2 = [e2_fx, e2_08, e2_18]

n1_fx, e3_fx = node_energy('Z1_EBP4_CH16_L3', 1)
n1_08, e3_08 = node_energy('Z1_0.8_CH16_2-4_L3', 1)
n1_18, e3_18 = node_energy('Z1_1.8_CH16_2-4_L3', 1)

c3 = [n1_fx, n1_08, n1_18]
e3 = [e3_fx, e3_08, e3_18]

s1 = np.add(c, c1)
s2 = np.add(s1, c2)

ind = np.arange(N)  
width = 0.2

fig = plt.subplots(figsize =(10, 7))

p = plt.bar(ind, c, width, color=(0.4, 0.6, 0.6, 0.4), hatch= '///')
p1 = plt.bar(ind, c1, width, bottom = c, color=(0.2, 0.4, 0.6, 0.6), hatch= '\\')
p2 = plt.bar(ind, c2, width, bottom = s1, color=(0.2, 0.6, 0.4, 0.6), hatch= '/')
p3 = plt.bar(ind, c3, width, bottom = s2, color=(0.4, 0.4, 0.4, 0.4), hatch= '//')

plt.ylabel('Consumo de energía (mJ)', fontsize='12')
plt.xlabel('Configuración de Tx de EBs', fontsize='12')
plt.xticks(ind, ('minimal TiSCH', 'TDEB-TSCH con beta = 0.8', 'TDEB-TSCH con beta = 1.8'), fontsize='8')
plt.legend((p[0], p1[0], p2[0], p3[0]), ('Nodo joinseeker (salto 3)', 'Nodo joinseeker (salto 2)', 'Nodo joinseeker (salto 1)', 'Nodo coordinador'), fontsize='12')

plt.show()