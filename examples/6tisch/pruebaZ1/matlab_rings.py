import numpy as np
import scipy.io
from functions import *

time_list1 = average_association_time ('Z1_EBP4_CH4_R2_50%')
time_list2 = average_association_time ('Z1_EBP4_CH4_R2_75%')
time_list3 = average_association_time ('Z1_EBP4_CH4_R2')


a = np.array(time_list1)
b = np.array(time_list2)
c = np.array(time_list3)

time_list4 = average_association_time ('Z1_0.8_CH4_2-4_R2_50%')
time_list5 = average_association_time ('Z1_0.8_CH4_2-4_R2_75%')
time_list6 = average_association_time ('Z1_0.8_CH4_2-4_R2')

d = np.array(time_list4)
e = np.array(time_list5)
f = np.array(time_list6)


time_list7 = average_association_time ('Z1_1.8_CH4_2-4_R2_50%')
time_list8 = average_association_time ('Z1_1.8_CH4_2-4_R2_75%')
time_list9 = average_association_time ('Z1_1.8_CH4_2-4_R2')

g = np.array(time_list7)
h = np.array(time_list8)
i = np.array(time_list9)

scipy.io.savemat('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/matlab/Z1_Anillos_2-4_CH4.mat', 
                    dict(m6TiSCH_50=a, m6TiSCH_75=b, m6TiSCH_100=c, TDEB08_50=d, TDEB08_75=e, 
                            TDEB08_100=f, TDEB18_50=g, TDEB18_75=h, TDEB18_100=i))

#mat = scipy.io.loadmat('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/matlab/Z1_ParC-J_2-4.mat')

#print (mat)