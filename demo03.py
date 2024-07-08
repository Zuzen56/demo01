from flask import Flask,session,flash,render_template,redirect,url_for

app = Flask(__name__)
app.secret_key = 'Your_secret_key&^52@!'

@app.route('/home')
def home():
    username = session.get('username')
    if 'username' in session:
        return render_template('home_page.html',username='username')
    return redirect(url_for('login',username=username))

@app.route('/login')
def login():
    return "test"

if __name__ == '__main__':
    app.run(port=5002)