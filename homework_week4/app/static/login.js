function login(){
    //let account_message=document.getElementById('username');
    //let password_message=document.getElementById('password');
    let checkbox_message=document.getElementById('scales');
    if(!checkbox_message.checked){
        alert("Please agree to the terms of service to continue.");
        return false;
    }
    
}

document.getElementById('signin').addEventListener('submit', async function(event) {
    event.preventDefault(); // 阻止默认的表单提交行为

    const formData = new FormData(this);
    const response = await fetch('/signin', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const responseData = await response.json(); // 解析 JSON 响应数据
        if (responseData.error) {
            // 显示错误提示信息或者其他处理
            window.location.href = '/error_dealing'

        } else {
            // 登录成功，重定向到/member页面
            window.location.href = '/member';
        }}

});
/*if(!checkbox_message.checked){
        alert("Please aggree to the terms of service to continue.");
        return false;
    }*/