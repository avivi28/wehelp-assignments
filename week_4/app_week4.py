from flask import Flask, redirect
#flask的第一步
from flask import render_template
#flask can not be resolved->install flask again:D!
from flask import request
# request 保存了HTTP請求(get/post)的一切信息,並連接html~
from flask import session
###
from flask import redirect, url_for
#redirect: 重新引導到某個url->傳遞參數username

app=Flask(__name__,template_folder='template',static_folder='static\css')
#static:靜態資料for CSS/JS
app.secret_key='Imthegoldenkey'
#create a golden key of flask->這樣flask_login才能運作

@app.before_request #防止強進member page
def before_request():#check whether the user id exists in session?

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']]

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User:{self.username}>'

users = []
users.append(User(id=1, username="test", password="test"))
users.append(User(id=2, username="bear", password="bear"))

@app.route("/", methods=['GET', 'POST'])
def login():
    return render_template('index.html')

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username'] #from html form 的 name
        password = request.form['password']

        if not username or not password:
            return redirect(url_for('fail', message='請輸入帳號、密碼'))

        user = [x for x in users if x.username == username]
        password = [x for x in users if x.password == password]
        if not user or not password:
            return redirect(url_for('fail', message='帳號,或密碼輸入錯誤QQ'))

        #use the class user, and check 帳號correct or not
        if user and password:
            session['user_id']=user[0].id
            return redirect(url_for('member'))

    return render_template('index.html')
# 這個是homepages
# 要把html放在正確的repository~

@app.route("/member")
def member():
    if not session['user_id']:
        return redirect(url_for('signin'))
    return render_template('member.html')
# 這個是member page

@app.route("/signout")
def signout():
    session['user_id'] = None
    return render_template('index.html')

@app.route("/fail")
def fail():
    return render_template('fail.html')

if __name__=='__main__':
    app.debug = True 
    app.run()
#flask要啟動了~