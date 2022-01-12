from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient('13.209.87.2', 27017, username="test", password="test")
db = client.hanghaegram


@app.route('/detail')
def showing():

    articles = list(db.articles.find({}, {"_id": False}))

    print(articles)
    return render_template("detail.html", articles=articles, )



@app.route('/detail/posts', methods=['POST'])
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

    db.articles.insert_one(doc)

    return jsonify({'msg': '정상적으로 저장되었습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)