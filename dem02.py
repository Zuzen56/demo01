from flask import Flask,render_template

app=Flask(__name__)

@app.route('/index')
def index():
    return "这是一个测试文件"

@app.route('/template')
def template():
    name="张三"
    return render_template('index.html',name = name)

@app.route('/macro')
def input_style():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5001)
