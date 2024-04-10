stations_list1=[
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongsan",
    "Beimon",
    "Ximen",
    "Xiaonanmon",
    "CKS Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xindian City Hall",
    "Xindian",
]

stations_list2=["Xiaobitan"]

def find_and_print(messages, current_station):
    dictionary={}
    distance=[]   

    for name, message in messages.items():
        for station in stations_list1:
                if station not in dictionary.values() and station in message:
                     dictionary.update({name:station})
            #印出在主線的站牌，且若站牌在該字典沒有重複，則新增進字典
        for station in stations_list2:
                if station not in dictionary.values() and station in message:
                    dictionary.update({name:station})
            #印出在支線的站牌，且若站牌在該字典沒有重複，則新增進字典

    #for name,station in dictionary.items():#如果message中有兩人在同一站就只顯示第一人的名稱
    #     for name2,station2 in dictionary.items():
    #          if name!=name2 and station==station2:
    #               dictionary.pop(name2) #不可以用pop()否則會導致dictionary結果亂掉
    #print(dictionary)
                    

    
    #print(dictionary)
    #{'Leslie': 'Xiaobitan', 'Bob': 'Ximen', 'Mary': 'Jingmei', 'Copper': 'Taipei Arena', 'Vivian': 'Xindian', 'Vivi': 'Qizhang'}

    if current_station in stations_list1:
         for name,location in dictionary.items():
              if location in stations_list1:
                   distance.append(abs(stations_list1.index(current_station) - stations_list1.index(location)) )
                   
              elif location in stations_list2:
                   distance.append(abs(stations_list1.index(current_station) - stations_list1.index("Qizhang"))+1 )
                
    elif current_station in stations_list2:    
         for name,location in dictionary.items():
              if location in stations_list1:
                   distance.append(abs(stations_list1.index(current_station) - stations_list1.index("Qizhang"))+1 )
                   
              elif location in stations_list2:
                   distance.append(abs(stations_list1.index(current_station) - stations_list1.index(location)) )
                   
         #distance.append(abs(stations_list1.index(item) - stations_list.index(station)) + 1)
    #print(distance)#將每個人離你的距離放入distance列表中並列出每個人離你的距離
    min_distance_index=0
    min_distance_index=distance.index(min(distance))#找出最小的距離的那個人
    #print(min_distance_index)
    print(list(dictionary.keys())[min_distance_index])#印出那個人的名字



# your code here
messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.7",
"Mary":"I have a drink near Jingmei MRT station.14",
"Copper":"I just saw a concert at Taipei Arena.2",
"Vivian":"I'm at Xindian station waiting for you.18",
#"Vivi":"I'm at Xiaobitan station waiting for you.18"
}

find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian
