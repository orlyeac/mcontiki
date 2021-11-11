import numpy as np
import scipy.io
from functions import *
from energy import *

dic1 = calculate_energy ('Z1_EBP4_CH4_R2_75%')

node1_m6TiSCH = []
node2_m6TiSCH = []
node3_m6TiSCH = []
node4_m6TiSCH = []
node5_m6TiSCH = []
node6_m6TiSCH = []
node7_m6TiSCH = []
node8_m6TiSCH = []
node9_m6TiSCH = []
node10_m6TiSCH = []
node11_m6TiSCH = []

for i in range(1,len(dic1)+1):
    node1_m6TiSCH.append(dic1.get(i).get(1))
    node2_m6TiSCH.append(dic1.get(i).get(2))
    node3_m6TiSCH.append(dic1.get(i).get(3))
    node4_m6TiSCH.append(dic1.get(i).get(4))
    node5_m6TiSCH.append(dic1.get(i).get(5))
    node6_m6TiSCH.append(dic1.get(i).get(6))
    node7_m6TiSCH.append(dic1.get(i).get(7))
    node8_m6TiSCH.append(dic1.get(i).get(8))
    node9_m6TiSCH.append(dic1.get(i).get(9))
    node10_m6TiSCH.append(dic1.get(i).get(10))
    node11_m6TiSCH.append(dic1.get(i).get(11))

node1_m6TiSCH = list(map(lambda x: x/1000, node1_m6TiSCH)) 
node2_m6TiSCH = list(map(lambda x: x/1000, node2_m6TiSCH))
node3_m6TiSCH = list(map(lambda x: x/1000, node3_m6TiSCH))
node4_m6TiSCH = list(map(lambda x: x/1000, node4_m6TiSCH))
node5_m6TiSCH = list(map(lambda x: x/1000, node5_m6TiSCH))
node6_m6TiSCH = list(map(lambda x: x/1000, node6_m6TiSCH))
node7_m6TiSCH = list(map(lambda x: x/1000, node7_m6TiSCH))
node8_m6TiSCH = list(map(lambda x: x/1000, node8_m6TiSCH))
node9_m6TiSCH = list(map(lambda x: x/1000, node9_m6TiSCH))
node10_m6TiSCH = list(map(lambda x: x/1000, node10_m6TiSCH))
node11_m6TiSCH = list(map(lambda x: x/1000, node11_m6TiSCH))

a = np.array([node1_m6TiSCH, node2_m6TiSCH, node3_m6TiSCH, node4_m6TiSCH, node5_m6TiSCH, 
                node6_m6TiSCH, node7_m6TiSCH, node8_m6TiSCH, node9_m6TiSCH, node10_m6TiSCH, node11_m6TiSCH])
#---------------------------------------------------------
dic2 = calculate_energy ('Z1_0.8_CH4_2-4_R2_75%')

node1_TDEB08 = []
node2_TDEB08 = []
node3_TDEB08 = []
node4_TDEB08 = []
node5_TDEB08 = []
node6_TDEB08 = []
node7_TDEB08 = []
node8_TDEB08 = []
node9_TDEB08 = []
node10_TDEB08 = []
node11_TDEB08 = []

for i in range(1,len(dic2)+1):
    node1_TDEB08.append(dic2.get(i).get(1))
    node2_TDEB08.append(dic2.get(i).get(2))
    node3_TDEB08.append(dic2.get(i).get(3))
    node4_TDEB08.append(dic2.get(i).get(4))
    node5_TDEB08.append(dic2.get(i).get(5))
    node6_TDEB08.append(dic2.get(i).get(6))
    node7_TDEB08.append(dic2.get(i).get(7))
    node8_TDEB08.append(dic2.get(i).get(8))
    node9_TDEB08.append(dic2.get(i).get(9))
    node10_TDEB08.append(dic2.get(i).get(10))
    node11_TDEB08.append(dic2.get(i).get(11))

