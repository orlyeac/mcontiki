from functions import *
import matplotlib.pyplot as plt

#Data to plot
x = [0.05, 1, 2, 4, 8, 16]

#---------------------------------------------------------------------------
a1 = average_association_time ('EBP005_CSD1_CH16')
b1 = average_association_time ('EBP1_CSD1_CH16')
c1 = average_association_time ('EBP2_CSD1_CH16')
d1 = average_association_time ('EBP4_CSD1_CH16')
e1 = average_association_time ('EBP8_CSD1_CH16')
f1 = average_association_time ('EBP16_CSD1_CH16')

y1 = [a1[0], b1[0], c1[0], d1[0], e1[0], f1[0]]

bar_labels1 = [ms_to_str(a1[0]), ms_to_str(b1[0]), ms_to_str(c1[0]), ms_to_str(d1[0]), ms_to_str(e1[0]), ms_to_str(f1[0])]
#----------------------------------------------------------------------------
a2 = average_association_time ('EBP005_CSD1_CH4')
b2 = average_association_time ('EBP1_CSD1_CH4')
c2 = average_association_time ('EBP2_CSD1_CH4')
d2 = average_association_time ('EBP4_CSD1_CH4')
e2 = average_association_time ('EBP8_CSD1_CH4')
f2 = average_association_time ('EBP16_CSD1_CH4')

y2 = [a2[0], b2[0], c2[0], d2[0], e2[0], f2[0]]

bar_labels2 = [ms_to_str(a2[0]), ms_to_str(b2[0]), ms_to_str(c2[0]), ms_to_str(d2[0]), ms_to_str(e2[0]), ms_to_str(f2[0])]
#----------------------------------------------------------------------------

#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

fig, ax = plt.subplots()

#Plotting the points
plt.plot(x, y1, color='blue', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='blue', markersize=5, label='16 Channels') 
plt.plot(x, y2, color='red', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='red', markersize=5, label='4 Channels')

# setting x and y axis range 
plt.ylim(0,300000) 
#plt.xlim(1,8) 
#plt.axis([0,16,0,200000])
  
# naming the x axis 
plt.xlabel('EB Period (s)') 
# naming the y axis 
plt.ylabel('Association Time (ms)') 
  
# giving a title to my graph 
plt.title('TSCH Association Time (Tscan = 1 s)') 

#Create labels on the coordenates.
for i in range(len(x)):
    plt.text( x= x[i] - 1, y= y1[i]+3000, s= bar_labels1[i], size= 8, color= 'b')
    plt.text( x= x[i] + 0.1, y= y2[i]-3000, s= bar_labels2[i], size= 8, color= 'r')

# function to show the plot 
plt.legend()
plt.tight_layout()
plt.show() 