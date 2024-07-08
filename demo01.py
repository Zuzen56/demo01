from flask import Flask,sessions,redirect,url_for

app = Flask(__name__)

app.secret_key = 'Your_secret_key&^52@!'

@app.route('/hello')
def hello():
    return "hello!!!"

@app.route('/home')
def home():
    if'username' in sessions:
        return f'欢迎{sessions.get("username")}回来！'
    return redirect(url_for('/login'))

@app.route('/login')
def login():
    sessions['username']='张三'
    return redirect(url_for('/home'))


if __name__ == '__main__':
    app.run(port=5010)
