from array import array
from imp import NullImporter
from urllib.parse import quote_from_bytes
from flask import Flask, jsonify
from flask import render_template
from flask import request, jsonify, json #jsonify return JSON 格式;json decode JSON格式的file
from flask import session
import mysql.connector 
from mysql.connector import pooling
from flask_cors import CORS

poolname="mysqlpool"
poolsize=3

connectionpool=mysql.connector.pooling.MySQLConnectionPool(pool_name=poolname,pool_size=poolsize, pool_reset_session=True, host='localhost', user='root', password="password", database='website')
db = connectionpool.get_connection()
cursor = db.cursor() # 使用cursor()方法操作鼠標(中介)

app=Flask(__name__,template_folder='template',static_folder='static')
app.secret_key='Imthegoldenkey'
CORS(app)
app.config["JSON_AS_ASCII"] = False #讓JSON格式可以顯示中文

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
    cursor.execute("SELECT * FROM member WHERE username =%s", (username,))
    name_data = cursor.fetchone()
    if name_data is not None:
        return render_template('fail.html', message='帳號已經被註冊QQ')
    else:   
        cursor.execute(sql, val) #執行mysql語法  
        db.commit() # 提交當前事務(for update,insert,delete only)
        return render_template('index.html')

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    query= "SELECT * FROM member WHERE username = %s AND password = %s"
    input= (username, password,)
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

@app.route("/api/members")
def api():
    username = request.args.get('username')
    cursor.execute("SELECT id,name,username FROM member WHERE username=%s",(username,))
    query_result= cursor.fetchone()
    #correct_result=json.dumps(dictionary, indent=4) #indent for 美化output
    null = None
    error_dictionary={
        "data":null
    }
    if query_result is not None:
        id=query_result[0]
        name=query_result[1]
        user_name=query_result[2]
        dictionary={
        "data":{
            "id": id,
            "name":name,
            "username":user_name
        }
    }
        return jsonify(dictionary) 
    else:
        return jsonify(error_dictionary) 
# 這個是member page裡檢索page

@app.route("/api/member", methods=["POST"])
def rename():
    username = session["name"]
    name = request.get_json()
    cursor.execute("UPDATE member SET name = %s WHERE name=%s",(name["name"], username,))
    db.commit()
    true = True
    loginFail={
        "error": true 
    }
    loginSuccess={
        "ok": true
    }
    if not session["name"]:
        return jsonify(loginFail)
    else:
        return jsonify(loginSuccess)
# 這個是member page裡改名page

@app.route("/signout")
def signout():
    session["name"] = None
    return render_template('index.html')

@app.route("/error/")
def fail():
    return render_template('fail.html')

if __name__=='__main__':
    app.debug = True
    app.run(host='127.0.0.1',port=3000)
#flask要啟動了~