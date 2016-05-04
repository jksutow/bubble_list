import random
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

bubbleSort(bub_list)
print bub_list