node1_TDEB08 = list(map(lambda x: x/1000, node1_TDEB08)) 
node2_TDEB08 = list(map(lambda x: x/1000, node2_TDEB08))
node3_TDEB08 = list(map(lambda x: x/1000, node3_TDEB08))
node4_TDEB08 = list(map(lambda x: x/1000, node4_TDEB08))
node5_TDEB08 = list(map(lambda x: x/1000, node5_TDEB08))
node6_TDEB08 = list(map(lambda x: x/1000, node6_TDEB08))
node7_TDEB08 = list(map(lambda x: x/1000, node7_TDEB08))
node8_TDEB08 = list(map(lambda x: x/1000, node8_TDEB08))
node9_TDEB08 = list(map(lambda x: x/1000, node9_TDEB08))
node10_TDEB08 = list(map(lambda x: x/1000, node10_TDEB08))
node11_TDEB08 = list(map(lambda x: x/1000, node11_TDEB08))

b = np.array([node1_TDEB08, node2_TDEB08, node3_TDEB08, node4_TDEB08, node5_TDEB08, 
                node6_TDEB08, node7_TDEB08, node8_TDEB08, node9_TDEB08, node10_TDEB08, node11_TDEB08])
#----------------------------------------------------------
dic3 = calculate_energy ('Z1_1.8_CH4_2-4_R2_75%')

node1_TDEB18 = []
node2_TDEB18 = []
node3_TDEB18 = []
node4_TDEB18 = []
node5_TDEB18 = []
node6_TDEB18 = []
node7_TDEB18 = []
node8_TDEB18 = []
node9_TDEB18 = []
node10_TDEB18 = []
node11_TDEB18 = []

for i in range(1,len(dic3)+1):
    node1_TDEB18.append(dic3.get(i).get(1))
    node2_TDEB18.append(dic3.get(i).get(2))
    node3_TDEB18.append(dic3.get(i).get(3))
    node4_TDEB18.append(dic3.get(i).get(4))
    node5_TDEB18.append(dic3.get(i).get(5))
    node6_TDEB18.append(dic3.get(i).get(6))
    node7_TDEB18.append(dic3.get(i).get(7))
    node8_TDEB18.append(dic3.get(i).get(8))
    node9_TDEB18.append(dic3.get(i).get(9))
    node10_TDEB18.append(dic3.get(i).get(10))
    node11_TDEB18.append(dic3.get(i).get(11))

node1_TDEB18 = list(map(lambda x: x/1000, node1_TDEB18)) 
node2_TDEB18 = list(map(lambda x: x/1000, node2_TDEB18))
node3_TDEB18 = list(map(lambda x: x/1000, node3_TDEB18))
node4_TDEB18 = list(map(lambda x: x/1000, node4_TDEB18))
node5_TDEB18 = list(map(lambda x: x/1000, node5_TDEB18))
node6_TDEB18 = list(map(lambda x: x/1000, node6_TDEB18))
node7_TDEB18 = list(map(lambda x: x/1000, node7_TDEB18))
node8_TDEB18 = list(map(lambda x: x/1000, node8_TDEB18))
node9_TDEB18 = list(map(lambda x: x/1000, node9_TDEB18))
node10_TDEB18 = list(map(lambda x: x/1000, node10_TDEB18))
node11_TDEB18 = list(map(lambda x: x/1000, node11_TDEB18))

c = np.array([node1_TDEB18, node2_TDEB18, node3_TDEB18, node4_TDEB18, node5_TDEB18, 
                node6_TDEB18, node7_TDEB18, node8_TDEB18, node9_TDEB18, node10_TDEB18, node11_TDEB18])


#print (a)

scipy.io.savemat('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/matlab/Z1_Anillos75%_2-4_CH4_Energy.mat', 
                    dict(m6TiSCH=a, TDEB08=b, TDEB18=c))