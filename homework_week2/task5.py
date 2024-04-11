def find(spaces, stat, n):
    available=[]
# your code here
#    print(len(spaces))#6
#    print(len(stat))#6
#    for item1 in spaces:
#        print(spaces[spaces.index(item1)])#3,1,5,4,3,2
    #print(spaces[0])#3
    #print(spaces)
    #print(stat)

    for i in range(0,len(spaces)):
        if stat[i]==1 and spaces[i]>=n:
            available.append(spaces[i])
        else:
            result=-1
    #print(available)#[4, 3, 2]
    if available:
        result=min(available)#2
        print(spaces.index(result))
    else:
        print(result)

    
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
#print('***')
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
