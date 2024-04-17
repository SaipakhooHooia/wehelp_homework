const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// 设置静态文件目录
app.use(express.static(path.join(__dirname )));

// 首页路由
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'task3.html'));
});

// 启动服务器
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

//http://localhost:3000
