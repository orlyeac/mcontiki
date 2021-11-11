from functions import *
import matplotlib.pyplot as plt

#Data to plot
x = [0.5, 0.8, 1, 1.4, 1.8]

#------------------------------------------------------------------------------------------
tA1, eA1 = average_association_time ('N05_8.16_CSD1_CH4')
tB1, eB1 = average_association_time ('N08_8.16_CSD1_CH4')
tC1, eC1 = average_association_time ('N1_8.16_CSD1_CH4')
tD1, eD1 = average_association_time ('N14_8.16_CSD1_CH4')
tE1, eE1 = average_association_time ('N18_8.16_CSD1_CH4')

u1, m = average_association_time ('EBP16_CSD1_CH4')
#print (u1)

yt1 = [tA1, tB1, tC1, tD1, tE1]
ye1 = [eA1, eB1, eC1, eD1, eE1]

labels1 = [ms_to_str(tA1), ms_to_str(tB1), ms_to_str(tC1), ms_to_str(tD1), ms_to_str(tE1)]
#-------------------------------------------------------------------------------------------
tA2, eA2 = average_association_time ('N05_8.16_CSD1_CH16')
tB2, eB2 = average_association_time ('N08_8.16_CSD1_CH16')
tC2, eC2 = average_association_time ('N1_8.16_CSD1_CH16')
tD2, eD2 = average_association_time ('N14_8.16_CSD1_CH16')
tE2, eE2 = average_association_time ('N18_8.16_CSD1_CH16')

u2, n = average_association_time ('EBP16_CSD1_CH16')
#print (u2)

yt2 = [tA2, tB2, tC2, tD2, tE2]
ye2 = [eA2, eB2, eC2, eD2, eE2]

labels2 = [ms_to_str(tA2), ms_to_str(tB2), ms_to_str(tC2), ms_to_str(tD2), ms_to_str(tE2)]
#--------------------------------------------------------------------------------------------

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

plt.plot(x, yt1, color='blue', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='blue', markersize=5, label='4 Channels')
plt.plot(x, yt2, color='red', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='red', markersize=5, label='16 Channels')
plt.axhline(y=u1, color='blue')
plt.axhline(y=u2, color='red')

# naming the x axis 
plt.xlabel('Number(n * Channels) of Beacons with fast EB Period ') 
# naming the y axis 
plt.ylabel('Association Time (ms)')

# giving a title to my graph 
plt.title('TSCH Association Time')

#Create labels on the coordenates.
for i in range(len(x)):
    plt.text( x= x[i] - 0.05, y= yt1[i]+3000, s= labels1[i], size= 8, color= 'b')
    plt.text( x= x[i] - 0.05, y= yt2[i]+3000, s= labels2[i], size= 8, color= 'r')
    plt.text( x= 1.1, y= u1 + 1000, s= ms_to_str(u1), size= 8, color= 'b')
    plt.text( x= 1.1, y= u2 + 1000, s= ms_to_str(u2), size= 8, color= 'r')

# function to show the plot 
plt.legend()
plt.tight_layout()
plt.show() 

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

plt.plot(x, ye1, color='blue', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='blue', markersize=5, label='4 Channels')
plt.plot(x, ye2, color='red', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='red', markersize=5, label='16 Channels')

# naming the x axis 
plt.xlabel('Number(n * Channels) of Beacons with fast EB Period ') 
# naming the y axis 
plt.ylabel('Number of EBs to associate')

# giving a title to my graph 
plt.title('TSCH')

#Create labels on the coordenates.
for i in range(len(x)):
    plt.text( x= x[i] - 0.05, y= ye1[i]+0.1, s= ye1[i], size= 8, color= 'b')
    plt.text( x= x[i] - 0.05, y= ye2[i]+0.1, s= ye2[i], size= 8, color= 'r')


# function to show the plot 
plt.legend()
plt.tight_layout()
plt.show() 