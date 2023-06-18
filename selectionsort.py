import time

def Selection_Sort(data,drawData,timeTick):
    for i in range(len(data)-1):
        min=i
        for j in range(i+1,len(data)):
            if(data[min]>data[j]):
                min=j
            drawData(data,['yellow' if x==j or x==j+1 else '#A90042' for x in range(len(data))])
            time.sleep(timeTick)
        if(min!=i):
            data[i],data[min]=data[min],data[i]

    


    



