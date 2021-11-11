# -*- coding: utf-8 -*-

"""
Created on Tue Dec 8 21:25:27 2020

@author: mmmorfa
"""
#--------------------------------------------------------------------------
from datetime import timedelta
import time
import os
from numpy import mean, std
from math import sqrt
import pandas as pd

#--------------------------------------------------------------------------
def get_association_time_txt (file_name):
    """Get the association time from a txt file"""
    with open (file_name) as file_obj:
        line_list = file_obj.readlines()
    
    t = int(line_list[0])/1000

    if len(line_list) != 1:
        e = int(line_list[1])
    else: e = 0
    return t, e

#---------------------------------------------------------------------------
def ms_to_str (ms):
    """To convert a milisecond integer into a timestamp string"""
    milis_str = str(round(ms%1000))
    string_time = str(timedelta(seconds=(ms - ms%1000)/1000)) + '.' + milis_str
    return string_time


#------------------------------------------------------------------------------
def average_association_time (folder_name):
    """Get the average association time of a list of sample files"""

    i = 1

    time_list = []
    EB_list = []

    while os.path.isfile('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/' + folder_name + '/log_2_' + '{}.txt'.format(str(i))):
        a, b = get_association_time_txt('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/' + folder_name + '/' + 'log_2_'+ '{}.txt'.format(str(i)))
        time_list.append(a)
        EB_list.append(b)
        i+=1
    
    average_t = mean(time_list)
    average_e = mean(EB_list)

    #Standard Deviation
    time_std = std(time_list)
    
    m_error = error (average_t, time_std)

    #maxim = min(time_list)

    return average_t, m_error

#----------------------------------------------------------------------------------
def error (list_mean, list_std):
    """Calculate the error margin"""
    e = 1.96 * (list_std/(sqrt(1000)))
    p = (e/list_mean)* 100 
    return e

#----------------------------------------------------------------------------------
def rename_file ():

    i = 1
    while os.path.isfile('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/log_2_' + '{}.txt'.format(str(i))):
        os.rename('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/logs/log_2_' + '{}.txt'.format(str(i)) , '/home/mmmorfa/contiki-ng/examples/6tisch/simple-node/logs/log_2_' + '{}.txt'.format(str(i+457)))
        i+=1
