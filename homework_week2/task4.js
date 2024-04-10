function getNumber(index){
    // your code here
    //0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25
    if (index%3===0){
        let times=Math.floor(index/3);
        let result=(4+4-1)*times;
        console.log(result);
    }
    /*let index = 5; // 举例
let times = Math.floor(index / 3); */

    else if (index%3==1){
        let times=Math.floor(index/3);
        let result=(4+4-1)*times+4;
        console.log(result);
    }
        
        
    else if (index%3==2){
        let times=Math.floor(index/3);
        let result=(4+4-1)*times+4+4;
        console.log(result);
    }
        
    }
    getNumber(1); // print 4
    getNumber(5); // print 15
    getNumber(10); // print 25
    getNumber(30); // print 70