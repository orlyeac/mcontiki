import numpy as np
import scipy.io
from functions import *

time_list1 = average_association_time ('Z1_0.5_CH16_2-4_P')
time_list2 = average_association_time ('Z1_0.8_CH16_2-4_P')
time_list3 = average_association_time ('Z1_1.0_CH16_2-4_P')
time_list4 = average_association_time ('Z1_1.5_CH16_2-4_P')
time_list5 = average_association_time ('Z1_1.8_CH16_2-4_P')

a = np.array(time_list1)
b = np.array(time_list2)
c = np.array(time_list3)
d = np.array(time_list4)
e = np.array(time_list5)

time_list6 = average_association_time ('Z1_0.5_CH8_2-4_P')
time_list7 = average_association_time ('Z1_0.8_CH8_2-4_P')
time_list8 = average_association_time ('Z1_1.0_CH8_2-4_P')
time_list9 = average_association_time ('Z1_1.5_CH8_2-4_P')
time_list10 = average_association_time ('Z1_1.8_CH8_2-4_P')

f = np.array(time_list6)
g = np.array(time_list7)
h = np.array(time_list8)
i = np.array(time_list9)
j = np.array(time_list10)

time_list11 = average_association_time ('Z1_0.5_CH4_2-4_P')
time_list12 = average_association_time ('Z1_0.8_CH4_2-4_P')
time_list13 = average_association_time ('Z1_1.0_CH4_2-4_P')
time_list14 = average_association_time ('Z1_1.5_CH4_2-4_P')
time_list15 = average_association_time ('Z1_1.8_CH4_2-4_P')

k = np.array(time_list11)
l = np.array(time_list12)
m = np.array(time_list13)
n = np.array(time_list14)
o = np.array(time_list15)

scipy.io.savemat('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/matlab/Z1_ParC-J_2-4.mat', 
                    dict(CH16_beta05=a, CH16_beta08=b, CH16_beta10=c, CH16_beta15=d, CH16_beta18=e, 
                            CH8_beta05=f, CH8_beta08=g, CH8_beta10=h, CH8_beta15=i, CH8_beta18=j, 
                            CH4_beta05=k, CH4_beta08=l, CH4_beta10=m, CH4_beta15=n, CH4_beta18=o))

#mat = scipy.io.loadmat('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/matlab/Z1_ParC-J_2-4.mat')

#print (mat)
