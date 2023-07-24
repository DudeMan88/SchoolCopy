import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


def readascii_ben(file,startline=0,endline = 10**100):
    with open(file) as f:
        year = []
        month = []
        day = []
        hour = []
        minute = []
        second = []
        AE = []
        AL = []
        AU = []
        time = []
        onsets=[]
        index = 0
        for line in f:
            index += 1
            if index > startline and index < endline:
                temp = line.split()
                hr = int(temp[3])
                dy = int(temp[2])
                if hr == 24:
                    hr = 0
                    dy+= 1
                year.append(int(temp[0]))
                month.append(int(temp[1]))
                day.append(dy)
                hour.append(hr)
                minute.append(int(temp[4]))
                second.append(int(temp[5]))
                AE.append(int(temp[6]))
                AL.append(int(temp[7]))
                AU.append(int(temp[8]))
                time.append(dt.datetime(int(temp[0]),int(temp[1]),int(dy),hour = int(hr),minute=int(temp[4]),second=int(temp[5])))
            elif index > endline:
                break
            else: 
                continue
        index = 0
        npts=len(AL)
        while index < npts-30:
            x=AL[index]
            if AL[index+1] - x  < -15: ### 4 conditions for storm onset ###
                # print('here:',index)
                if AL[index+2] - x  < -30:
                    if AL[index+3] - x  < -45:
                        s = sum(AL[index+4:index+30])/26
                        # print(s,x)
                        if (s- x  < -100):
                            onsets.append(index)
                            index += 29
                            # print(onsets)

            # if index + 31 > len(AL):
            #     # raise "No onset"
            #     break
            index +=1 
        lists = {"year" : year,
        'month':month,
        'day' : day,
        'hour' : hour,
        'minute' : minute,
        'second' : second,
        'AE' : AE,
        'AL' : AL,
        'AU' : AU,
        'time' : time,
        'onsets' : onsets}
        return lists


### ASSIGNMENT 1 kind of###

# data = readascii_ben("sme_2013.txt",startline=106, endline=100000)
# # time = [str(dt.time(hour = x.hour,minute=x.minute,second=x.second)) for x in data['time']]
# for x in range(len(data['onsets'])):    
#     index = 0
#     yValues = []
#     xValues = []
#     onset = data['onsets'][x]-2
#     while (data['time'][onset+index].hour*60)+data['time'][onset+index].minute <= (data['time'][onset].hour*60) + data['time'][onset].minute + 30:
#         yValues.append(data['AL'][onset+index])
#         xValues.append(data['time'][onset+index])
#         index+=1
#         if index+onset >= len(data['time']):
#             break
#     xValues = np.array(xValues);yValues = np.array(yValues)
#     plt.ylabel('AL value')
#     plt.xlabel('Time of day in month '+ str(data['month'][onset])+' (dd:hh:mm)')
#     plt.plot(xValues,yValues)
#     plt.show()

        
### ASSIGNMENT 2 ###
        
# data = readascii_ben('sme_2013.txt',startline=106)
# ind = data['month'].index(2)
# for x in data['onsets']:
#     if x > ind:
#         y = data['onsets'].index(x)
#         del data['onsets'][y:]
#         break
# del data['month'][ind:]
# print([data['time'][x] for x in data['onsets']])


### ASSIGNMENT 3 ###

data = readascii_ben('sme_2013.txt',startline=106)
minimums = []
for x in range(len(data['onsets'])):    
    index = 0
    yValues = []
    xValues = []
    onset = data['onsets'][x]-2
    while (data['time'][onset+index].hour*60)+data['time'][onset+index].minute <= (data['time'][onset].hour*60) + data['time'][onset].minute + 30:
        yValues.append(data['AL'][onset+index])
        index+=1
        if index+onset >= len(data['time']):
            break
    minimums.append(min(yValues))
    
plt.hist(minimums,range=(-2200,-200),bins = 80)
plt.show()



























        
        
        
        
        
        
        