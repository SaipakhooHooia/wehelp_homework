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

function findAndPrint(messages, currentStation){
    // your code here
    var dictionary={}
    var distance=[]   

    for (let [name, message] of Object.entries(messages)) {//Object.entries就像python的dic.items()一樣，會返回key和value
        // 遍歷 stations_list1 中的每一個車站名稱
        for (let i = 0; i < stations_list1.length; i++) {
            let station = stations_list1[i];
            // 檢查 station 是否已經存在於 dictionary 的值中
            if (!Object.values(dictionary).includes(station) && message.includes(station)) {
                //Object.values就像python的dic.value()一樣，會返回value
                // 如果車站名沒有已經存在在dictionary中，就將 name 和 station 添加到 dictionary 中
                Object.assign(dictionary, { [name]: station });//相對於python中的dic.update
                // 跳出內層循環，已經找到一個符合條件的 station
                //break;
            }
        }

        for (let i = 0; i < stations_list2.length; i++) {
            let station = stations_list2[i];
            // 檢查 station 是否已經存在於 dictionary 的值中
            if (!Object.values(dictionary).includes(station) && message.includes(station)) {
                //Object.values就像python的dic.value()一樣，會返回value
                // 如果車站名沒有已經存在在dictionary中，就將 name 和 station 添加到 dictionary 中
                Object.assign(dictionary, { [name]: station });//Object.assign相對於python中的dic.update
                // 跳出內層循環，已經找到一個符合條件的 station
                //break;
            }
        }
    }

    //console.log(dictionary)

    if (stations_list1.includes(currentStation)){
        for (let location of Object.values(dictionary)){
            //console.log(location)
              if (stations_list1.includes(location)){
                   //distance.append(abs(stations_list1.index(current_station) - stations_list1.index(location)))
                   distance.push(Math.abs(stations_list1.indexOf(currentStation) - stations_list1.indexOf(location)));
                   //console.log("print")
                }
                   
              else if (stations_list2.includes(location)){
                   //distance.append(abs(stations_list1.index(current_station) - stations_list1.index("Qizhang"))+1 )
                   distance.push(Math.abs(stations_list1.indexOf(currentStation) - stations_list1.indexOf("Qizhang"))+1);
                   //console.log("print1")
                }
        }        
    }

    else if (stations_list2.includes(currentStation)){
        //console.log("print5")
        for (let location of Object.values(dictionary)){
            if (stations_list1.includes(location)){
                 //distance.append(abs(stations_list1.index(current_station) - stations_list1.index(location)))
                 distance.push(Math.abs(stations_list1.indexOf(currentStation) - stations_list1.indexOf("Qizhang"))+1);
                 //console.log("print2")
              }
                 
            else if (stations_list2.includes(location)){
                 //distance.append(abs(stations_list1.index(current_station) - stations_list1.index("Qizhang"))+1 )
                 distance.push(Math.abs(stations_list1.indexOf(currentStation) - stations_list1.indexOf(location)));
                 //console.log("print3")
              }
      } 
    }
    var min_distance_index=0;
    min_distance_index=distance.indexOf(Math.min(...distance));
    console.log(Object.keys(dictionary)[min_distance_index])
}
const messages={
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Leslie":"I'm at home near Xiaobitan station.",
"Vivian":"I'm at Xindian station waiting for you.",
//"Vivi":"I'm at Jingmei MRT station."
};
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian