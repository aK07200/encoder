import numpy as np
import matplotlib.pyplot as plt

msg = input("\nВведите входящее сообщение (без пробелов): ")

y1 = [] #входящее
for i in range(-1, len(msg)):
    if (i < 0):
        y1.append(int(msg[0]))
    elif (msg[i] == '0'):
        y1.append(0)
    elif (msg[i] == '1'):
        y1.append(1)

y2 = [] #g e thomas
for i in range(-1, len(msg)):
    if (i < 0):
        y2.append(int(msg[0]))
    elif (msg[i] == '0'):
        y2.append(0)
        y2.append(1)
    elif (msg[i] == '1'):
        y2.append(1)
        y2.append(0)

y3 = [] #ieee 802.3
for i in range(0, len(y2)):
    if (y2[i] == 0):
        y3.append(1)
    elif (y2[i] == 1):
        y3.append(0)

y4 = [] #ami
isSecond=bool(0)
for i in range(0, len(y1)):
    if (y1[i] == 0):
        y4.append(0)
    elif (y1[i] == 1 and isSecond == bool(1)):
        y4.append(-1)
        isSecond = bool(0)
    elif (y1[i] == 1 and isSecond == bool(0)):
        y4.append(1)
        isSecond = bool(1)

y5 = [] #nrzi
curr = y1[0]
for i in range(0, len(y1)):
    if (y1[i] == 0):
        y5.append(curr)
    elif (y1[i] == 1 and curr == 1):
        y5.append(0)
        curr=0
    elif (y1[i] == 1 and curr == 0):
        y5.append(1)
        curr=1

y6 = [] #rz
for i in range(0, len(y2)):
    if (y2[i] == 0):
        y6.append(1)
        y6.append(0)
    elif (y2[i] == 1):
        y6.append(-1)
        y6.append(0)

y_st = y1
y8 = []
if (len(y_st) % 2 == 1):
        y_st.append(0)
for i in range(0, int(len(y_st)/2)):
    if (y_st[2*i-1] == 0 and y_st[2*i] == 0):
        y8.append(0)
    elif (y_st[2*i-1] == 0 and y_st[2*i] == 1):
        y8.append(1)
    elif (y_st[2*i-1] == 1 and y_st[2*i] == 0): 
        y8.append(2)
    elif (y_st[2*i-1] == 1 and y_st[2*i] == 1):
        y8.append(3)

plt.subplot(7, 1, 1)
plt.plot(y1, drawstyle='steps')
plt.title('Default')
plt.grid(axis = 'x')

plt.subplot(7, 1, 2)
plt.plot(y2, drawstyle='steps')
plt.title('Manchester G.E.Thomas')
plt.grid(axis = 'x')

plt.subplot(7, 1, 3)
plt.plot(y3, drawstyle='steps')
plt.title('Manchester IEEE 802.3')
plt.grid(axis = 'x')

plt.subplot(7, 1, 4)
plt.plot(y4, drawstyle='steps')
plt.title('AMI')
plt.grid(axis = 'x')

plt.subplot(7, 1, 5)
plt.plot(y5, drawstyle='steps')
plt.title('NRZI')
plt.grid(axis = 'x')

plt.subplot(7, 1, 6)
plt.plot(y6, drawstyle='steps')
plt.title('RZ')
plt.grid(axis = 'x')

plt.subplot(7, 1, 7)
plt.plot(y8, drawstyle='steps')
plt.title('PAM-5')
plt.grid(axis = 'x')

plt.suptitle('message = ' + msg)
plt.subplots_adjust(hspace=1)
plt.show()
