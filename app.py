from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 企业微信机器人 Webhook
WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=570e35d7-f044-4129-9276-f41688eddd8b"

@app.route("/")
def index():
    return "Follow.is to WeChat Bot is running.", 200

@app.route("/follow", methods=["POST"])
def follow_update():
    data = request.json or {}
    title = data.get("title", "Follow.is 有更新")
    url = data.get("url", "")
    content = f"📢 Follow.is 更新通知：\n\n标题：{title}\n链接：{url}"

    # 推送到企业微信
    resp = requests.post(WECHAT_WEBHOOK, json={
        "msgtype": "text",
        "text": {"content": content}
    })

    return "Pushed", resp.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
