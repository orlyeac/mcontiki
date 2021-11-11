import os

#Z1_0.8N_CH4_2to4_P

file_list1 = os.listdir('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/w/')
#file_list2 = os.listdir('/home/mmmorfa/contiki-ng/examples/6tisch/simple-node/logs/N18_8.16_CSD1_CH16_M3/')

#print (file_list1)
i = 0
#k = len(file_list2)
l = 1
#o = 88

#print(file_list1)

"""
if not os.path.isfile('/home/mmmorfa/contiki-ng/examples/6tisch/simple-node/logs/w/log_2_' + '{}.txt'.format(str(o))):
    print ("No esta")
"""

while os.path.isfile('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/w/' + str(file_list1[i])):
    while True:
        if not os.path.isfile('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/Z1_0.5N_CH4_2to4_P/log_2_' + '{}.txt'.format(str(l))):
            os.rename('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/w/' + str(file_list1[i]) , '/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/Z1_0.5N_CH4_2to4_P/log_2_' + '{}.txt'.format(str(l)))
            break
        l+=1
    i+=1