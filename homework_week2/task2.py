# your code here, maybe
consultants_time={}

def book(consultants, hour, duration, criteria):
# your code here
    rate_ranking=[]
    price_ranking=[]

    for consultant in consultants:
         if consultant['name'] not in consultants_time:
              consultants_time[consultant['name']]=[]
    #先在時間表中將consultants中的人名新增到consultants_time的key裡

    sorted_consultants = sorted(consultants, key=lambda x: x['rate'], reverse=True)
    rate_ranking = [consultant['name'] for consultant in sorted_consultants]
    #print(rate_ranking)#[4.5, 3.8, 3]john,jenny,bob

    sorted_consultants = sorted(consultants, key=lambda x: x['price'])
    price_ranking = [consultant['name'] for consultant in sorted_consultants]
    #print(price_ranking)#[800, 1000, 1200]jenny,john,bob

    def book_time():
        booked_time=[]
        for i in range(duration):
            booked_time.append(hour+i)
        return booked_time
    time_duration=book_time()
    #print(time_duration)

    final_decision=None

    if criteria=='rate':
         for i in range(len(consultants_time.keys())):
              if not set(time_duration) & set(consultants_time[rate_ranking[i]]):
                   consultants_time[rate_ranking[i]].extend(time_duration)
                   final_decision=rate_ranking[i]
                   break
              else:
                   final_decision="No Service"

    if criteria=='price':
         for i in range(len(consultants_time.keys())):
              if not set(time_duration) & set(consultants_time[price_ranking[i]]):
                   consultants_time[price_ranking[i]].extend(time_duration)
                   final_decision=price_ranking[i]
                   break
              else:
                   final_decision="No Service"
    
    print(final_decision)


    """
    for consultant in consultants:
        booked_time = []
        for j in range(duration):
            booked_time.append(hour+j)
        consultants_time[consultant["name"]].extend(booked_time)

    print(consultants_time)"""
    
consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny

book(consultants, 11, 2, "price") # Jenny

book(consultants, 10, 2, "price") # John

book(consultants, 20, 2, "rate") # John

book(consultants, 11, 1, "rate") # Bob

book(consultants, 11, 2, "rate") # No Service

book(consultants, 14, 3, "price") # John