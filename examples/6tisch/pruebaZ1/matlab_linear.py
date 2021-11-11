import numpy as np
import scipy.io
from functions import *

time_list1 = average_association_time ('Z1_EBP4_CH16_P')
time_list2 = average_association_time ('Z1_EBP4_CH16_L2')
time_list3 = average_association_time ('Z1_EBP4_CH16_L3')


a = np.array(time_list1)
b = np.array(time_list2)
c = np.array(time_list3)

time_list4 = average_association_time ('Z1_0.8_CH16_2-4_P')
time_list5 = average_association_time ('Z1_0.8_CH16_2-4_L2')
time_list6 = average_association_time ('Z1_0.8_CH16_2-4_L3')

d = np.array(time_list4)
e = np.array(time_list5)
f = np.array(time_list6)


time_list7 = average_association_time ('Z1_1.8_CH16_2-4_P')
time_list8 = average_association_time ('Z1_1.8_CH16_2-4_L2')
time_list9 = average_association_time ('Z1_1.8_CH16_2-4_L3')

g = np.array(time_list7)
h = np.array(time_list8)
i = np.array(time_list9)

scipy.io.savemat('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/matlab/Z1_Lineal_2-4_CH16.mat', 
                    dict(m6TiSCH_hop1=a, m6TiSCH_hop2=b, m6TiSCH_hop3=c, TDEB08_hop1=d, TDEB08_hop2=e, 
                            TDEB08_hop3=f, TDEB18_hop1=g, TDEB18_hop2=h, TDEB18_hop3=i))

#mat = scipy.io.loadmat('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/matlab/Z1_ParC-J_2-4.mat')

#print (mat)