import numpy as np
import scipy.io
from functions import *
from energy import *

dic1 = calculate_energy ('Z1_0.5_CH16_2-4_P')

node1_05 = []
node2_05 = []

for i in range(1,len(dic1)+1):
    node1_05.append(dic1.get(i).get(1))
    node2_05.append(dic1.get(i).get(2))

node1_05 = list(map(lambda x: x/1000, node1_05)) 
node2_05 = list(map(lambda x: x/1000, node2_05))

a = np.array([node1_05, node2_05])
#---------------------------------------------------------
dic2 = calculate_energy ('Z1_0.8_CH16_2-4_P')

node1_08 = []
node2_08 = []

for i in range(1,len(dic2)+1):
    node1_08.append(dic2.get(i).get(1))
    node2_08.append(dic2.get(i).get(2))

node1_08 = list(map(lambda x: x/1000, node1_08)) 
node2_08 = list(map(lambda x: x/1000, node2_08))

b = np.array([node1_08, node2_08])
#----------------------------------------------------------
dic3 = calculate_energy ('Z1_1.0_CH16_2-4_P')

node1_10 = []
node2_10 = []

for i in range(1,len(dic3)+1):
    node1_10.append(dic3.get(i).get(1))
    node2_10.append(dic3.get(i).get(2))

node1_10 = list(map(lambda x: x/1000, node1_10)) 
node2_10 = list(map(lambda x: x/1000, node2_10))

c = np.array([node1_10, node2_10])
#----------------------------------------------------------
dic4 = calculate_energy ('Z1_1.5_CH16_2-4_P')

node1_15 = []
node2_15 = []

for i in range(1,len(dic4)+1):
    node1_15.append(dic4.get(i).get(1))
    node2_15.append(dic4.get(i).get(2))

node1_15 = list(map(lambda x: x/1000, node1_15)) 
node2_15 = list(map(lambda x: x/1000, node2_15))

d = np.array([node1_15, node2_15])
#----------------------------------------------------------
dic5 = calculate_energy ('Z1_1.8_CH16_2-4_P')

node1_18 = []
node2_18 = []

for i in range(1,len(dic5)+1):
    node1_18.append(dic5.get(i).get(1))
    node2_18.append(dic5.get(i).get(2))

node1_18 = list(map(lambda x: x/1000, node1_18)) 
node2_18 = list(map(lambda x: x/1000, node2_18))

e = np.array([node1_18, node2_18])

#print (a)

scipy.io.savemat('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/matlab/Z1_ParC-J_2-4_CH16_Energy.mat', 
                    dict(beta05=a, beta08=b, beta10=c, beta15=d, beta18=e))