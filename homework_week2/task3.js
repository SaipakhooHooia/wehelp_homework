function func(...data){
    // your code here
    var my_list=[];
    var name_list=my_list.concat(...data);
    //console.log(name_list);//['彭大牆', '陳王明雅', '吳明']
    //var temp_list=[];
    var compare_list=[];

    for(let name of name_list){
        var word_list=[];
        if (name.length==2){
            word_list=word_list.concat(name[1]);
        }
        else{
        for (let i = 1; i < name.length - 1; i++){
            word_list=word_list.concat(name[i]);  
        }}
        //console.log(word_list);
        compare_list.push(word_list);//使用push()而不是concat()，可以將列表加入列表，而不會拆解成元素
    }

    function compare(list1,list2){
        var new_list1=[];
        new_list1=new_list1.concat(list1);
        var new_list2=[];
        new_list2=new_list2.concat(list2);//先將列表中的列表拆解成一個個元素
        //console.log("new_list1=",new_list1);
        //console.log("new_list2=",new_list2);
        for (let item of new_list1){
            for (let item2 of new_list2){
                if(item===item2){
                    /*var list3=list2.slice(list2.indexOf(list1)-1,list2.indexOf(list1));
                    console.log("list3=",list3);
                    return list3;//有相同元素*/
                    return true;
                }
            }
        }
        return false;//沒有相同元素
    }

    for (let name of compare_list){
        for (let i=0;i<compare_list.length;i++){
            let temp_list=[];
            temp_list = compare_list[i];//[ '大' ]
            let rest_list=[];
            for (let j=0;j<compare_list.length;j++){
                if (j!=i){//將compare_list裡面的元素加進去rest_list裡面，如果=temp_list則不加
                    rest_list=rest_list.concat(compare_list[j]); //[ '王', '明', '明' ]
                }
            }
            if (!(compare(temp_list,rest_list))){//如果這個function return false(沒有相同元素)
                var result=temp_list;
                break;
            }
        }
        //console.log("迴圈結果",final_list);
    }
    //console.log(result);

    if (result){
       for (let name of name_list){
        for (let item of result){
            if(name.includes(item)){
            //console.log("here");
            console.log(name);
            break;
        }
    }    
    } 
    }
    else{
        console.log("沒有");
    }
    

    }
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
//console.log("***")
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
//console.log("***")
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
//console.log("***")
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安