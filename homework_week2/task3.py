def func(*data):
# your code here
    my_list=list(data)#['彭大牆', '陳王明雅', '吳明']
    compare_list=[]
    
    for name in my_list:
        #print(f"Current string: {name}")
        temp_list=[]
        if len(name)==2:
            for word in name[1]:
                temp_list.append(word)
            compare_list.append(temp_list)
        else:
            for word in name[1:-1]:
                temp_list.append(word)
            compare_list.append(temp_list)

    #print(compare_list)

    #new_list=[]
    #for item in range(len(compare_list)):
    #    subject = list(compare_list[item])
    #    new_list.append(subject)
    #print("new_list=",new_list)
    #copy_list=compare_list.copy()
    no_intersection=None

    for item in range(len(compare_list)):#如何讓compare_list不會減少?
        #變量item沒有被使用到沒關係，僅代表以下動作要執行len(compare_list)次
        copy_list=compare_list.copy()#在每次執行時copy一次才有每次更新列表成原本的樣子
        subject=[]
        subject=list(copy_list.pop(item))
        compare_items=[]
        for other_item in copy_list:
            compare_items.extend(other_item)
        
        if set(subject) & set(compare_items):
            continue
        elif not set(subject) & set(compare_items):
            no_intersection=subject

    if not (no_intersection):
        print('沒有')
    else:
        for data in my_list:
            if set(no_intersection) & set(data):
                result=data#將中間名對照回my_list裡面的全名並印出
        print(result)   

        #print("subject=",subject)
        #print("compare_items=",compare_items)
        #print("no_intersection=",no_intersection)
        #if not set(subject) & set(compare_items):
        #    print(subject)
        #print(subject)
        #print(compare_items)

        
       

'''
    for i in compare_list:
        unique=True
        for j in compare_list:
            if i!=j and set(i) & set(j):
                unique=False
                break
            if unique:
                print(j)

'''
'''    for item in compare_list:
        print(type(item))
        for word in item:
            print(type(word))
            intersection = set(compare_list[word]) & set(compare_list[item])
            if not intersection:
                print(compare_list[item])
    #        if len(intersection) == 0:
     #           print(word)'''

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
#print("*")
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
#print("*")
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
#print("*")
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
