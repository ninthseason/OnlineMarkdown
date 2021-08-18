from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open("static/text.md", "r", encoding='utf-8') as f:
        text = f.read()
    return render_template("index.html", markdowntext=text)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == "POST":
        text = request.form.get("text")
        verification = request.form.get("verification")
        if verification == "1346":
            with open("static/text.md", 'w', encoding='utf-8') as f:
                f.write(text)
    return "0"


if __name__ == '__main__':
    # app.run()
    http_server = WSGIServer(('0.0.0.0', 5000), app)   # 配置WSGI
    http_server.serve_forever()   # 启动服务器
