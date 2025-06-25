
# Follow.is → 企业微信机器人 推送器

这是一个使用 Flask 构建的中间平台，用于接收 Follow.is 的 webhook 请求，并将内容推送到你配置的企业微信群机器人。

## 🛠 部署方式（推荐使用 Render）

1. 注册并登录 https://render.com
2. 创建一个新的 Web Service，连接此代码仓库
3. 设置 Build Command: `pip install -r requirements.txt`
4. 设置 Start Command: `python app.py`
5. 部署后会获得一个公网地址（如 https://your-app.onrender.com）
6. 将该地址设置为 Follow.is 的 webhook 地址（POST 请求，路径为 /follow）

## 🔧 企业微信机器人配置

已在代码中写入你的机器人 webhook 地址，如需替换请编辑 `app.py` 中的变量 `WECHAT_WEBHOOK`

## 🧪 测试方式

可用 curl 或 Postman 测试：

```bash
curl -X POST https://your-app.onrender.com/follow \
     -H "Content-Type: application/json" \
     -d '{"title": "特朗普宣布加税", "url": "https://follow.is/example-news"}'
```

