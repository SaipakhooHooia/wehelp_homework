let loginData={
    "username":"test",
    "password":"test"
}

function login(){
    let account_message=document.getElementById('username');
    let password_message=document.getElementById('password');
    let checkbox_message=document.getElementById('scales');
    if(account_message.value==loginData.username && password_message.value==loginData.password && checkbox_message.checked){
        return true;
    }
    else if(!checkbox_message.checked){
        alert("Please check the checkbox first");
        return false;
    }
}