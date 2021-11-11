from functions import *
import matplotlib.pyplot as plt

#Data to plot
x = [1, 2, 3, 4]

#------------------------------------------------------------------------------------------
tA1, eA1 = average_association_time ('EBP16_CSD1_CH16')
tB1, eB1 = average_association_time ('EBP16_CSD1_CH16_L3')
tC1, eC1 = average_association_time ('EBP16_CSD1_CH16_L4')
tD1, eD1 = average_association_time ('EBP16_CSD1_CH16_L5')

yt1 = list(map(lambda x: x/1000, [tA1, tB1, tC1, tD1]))
ye1 = list(map(lambda x: x/1000, [eA1, eB1, eC1, eD1]))

#-------------------------------------------------------------------------------------------
tA2, eA2 = average_association_time ('N1_8.16_CSD1_CH16')
tB2, eB2 = average_association_time ('N1_8.16_CSD1_CH16_L3')
tC2, eC2 = average_association_time ('N1_8.16_CSD1_CH16_L4')
tD2, eD2 = average_association_time ('N1_8.16_CSD1_CH16_L5')

yt2 = list(map(lambda x: x/1000, [tA2, tB2, tC2, tD2]))
ye2 = list(map(lambda x: x/1000, [eA2, eB2, eC2, eD2]))

#--------------------------------------------------------------------------------------------
tA3, eA3 = average_association_time ('N18_8.16_CSD1_CH16')
tB3, eB3 = average_association_time ('N18_8.16_CSD1_CH16_L3')
tC3, eC3 = average_association_time ('N18_8.16_CSD1_CH16_L4')
tD3, eD3 = average_association_time ('N18_8.16_CSD1_CH16_L5')

yt3 = list(map(lambda x: x/1000, [tA3, tB3, tC3, tD3]))
ye3 = list(map(lambda x: x/1000, [eA3, eB3, eC3, eD3]))

#--------------------------------------------------------------------------------------------

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

# naming the x axis 
plt.xlabel('Number of Hop') 
# naming the y axis 
plt.ylabel('Association Time (s)')

# giving a title to my graph 
plt.title('TSCH Association Time -- Linear Topology  [Channels (n) = 16]')

plt.errorbar(x, yt1, yerr=ye1, color='blue', fmt='--o', label='Fixed EB Period', capsize=3)
plt.errorbar(x, yt2, yerr=ye2, color='red', fmt='--o', label='1/2 EB Period for 1*n EBs', capsize=3)
plt.errorbar(x, yt3, yerr=ye3, color= 'green', fmt='--o', label='1/2 EB Period for 1.8*n EBs', capsize=3)

plt.xticks(x, x)

# function to show the plot 
plt.legend()
plt.tight_layout()
plt.grid(b=True, which='major', color='#666666', linestyle=':')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle=':', alpha=0.2)

plt.show() 