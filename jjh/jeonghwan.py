from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)

SECRET_KEY = 'SPARTA'

client = MongoClient('13.209.50.161', 27017, username="test", password="test")
db = client.hanghaegram

    # 처음 화면
@app.route('/')
def home():
    return render_template('index.html')

    # 카테고리 페이지로 이동
@app.route('/category')
def login():
    msg = request.args.get("msg")
    return render_template('category.html', msg=msg)

    #회원가입 페이지로 이동
@app.route('/signup')
def register():
    msg = request.args.get("msg")
    return render_template('signup.html', msg=msg)

    # 로그인
@app.route('/sign_in', methods=['POST'])
def sign_in():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

    # 회원가입
@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "profile_name": username_receive,                           # 프로필 이름 기본값은 아이디
        "profile_pic": "",                                          # 프로필 사진 파일 이름
        "profile_pic_real": "profile_pics/profile_placeholder.png", # 프로필 사진 기본 이미지
        "profile_info": ""                                          # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

    # 회원가입
@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

    # 카테고리 모음


@app.route('/pet')
def showing():

    articles = list(db.pet.find({}, {"_id": False}))

    return render_template("pet.html", articles=articles, )

@app.route('/pet/posts', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    now = datetime.now()
    nowtime = now.strftime('%H시 %M분 %S초 / %Y년 %m월 %d일')

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'

    save_to = f'static/image/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'file': f'{filename}.{extension}',
        'upload_time': nowtime
    }

    db.pet.insert_one(doc)
    print(doc)

    return jsonify({'msg': '정상적으로 저장되었습니다.'})

@app.route('/daily')
def showing2():

    articles = list(db.daily.find({}, {"_id": False}))

    return render_template("daily.html", articles=articles, )

@app.route('/daily/posts', methods=['POST'])
def saving2():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    now = datetime.now()
    nowtime = now.strftime('%H시 %M분 %S초 / %Y년 %m월 %d일')

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'

    save_to = f'static/image/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'file': f'{filename}.{extension}',
        'upload_time': nowtime
    }

    db.daily.insert_one(doc)

    return jsonify({'msg': '정상적으로 저장되었습니다.'})

@app.route('/exercise')
def showing3():

    articles = list(db.exercise.find({}, {"_id": False}))

    return render_template("exercise.html", articles=articles, )

@app.route('/exercise/posts', methods=['POST'])
def saving3():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    now = datetime.now()
    nowtime = now.strftime('%H시 %M분 %S초 / %Y년 %m월 %d일')

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'

    save_to = f'static/image/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'file': f'{filename}.{extension}',
        'upload_time': nowtime
    }

    db.exercise.insert_one(doc)

    return jsonify({'msg': '정상적으로 저장되었습니다.'})

@app.route('/food')
def showing4():

    articles = list(db.food.find({}, {"_id": False}))

    return render_template("food.html", articles=articles, )

@app.route('/food/posts', methods=['POST'])
def saving4():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    now = datetime.now()
    nowtime = now.strftime('%H시 %M분 %S초 / %Y년 %m월 %d일')

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'

    save_to = f'static/image/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'file': f'{filename}.{extension}',
        'upload_time': nowtime
    }

    db.food.insert_one(doc)

    return jsonify({'msg': '정상적으로 저장되었습니다.'})

@app.route('/trip')
def showing5():

    articles = list(db.trip.find({}, {"_id": False}))

    return render_template("trip.html", articles=articles, )

@app.route('/trip/posts', methods=['POST'])
def saving5():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    now = datetime.now()
    nowtime = now.strftime('%H시 %M분 %S초 / %Y년 %m월 %d일')

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'

    save_to = f'static/image/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'file': f'{filename}.{extension}',
        'upload_time': nowtime
    }

    db.trip.insert_one(doc)

    return jsonify({'msg': '정상적으로 저장되었습니다.'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)