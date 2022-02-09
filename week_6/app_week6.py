from flask import Flask
from flask import render_template
from flask import request
from flask import session
import mysql.connector
db = mysql.connector.connect (host='localhost', user='root', password="password", database='website')
cursor = db.cursor() # 使用cursor()方法操作鼠標 

app=Flask(__name__,template_folder='template',static_folder='static\css')
app.secret_key='Imthegoldenkey'

@app.route("/", methods=['GET', 'POST'])
def login():
    return render_template('index.html')

@app.route("/register", methods=['POST'])
def register():   
    name = request.form['member_name']
    username = request.form['username']
    password = request.form['password']
    sql = "INSERT INTO member(name, username, password) VALUES(%s,%s,%s)" # %s means subsitute string (placeholder)
    val = (name, username, password)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM member WHERE name =%s", (name,))
    name_data = cursor.fetchone()
    if name_data is not None:
        return render_template('fail.html', message='帳號已經被註冊QQ')
    else:   
        cursor.execute(sql, val) #執行mysql語法  
        db.commit() # 提交當前事務
        return render_template('index.html')

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    query= "SELECT * FROM member WHERE username = %s AND password = %s"
    input= (username, password)
    cursor.execute(query, input)
    results= cursor.fetchone() #fetchall(get ALL) vs fetchone(get the 1st row)
    if results != None:
        results= results[1]
        session["name"] = results # record the username-> for security
        return render_template('member.html', hello_name=results)
    elif not username or not password:
        return render_template('fail.html', message='請輸入帳號、密碼')
    else:
        return render_template('fail.html', message='帳號,或密碼輸入錯誤QQ')

# 這個是homepages

@app.route("/member")
def member():
    if not session["name"]:
        return render_template('index.html')
    return render_template('member.html')
# 這個是member page

@app.route("/signout")
def signout():
    session["name"] = None
    return render_template('index.html')

@app.route("/fail")
def fail():
    return render_template('fail.html')

if __name__=='__main__':
    app.debug = True 
    app.run()
#flask要啟動了~