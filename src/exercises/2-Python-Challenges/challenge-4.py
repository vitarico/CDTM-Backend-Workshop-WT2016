import random

list = [random.randint(1,100) for i in xrange(10)]

for i in range(list.__len__()):
    print list[i]
print " "


sorted= False
while sorted == False:
    for i in range(list.__len__()-1):
        sorted = True
        if list[i] < list[i+1] :
            sorted = False
            list[i], list[i+1] = list[i+1], list[i]
    for i in range(list.__len__()):
        print list[i]
    print " "