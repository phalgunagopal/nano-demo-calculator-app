from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    content_type=request.headers.get('Content-Type')
    if content_type=='application/json':
        json=request.json
        data1=json['first']
        data2=json['second']
        first=(int) (data1)
        second=(int)(data2)
        sum=first+second
        return jsonify(sum)

    else:
        return 'content-type not matching'
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    content_type=request.headers.get('Content-Type')
    if content_type=='application/json':
        json=request.json
        data1=json['first']
        data2=json['second']
        first=(int) (data1)
        second=(int)(data2)
        diff=first-second
        return jsonify(diff)

    else:
        return 'content-type not matching'

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
    # app.run(debug=True,port=8080)
