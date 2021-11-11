import matplotlib
from numpy.core.fromnumeric import size
from functions import *
import matplotlib.pyplot as plt
#import numpy as np
#from scipy.interpolate import make_interp_spline

#Data to plot
#x = np.array([0.5, 0.8, 1, 1.5, 1.8])
x = [0.5, 0.75, 1]

#------------------------------------------------------------------------------------------
tA1, eA1 = average_association_time ('Z1_EBP4_CH4_R2_50%')
tB1, eB1 = average_association_time ('Z1_EBP4_CH4_R2_75%')
tC1, eC1 = average_association_time ('Z1_EBP4_CH4_R2')


yt1 = list(map(lambda x: x/1000, [tA1, tB1, tC1]))
ye1 = list(map(lambda x: x/1000, [eA1, eB1, eC1]))

#X_Y_Spline1 = make_interp_spline(x, yt1)
#X_1 = np.linspace(x.min(), x.max(), 500)
#Y_1 = X_Y_Spline1(X_1)

#--------------------------------------------------------------------------------------------
tA2, eA2 = average_association_time ('Z1_0.8_CH4_2-4_R2_50%')
tB2, eB2 = average_association_time ('Z1_0.8_CH4_2-4_R2_75%')
tC2, eC2 = average_association_time ('Z1_0.8_CH4_2-4_R2')


yt2 = list(map(lambda x: x/1000, [tA2, tB2, tC2]))
ye2 = list(map(lambda x: x/1000, [eA2, eB2, eC2]))

#X_Y_Spline2 = make_interp_spline(x, yt2)
#X_2 = np.linspace(x.min(), x.max(), 500)
#Y_2 = X_Y_Spline2(X_2)

#--------------------------------------------------------------------------------------------
tA3, eA3 = average_association_time ('Z1_1.8_CH4_2-4_R2_50%')
tB3, eB3 = average_association_time ('Z1_1.8_CH4_2-4_R2_75%')
tC3, eC3 = average_association_time ('Z1_1.8_CH4_2-4_R2')


yt3 = list(map(lambda x: x/1000, [tA3, tB3, tC3]))
ye3 = list(map(lambda x: x/1000, [eA3, eB3, eC3]))

#X_Y_Spline3 = make_interp_spline(x, yt3)
#X_3 = np.linspace(x.min(), x.max(), 500)
#Y_3 = X_Y_Spline3(X_3)

#--------------------------------------------------------------------------------------------
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

plt.rcParams['font.size'] = '16'

# naming the x axis 
plt.xlabel('Calidad del enlace') 
# naming the y axis 
plt.ylabel('Tiempo de Asociación (s)')

# giving a title to my graph 
#plt.title('Tiempo de Asociación TSCH (Escenario Par Coordinador-Joinseeker)')

plt.errorbar(x, yt1, yerr=ye1, color='blue', fmt='--o', label='minimal 6TiSCH', capsize=3)
plt.errorbar(x, yt2, yerr=ye2, color='red', fmt='--D', label='TDEB-TSCH con beta = 0.8', capsize=3)
plt.errorbar(x, yt3, yerr=ye3, color='green', fmt='--^', label='TDEB-TSCH con beta = 1.8', capsize=3)

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