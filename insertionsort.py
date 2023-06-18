import time

def Insertion_Sort(data,drawData,timeTick):
    for j in range(1,len(data)):
        key=data[j]
        i=j-1
        while(i>=0 and key<data[i]):
            data[i+1]=data[i]
            i=i-1
            drawData(data,['yellow' if x==j or x==j+1 else '#A90042' for x in range(len(data))])
            time.sleep(timeTick)

        data[i+1]=key
    



