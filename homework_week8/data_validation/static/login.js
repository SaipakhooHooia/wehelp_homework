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

const passwordPattern = /^[A-Za-z0-9@#$%]{4,8}$/;
function signup(){
    let signup_name = document.getElementById('signup_name').value;
    let signup_username = document.getElementById('signup_username').value;
    let signup_password = document.getElementById('signup_password').value;
    if (!signup_name || !signup_username || !signup_password) {
        alert("No empty input.");
        return false;
    }

    console.log("Password test result: ", passwordPattern.test(signup_password));
    console.log("Password test result: ", signup_password);
    if(!passwordPattern.test(signup_password)){
        alert("Password must be 4-8 characters long and include only English alphabets, numbers, and @#$%");
        //event.preventDefault();
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

document.getElementById('member-search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let search_username = document.getElementById('search_username').value;
    fetch(`/api/member?username=${search_username}`)
        .then(response => response.json())
        .then(data => {
            if (data && data.data) {
                document.getElementById('nameBroad').textContent = `${data.data.name}(${search_username})`;
            } else {
                document.getElementById('nameBroad').textContent = 'No Data';
            }
        })
        .catch(error => {
            console.error('Error fetching member name:', error);
            document.getElementById('nameBroad').textContent = 'No Data';
        });
});

function updateName(){
    let newName = document.getElementById("new_name").value;
    fetch('/api/member', {
        method: 'PATCH', 
        headers: {
            'Content-Type': 'application/json', 
        },
        body: JSON.stringify({ "name": newName })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.ok) {
            console.log('Name has been changed.');
            document.getElementById('updateNameBroad').textContent = `更新成功`;
            let welcomeMessage = document.querySelector('.login-text');
            welcomeMessage.textContent = `${newName}, 歡迎登入系統`;
        } else if (data.error) {
            console.log('Name changed failed.');
            document.getElementById('updateNameBroad').textContent = `更新失敗`;

        }
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}