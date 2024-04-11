def get_number(index):
# your code here
# 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25
    if index%3==0:
        times=int(index/3)
        result=(4+4-1)*times
        print(result)

    elif index%3==1:
        times=int(index/3)
        result=(4+4-1)*times+4
        print(result)
        
    elif index%3==2:
        times=int(index/3)
        result=(4+4-1)*times+4+4
        print(result)

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70
