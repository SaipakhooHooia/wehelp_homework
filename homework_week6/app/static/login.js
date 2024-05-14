function login(){
    let checkbox_message = document.getElementById('scales');
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    if(!checkbox_message.checked){
        alert("Please agree to the terms of service to continue.");
        return false;
    }
    if(!username || !password){
        alert("No empty input.");
        return false;
    }
    
}

function signup(){
    let signup_name = document.getElementById('signup_name').value;
    let signup_username = document.getElementById('signup_username').value;
    let signup_password = document.getElementById('signup_password').value;
    if (!signup_name || !signup_username || !signup_password) {
        alert("No empty input.");
        return false;
    }
}

function commentLine(){
    console.log("comment is been recorded.");
    let message = document.getElementById('comment').value;
    if(!message){
        alert("No comment is inputed.");
        return false;
    }
    let commentBroad = document.getElementById('commentBroad');
    commentBroad.innerText = message;
}




  