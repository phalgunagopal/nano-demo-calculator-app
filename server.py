from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    
    
    data1=request.json['first']
    data2=request.json['second']
    return jsonify({"result: ": data1+data2 })

   
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
   
    data1=request.json['first']
    data2=request.json['second']
    return jsonify({"result: ": data1-data2 })
    

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
    # app.run(debug=True,port=8080)
