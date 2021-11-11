import matplotlib
from numpy.core.fromnumeric import size
from functions import *
import matplotlib.pyplot as plt
#import numpy as np
#from scipy.interpolate import make_interp_spline

#Data to plot
#x = np.array([0.5, 0.8, 1, 1.5, 1.8])
x = [0.5, 0.8, 1.0, 1.5, 1.8]

#------------------------------------------------------------------------------------------
tA1, eA1 = average_association_time ('Z1_0.5_CH4_2-4_P')
tB1, eB1 = average_association_time ('Z1_0.8_CH4_2-4_P')
tC1, eC1 = average_association_time ('Z1_1.0_CH4_2-4_P')
tD1, eD1 = average_association_time ('Z1_1.5_CH4_2-4_P')
tE1, eE1 = average_association_time ('Z1_1.8_CH4_2-4_P')

yt1 = list(map(lambda x: x/1000, [tA1, tB1, tC1, tD1, tE1]))
ye1 = list(map(lambda x: x/1000, [eA1, eB1, eC1, eD1, eE1]))

#X_Y_Spline1 = make_interp_spline(x, yt1)
#X_1 = np.linspace(x.min(), x.max(), 500)
#Y_1 = X_Y_Spline1(X_1)

#--------------------------------------------------------------------------------------------
tA2, eA2 = average_association_time ('Z1_0.5_CH8_2-4_P')
tB2, eB2 = average_association_time ('Z1_0.8_CH8_2-4_P')
tC2, eC2 = average_association_time ('Z1_1.0_CH8_2-4_P')
tD2, eD2 = average_association_time ('Z1_1.5_CH8_2-4_P')
tE2, eE2 = average_association_time ('Z1_1.8_CH8_2-4_P')

yt2 = list(map(lambda x: x/1000, [tA2, tB2, tC2, tD2, tE2]))
ye2 = list(map(lambda x: x/1000, [eA2, eB2, eC2, eD2, eE2]))

#X_Y_Spline2 = make_interp_spline(x, yt2)
#X_2 = np.linspace(x.min(), x.max(), 500)
#Y_2 = X_Y_Spline2(X_2)

#--------------------------------------------------------------------------------------------
tA3, eA3 = average_association_time ('Z1_0.5_CH16_2-4_P')
tB3, eB3 = average_association_time ('Z1_0.8_CH16_2-4_P')
tC3, eC3 = average_association_time ('Z1_1.0_CH16_2-4_P')
tD3, eD3 = average_association_time ('Z1_1.5_CH16_2-4_P')
tE3, eE3 = average_association_time ('Z1_1.8_CH16_2-4_P')

yt3 = list(map(lambda x: x/1000, [tA3, tB3, tC3, tD3, tE3]))
ye3 = list(map(lambda x: x/1000, [eA3, eB3, eC3, eD3, eE3]))

#X_Y_Spline3 = make_interp_spline(x, yt3)
#X_3 = np.linspace(x.min(), x.max(), 500)
#Y_3 = X_Y_Spline3(X_3)

#--------------------------------------------------------------------------------------------
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

plt.rcParams['font.size'] = '16'

# naming the x axis 
plt.xlabel('Factor beta de fase intensiva de envío de EBs') 
# naming the y axis 
plt.ylabel('Tiempo de Asociación (s)')

# giving a title to my graph 
#plt.title('Tiempo de Asociación TSCH (Escenario Par Coordinador-Joinseeker)')

plt.errorbar(x, yt1, yerr=ye1, color='blue', fmt='--o', label='4 Canales', capsize=3)
plt.errorbar(x, yt2, yerr=ye2, color='red', fmt='--D', label='8 Canales', capsize=3)
plt.errorbar(x, yt3, yerr=ye3, color='green', fmt='--^', label='16 Canales', capsize=3)

#plt.plot(X_1, Y_1)
#plt.plot(X_2, Y_2)
#plt.plot(X_3, Y_3)

plt.xticks(x, x)

# function to show the plot 
plt.legend()
plt.tight_layout()
plt.grid(b=True, which='major', color='#666666', linestyle=':')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle=':', alpha=0.2)


plt.show() 