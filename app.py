
import db
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/action_page', methods=['GET', 'POST'])
def action_page():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    # DB에 데이터 저장
    db.insert_data(name, email, message)
    # return "form.html 에서 찾기 버튼 눌렀을때 온 페이지"
    # return f"당신이 입력한 {name} {email} {message}"
    return render_template("action_page.html")

@app.route('/msg')
def msg():
    contact_list = db.select_data()
    return render_template("message.html", data=contact_list)