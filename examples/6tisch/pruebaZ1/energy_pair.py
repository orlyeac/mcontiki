from energy import *
import numpy as np
import matplotlib.pyplot as plt

N = 5

c1_05, e1_05 = node_energy('Z1_0.5_CH16_2-4_P', 1)
c1_08, e1_08 = node_energy('Z1_0.8_CH16_2-4_P', 1)
c1_10, e1_10 = node_energy('Z1_1.0_CH16_2-4_P', 1)
c1_15, e1_15 = node_energy('Z1_1.5_CH16_2-4_P', 1)
c1_18, e1_18 = node_energy('Z1_1.8_CH16_2-4_P', 1)

c1 = [c1_05, c1_08, c1_10, c1_15, c1_18]
e1 = [e1_05, e1_08, e1_10, e1_15, e1_18]

c2_05, e2_05 = node_energy('Z1_0.5_CH16_2-4_P', 2)
c2_08, e2_08 = node_energy('Z1_0.8_CH16_2-4_P', 2)
c2_10, e2_10 = node_energy('Z1_1.0_CH16_2-4_P', 2)
c2_15, e2_15 = node_energy('Z1_1.5_CH16_2-4_P', 2)
c2_18, e2_18 = node_energy('Z1_1.8_CH16_2-4_P', 2)

c2 = [c2_05, c2_08, c2_10, c2_15, c2_18]
e2 = [e2_05, e2_08, e2_10, e2_15, e2_18]

ind = np.arange(N)  
width = 0.3

fig = plt.subplots(figsize =(10, 7))


p1 = plt.bar(ind, c2, width, color=(0.2, 0.4, 0.6, 0.6), hatch= '\\')
p2 = plt.bar(ind, c1, width, bottom = c2, color=(0.2, 0.6, 0.4, 0.6), hatch= '/')

plt.ylabel('Consumo de energía (mJ)', fontsize='12')
plt.xlabel('Factor beta de fase intensiva de envío de EBs', fontsize='12')
plt.xticks(ind, ('0.5', '0.8', '1.0', '1.5', '1.8'), fontsize='12')
plt.legend((p1[0], p2[0]), ('Nodo joinseeker','Nodo coordinador'), fontsize='12')

plt.show()