from flask import Flask, render_template

app = Flask(__name__)

# 模擬一些文章資料
posts = [
    {
        "id": 1,
        "title": "Flask 入門教學",
        "author": "小明",
        "content": "這是一篇介紹 Flask 的入門文章。Flask 是一個輕量級的 Python Web 框架..."
    },
    {
        "id": 2,
        "title": "Python 基礎語法",
        "author": "小華",
        "content": "本文介紹 Python 的基本語法，包含變數、條件判斷與迴圈結構..."
    }
]

@app.route('/')
def index():
    # 顯示所有文章列表
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    # 根據 id 顯示單篇文章
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "文章不存在", 404
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)

