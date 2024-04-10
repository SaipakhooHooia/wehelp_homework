// your code here, maybe
var consultants_time={}

function book(consultants, hour, duration, criteria){
    // your code here
    //var rate_ranking=[] 因為底下使用Const定義列表，因此不需要先定義一個空列表
    //var price_ranking=[]

    for(let consultant of Object.entries(consultants)){
        if(!(Object.keys(consultants).includes(consultant["name"]))){
            var name=consultant[1]['name'];
            //consultant長這樣: 
            //[ '0', { name: 'Johny', rate: 4.5, price: 1000 } ]
            //[ '1', { name: 'Bob', rate: 3, price: 1200 } ]
            //[ '2', { name: 'Jenny', rate: 3.8, price: 800 } ]
            //莫名其妙多了一個索引在前面，所以要取consultant[1]，索引後面的字典，再來才是取裡面的["name"]
            //console.log(consultant);
            consultants_time[name]=[];//var [key] = value;
        }
    }
    console.log(consultants_time)

    // 按照 rate 排序
    const sortedByRate = consultants.slice().sort((a, b) => b.rate - a.rate);
    const rate_ranking = sortedByRate.map(consultant => consultant.name);
    //console.log(rate_ranking); // ["John", "Jenny", "Bob"]

    // 按照 price 排序
    const sortedByPrice = consultants.slice().sort((a, b) => a.price - b.price);
    const price_ranking = sortedByPrice.map(consultant => consultant.name);
    //console.log(price_ranking); // ["Jenny", "John", "Bob"]

    function book_time(){
    let booked_time=[]
    for (let i=0;i<duration;i++){
        booked_time.push(hour+i)}
    return booked_time
    }
    var time_duration=book_time();
    //console.log(time_duration);

    var rate_consultant;
    var final_decision;

    function compare(list1,list2){
        for (let item of list1){
            for (let item2 of list2){
                if(item===item2){
                    return true;//有相同元素
                }
            }
        }
        return false;//沒有相同元素
    }

    if (criteria==="rate"){
        for (let item of time_duration){
            for (let i =0;i<Object.keys(consultants_time).length;i++){
                if (!(compare(consultants_time[rate_ranking[i]],time_duration)))
                //(!(consultants_time[rate_ranking[i]].includes(item)))
            {
                var rate_consultant=i;
                break;//如果沒有加break就會一直往下執行配對到最後一個顧問
                //consultants_time[rate_ranking[0]].push(time_duration);
            }
            else{
                final_decision="No Service";
            }
            }  
        }
    }
    for (let i =0;i<Object.keys(consultants_time).length;i++){
        if (rate_consultant===i){
            consultants_time[rate_ranking[i]]=consultants_time[rate_ranking[i]].concat(time_duration);
            final_decision=rate_ranking[i];
        }
    }

    var price_consultant;
    
    if (criteria==="price"){
        for (let item of time_duration){
            for (let i =0;i<Object.keys(consultants_time).length;i++){
                if (!(compare(consultants_time[price_ranking[i]],time_duration))){
                var price_consultant=i;
                break;
                //consultants_time[rate_ranking[0]].push(time_duration);
            }
            else{
                final_decision="No Service";
            }
            }  
        }
    }
    for (let i =0;i<Object.keys(consultants_time).length;i++){
        if (price_consultant===i){
            consultants_time[price_ranking[i]]=consultants_time[price_ranking[i]].concat(time_duration);
            final_decision=price_ranking[i];
        }
    }

    console.log(final_decision)
    //console.log(consultants_time)
    }


const consultants=[
{"name":"Johny", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800},
];

book(consultants, 15, 1, "price"); // Jenny
console.log("***")
book(consultants, 11, 2, "price"); // Jenny
console.log("***")
book(consultants, 10, 2, "price"); // John
console.log("***")
book(consultants, 20, 2, "rate"); // John
console.log("***")
book(consultants, 11, 1, "rate"); // Bob
console.log("***")
book(consultants, 11, 2, "rate"); // No Service
console.log("***")
book(consultants, 14, 3, "price"); // John

//{'John': [10, 11, 20, 21, 14, 15, 16], 'Bob': [11], 'Jenny': [15, 11, 12]}