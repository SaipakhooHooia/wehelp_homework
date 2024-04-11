function find(spaces, stat, n){
    // your code here
    let available=[];
    let result;
    //console.log(spaces);//[ 4, 6, 5, 8 ]
    //console.log(stat);//[ 0, 1, 1, 1 ]
    for (let i=0;i<spaces.length;i++){
        if(spaces[i]>=n && stat[i]==1){
            available=available.concat(spaces[i]);
            //console.log(available);
        } 
    }
    //console.log(available);//[ 6, 5, 8 ]
    //console.log(Math.min(...available));//javascript的計算要記得加...
    if(available){
        result=spaces.indexOf(Math.min(...available));
        }
        else{
            result=-1;
        }
        console.log(result);
    }
    
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2