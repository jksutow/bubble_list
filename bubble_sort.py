import random
import time
def bubbleSort(bub_list):
    exchanges = True
    passnum = len(bub_list)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if bub_list[i]>bub_list[i+1]:
                exchanges = True
                temp = bub_list[i]
                bub_list[i] = bub_list[i+1]
                bub_list[i+1]=temp
        passnum = passnum-1
bub_list = []
for i in range(100):
    bub_list.append(int(round(random.random() * 10000)))

start = time.clock()
bubbleSort(bub_list)
end = time.clock()

print "Here is the sorted list:", bub_list
print "It took:", (end - start), "to sort through the list."
