from functions import *
import matplotlib.pyplot as plt

#Data to plot
x = [2, 4, 8, 16]

#------------------------------------------------------------------------------------------
tA1, eA1 = average_association_time ('EBP16_CSD1_CH2')
tB1, eB1 = average_association_time ('EBP16_CSD1_CH4')
tC1, eC1 = average_association_time ('EBP16_CSD1_CH8')
tD1, eD1 = average_association_time ('EBP16_CSD1_CH16')

yt1 = [tA1, tB1, tC1, tD1]
ye1 = [eA1, eB1, eC1, eD1]

labels1 = [ms_to_str(tA1), ms_to_str(tB1), ms_to_str(tC1), ms_to_str(tD1)]
#-------------------------------------------------------------------------------------------
tA2, eA2 = average_association_time ('EBP16_CSD1_CH2')
tB2, eB2 = average_association_time ('N08_8.16_CSD1_CH4')
tC2, eC2 = average_association_time ('N08_8.16_CSD1_CH8')
tD2, eD2 = average_association_time ('N08_8.16_CSD1_CH16')

yt2 = [tA2, tB2, tC2, tD2]
ye2 = [eA2, eB2, eC2, eD2]

labels2 = [ms_to_str(tA2), ms_to_str(tB2), ms_to_str(tC2), ms_to_str(tD2)]
#--------------------------------------------------------------------------------------------
tA3, eA3 = average_association_time ('N1_8.16_CSD1_CH2')
tB3, eB3 = average_association_time ('N1_8.16_CSD1_CH4')
tC3, eC3 = average_association_time ('N1_8.16_CSD1_CH8')
tD3, eD3 = average_association_time ('N1_8.16_CSD1_CH16')

yt3 = [tA3, tB3, tC3, tD3]
ye3 = [eA3, eB3, eC3, eD3]

labels3 = [ms_to_str(tA3), ms_to_str(tB3), ms_to_str(tC3), ms_to_str(tD3)]
#--------------------------------------------------------------------------------------------
tA4, eA4 = average_association_time ('N18_8.16_CSD1_CH2')
tB4, eB4 = average_association_time ('N18_8.16_CSD1_CH4')
tC4, eC4 = average_association_time ('N18_8.16_CSD1_CH8')
tD4, eD4 = average_association_time ('N18_8.16_CSD1_CH16')

yt4 = [tA4, tB4, tC4, tD4]
ye4 = [eA4, eB4, eC4, eD4]

labels4 = [ms_to_str(tA4), ms_to_str(tB4), ms_to_str(tC4), ms_to_str(tD4)]
#--------------------------------------------------------------------------------------------

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
'''
plt.plot(x, yt1, color='blue', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='blue', markersize=3, label='Fixed EB Period')
plt.plot(x, yt2, color='red', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='red', markersize=3, label='1/2 EB Period for 0.8*n EBs')
plt.plot(x, yt3, color='green', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='green', markersize=3, label='1/2 EB Period for 1*n EBs')
plt.plot(x, yt4, color='orange', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='orange', markersize=3, label='1/2 EB Period for 1.8*n EBs')
'''
# naming the x axis 
plt.xlabel('Number of Channels (n)') 
# naming the y axis 
plt.ylabel('Association Time (ms)')

# giving a title to my graph 
plt.title('TSCH Association Time')

plt.errorbar(x, yt1, yerr=ye1, color='blue', fmt='--o', label='Fixed EB Period', capsize=3)
plt.errorbar(x, yt2, yerr=ye2, color='red', fmt='--o', label='1/2 EB Period for 0.8*n EBs', capsize=3)
plt.errorbar(x, yt3, yerr=ye3, color= 'green', fmt='--o', label='1/2 EB Period for 1*n EBs', capsize=3)
plt.errorbar(x, yt4, yerr=ye4, color='orange', fmt='--o', label='1/2 EB Period for 1.8*n EBs', capsize=3)

'''
#Create labels on the coordenates.
for i in range(len(x)):
    plt.text( x= x[i] - 0.3, y= yt1[i]+5000, s= labels1[i], size= 8, color= 'b')
    plt.text( x= x[i] + 0.3, y= yt2[i]+5000, s= labels2[i], size= 8, color= 'r')
    plt.text( x= x[i] - 0.3, y= yt3[i]+5000, s= labels3[i], size= 8, color= 'g')
    plt.text( x= x[i] + 0.3, y= yt4[i]+5000, s= labels4[i], size= 8, color= 'orange')
'''
# function to show the plot 
plt.legend()
plt.tight_layout()
plt.grid(b=True, which='major', color='#666666', linestyle=':')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle=':', alpha=0.2)

plt.show() 