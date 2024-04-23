let loginData={
    "username":"test",
    "password":"test"
}

function login(){
    let account_message=document.getElementById('username');
    let password_message=document.getElementById('password');
    let checkbox_message=document.getElementById('scales');
    if(account_message.value==loginData.username && password_message.value==loginData.password && checkbox_message.checked){
        console.log("Logged in status:", "{{ request.session.logged_in }}");
        return true;
    }
    else if(!checkbox_message.checked){
        alert("Please aggree to the terms of service to continue.");
        return false;
    }
    
}
