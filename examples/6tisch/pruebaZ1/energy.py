"""
Created on Sun Sep 19 11:05:27 20211

@author: mmmorfa
"""
#-----------------------------------------------------------------------------------
import os
from numpy import mean
from functions import *
#-----------------------------------------------------------------------------------
#INPUT_FILE = "COOJA.testlog"

# From Z1 node datasheet
CURRENT_MA = {
    "CPU" : 10,
    "LPM" : 0.023,
    "Deep LPM" : 0, # not used by Z1 nodes
    "Radio Rx" : 18.8,
    "Radio Tx" : 17.4,
}

STATES = list(CURRENT_MA.keys())

VOLTAGE = 3.0 # assume 3 volt batteries
RTIMER_ARCH_SECOND = 32768
#------------------------------------------------------------------------------------
def energy(INPUT_FILE):
    '''Return a dictionary with each node's consumption'''

    node_ticks = {}
    node_total_ticks = {}
    
    with open(INPUT_FILE, "r") as f:
        for line in f:
            if "INFO: Energest" not in line:
                continue
            fields = line.split()
            try:
                node = int(fields[1])
            except:
                continue

            if node not in node_ticks:
                # initialize to zero
                node_ticks[node] = { u : 0  for u in STATES }
                node_total_ticks[node] = 0

            try:
                state_index = 5
                state = fields[state_index]
                tick_index = state_index + 2
                if state not in STATES:
                    state = fields[state_index] + " " + fields[state_index+1]
                    tick_index += 1
                    if state not in STATES:
                        # add to the total time
                        if state == "Total time":
                            node_total_ticks[node] += int(fields[tick_index])
                        continue
                # add to the time spent in specific state
                ticks = int(fields[tick_index][:-1])
                node_ticks[node][state] += ticks
            except Exception as ex:
                print("Failed to process line '{}': {}".format(line, ex))

    nodes = sorted(node_ticks.keys())

    dict_energy = {}

    for node in nodes:
        total_avg_current_mA = 0
        period_ticks = node_total_ticks[node]
        period_seconds = period_ticks / RTIMER_ARCH_SECOND
        for state in STATES:
            ticks = node_ticks[node].get(state, 0)
            current_mA = CURRENT_MA[state]
            state_avg_current_mA = ticks * current_mA / period_ticks
            total_avg_current_mA += state_avg_current_mA
        total_charge_mC = period_ticks * total_avg_current_mA / RTIMER_ARCH_SECOND
        total_energy_mJ = total_charge_mC * VOLTAGE
        '''
        print("Node {}: {:.2f} mC ({:.3f} mAh) charge consumption, {:.2f} mJ energy consumption in {:.2f} seconds".format(
            node, total_charge_mC, total_charge_mC / 3600.0, total_energy_mJ, period_seconds))
        '''
        dict_energy[node] = total_energy_mJ

        #print("Energy Consumption: {:.2f}  mJ/s".format(total_energy_mJ/period_seconds))
        #return total_energy_mJ/period_seconds
    return dict_energy
#------------------------------------------------------------------------------------
def calculate_energy (folder):
    '''Return a dictionary with each node's consumption for every sample file'''
    i = 1

    dict_edict = {}

    while os.path.isfile('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/Testlogs/' + folder + '/COOJA_' + '{}.testlog'.format(str(i))):
        dict_edict [i] = energy ('/home/mmmorfa/contiki-ng/examples/6tisch/pruebaZ1/Testlogs/' + folder + '/COOJA_' + '{}.testlog'.format(str(i)))
        i+=1
    
    return dict_edict
#------------------------------------------------------------------------------------
def node_energy (folder, node_number):
    '''Return the consumption (in mJ) for a specific node'''
    a = calculate_energy(folder)
    node = []

    for i in range(1,len(a)+1):
        node.append(a.get(i).get(node_number))
    
    m = mean(node)
    e = error(m, std(node))
    return m, e
#-------------------------------------------------------------------------------------