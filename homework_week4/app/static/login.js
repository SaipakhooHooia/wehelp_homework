function login(){
    let checkbox_message=document.getElementById('scales');
    if(!checkbox_message.checked){
        alert("Please agree to the terms of service to continue.");
    }
    
}

function submitForm(){
    let number=document.getElementById('positive').value;
    window.location.href = "/square/"+number;
}

document.getElementById('calculateForm').addEventListener('submit', function(event) {
    let number=document.getElementById('positive').value;//取輸入表單的值
    if (number <= 0 || !Number.isInteger(Number(number))){//Number(number)將輸入的數字轉為數字類型
        alert("Please input positive number.");
        event.preventDefault();//阻止表單提交
    }
    else{
        submitForm()
    }
})

