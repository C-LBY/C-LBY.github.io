const fs = require('fs');

// 处理请求的函数
function handleRequest(req, res) {
    const filePath = 'path/to/your/file.txt'; // 替换为你要读取的文件路径

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            res.statusCode = 500;
            res.end('Error reading the file');
            return;
        }

        // 将文件内容按行分割
        const lines = data.split('\n');

        // 获取最后一行
        const lastLine = lines[lines.length - 1];

        // 输出到控制台
        console.log(lastLine);

        // 发送响应给前端
        res.end(lastLine);
    });
}

// 注册插件
hexo.extend.server.route({
    path: '/readfile',
    method: 'GET',
    handler: handleRequest
});