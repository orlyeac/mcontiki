from functions import *
import matplotlib.pyplot as plt

#Data to plot
x = [0.05, 1, 2, 4, 8, 16]

#---------------------------------------------------------------------------
a1 = average_association_time ('EBP005_CSD01_CH16')
b1 = average_association_time ('EBP1_CSD01_CH16')
c1 = average_association_time ('EBP2_CSD01_CH16')
d1 = average_association_time ('EBP4_CSD01_CH16')
e1 = average_association_time ('EBP8_CSD01_CH16')
f1 = average_association_time ('EBP16_CSD01_CH16')

y1 = [a1[0], b1[0], c1[0], d1[0], e1[0], f1[0]]

ymax1 = [a1[2], b1[2], c1[2], d1[2], e1[2], f1[2]]

bar_labels1 = [ms_to_str(a1[0]), ms_to_str(b1[0]), ms_to_str(c1[0]), ms_to_str(d1[0]), ms_to_str(e1[0]), ms_to_str(f1[0])]
max_labels1 = [ms_to_str(a1[2]), ms_to_str(b1[2]), ms_to_str(c1[2]), ms_to_str(d1[2]), ms_to_str(e1[2]), ms_to_str(f1[2])]

error_margin1 = [a1[1], b1[1], c1[1], d1[1], e1[1], f1[1]]
print ('CSD:0.1')
print (error_margin1)

#----------------------------------------------------------------------------
a2 = average_association_time ('EBP005_CSD1_CH16')
b2 = average_association_time ('EBP1_CSD1_CH16')
c2 = average_association_time ('EBP2_CSD1_CH16')
d2 = average_association_time ('EBP4_CSD1_CH16')
e2 = average_association_time ('EBP8_CSD1_CH16')
f2 = average_association_time ('EBP16_CSD1_CH16')

y2 = [a2[0], b2[0], c2[0], d2[0], e2[0], f2[0]]

ymax2 = [a2[2], b2[2], c2[2], d2[2], e2[2], f2[2]]

bar_labels2 = [ms_to_str(a2[0]), ms_to_str(b2[0]), ms_to_str(c2[0]), ms_to_str(d2[0]), ms_to_str(e2[0]), ms_to_str(f2[0])]
max_labels2 = [ms_to_str(a2[2]), ms_to_str(b2[2]), ms_to_str(c2[2]), ms_to_str(d2[2]), ms_to_str(e2[2]), ms_to_str(f2[2])]

error_margin2 = [a2[1], b2[1], c2[1], d2[1], e2[1], f2[1]]
print ('CSD:1')
print (error_margin2)

#----------------------------------------------------------------------------
a3 = average_association_time ('EBP005_CSD5_CH16')
b3 = average_association_time ('EBP1_CSD5_CH16')
c3 = average_association_time ('EBP2_CSD5_CH16')
d3 = average_association_time ('EBP4_CSD5_CH16')
e3 = average_association_time ('EBP8_CSD5_CH16')
f3 = average_association_time ('EBP16_CSD5_CH16')

y3 = [a3[0], b3[0], c3[0], d3[0], e3[0], f3[0]]

ymax3 = [a3[2], b3[2], c3[2], d3[2], e3[2], f3[2]]

bar_labels3 = [ms_to_str(a3[0]), ms_to_str(b3[0]), ms_to_str(c3[0]), ms_to_str(d3[0]), ms_to_str(e3[0]), ms_to_str(f3[0])]
max_labels3 = [ms_to_str(a3[2]), ms_to_str(b3[2]), ms_to_str(c3[2]), ms_to_str(d3[2]), ms_to_str(e3[2]), ms_to_str(f3[2])]

error_margin3 = [a3[1], b3[1], c3[1], d3[1], e3[1], f3[1]]
print ('CSD:5')
print (error_margin3)

#----------------------------------------------------------------------------
a4 = average_association_time ('EBP005_CSD25_CH16')
b4 = average_association_time ('EBP1_CSD25_CH16')
c4 = average_association_time ('EBP2_CSD25_CH16')
d4 = average_association_time ('EBP4_CSD25_CH16')
e4 = average_association_time ('EBP8_CSD25_CH16')
f4 = average_association_time ('EBP16_CSD25_CH16')

y4 = [a4[0], b4[0], c4[0], d4[0], e4[0], f4[0]]

ymax4 = [a4[2], b4[2], c4[2], d4[2], e4[2], f4[2]]

bar_labels4 = [ms_to_str(a4[0]), ms_to_str(b4[0]), ms_to_str(c4[0]), ms_to_str(d4[0]), ms_to_str(e4[0]), ms_to_str(f4[0])]
max_labels4 = [ms_to_str(a4[2]), ms_to_str(b4[2]), ms_to_str(c4[2]), ms_to_str(d4[2]), ms_to_str(e4[2]), ms_to_str(f4[2])]

error_margin4 = [a4[1], b4[1], c4[1], d4[1], e4[1], f4[1]]
print ('CSD:25')
print (error_margin4)

#----------------------------------------------------------------------------
#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

fig, ax = plt.subplots()

#Plotting the points
plt.plot(x, ymax1, color='blue', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='blue', markersize=5, label='Tscan = 0.1 s') 
plt.plot(x, ymax2, color='red', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='red', markersize=5, label='Tscan = 1 s')
plt.plot(x, ymax3, color='green', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='green', markersize=5, label='Tscan = 5 s')
plt.plot(x, ymax4, color='orange', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='orange', markersize=5, label='Tscan = 25 s')
'''
plt.scatter (x, ymax1, color='blue')
plt.scatter (x, ymax2, color='red')
plt.scatter (x, ymax3, color='green')
plt.scatter (x, ymax4, color='orange')
'''
# setting x and y axis range 
plt.ylim(0,1000) 
#plt.xlim(1,8) 
#plt.axis([0,16,0,200000])
  
# naming the x axis 
plt.xlabel('EB Period (s)') 
# naming the y axis 
plt.ylabel('Association Time (ms)') 
  
# giving a title to my graph 
plt.title('MIN---TSCH Association Time (16 Channels)') 

#Create labels on the coordenates.
for i in range(len(x)):
    plt.text( x= x[i] - 1, y= ymax1[i]+3000, s= max_labels1[i], size= 8, color= 'b')
    plt.text( x= x[i] + 0.1, y= ymax2[i]-3000, s= max_labels2[i], size= 8, color= 'r')
    plt.text( x= x[i] - 1, y= ymax3[i]+20000, s= max_labels3[i], size= 8, color= 'g')
    plt.text( x= x[i] + 0.1, y= ymax4[i]-20000, s= max_labels4[i], size= 8, color= 'orange')
'''
    plt.text( x= x[i] +0.5, y= ymax1[i], s= max_labels1[i], size= 8, color= 'b')
    plt.text( x= x[i] +0.5, y= ymax2[i], s= max_labels2[i], size= 8, color= 'r')
    plt.text( x= x[i] +0.5, y= ymax3[i], s= max_labels3[i], size= 8, color= 'g')
    plt.text( x= x[i] +0.5, y= ymax4[i], s= max_labels4[i], size= 8, color= 'orange')
'''

# function to show the plot 
plt.legend()
plt.tight_layout()
plt.show() 