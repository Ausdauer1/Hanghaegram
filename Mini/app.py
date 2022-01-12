from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient('13.209.87.2', 27017, username="test", password="test")
db = client.hanghaegram

@app.route('/categories')
def category():
    return render_template("categories_index.html")

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