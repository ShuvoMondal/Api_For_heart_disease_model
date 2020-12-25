from flask import Flask,jsonify,render_template,request
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)

rfc=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
@cross_origin()
def predict():

    parameters = request.get_json()

    age = parameters.get('age')
    sex = parameters.get('sex')
    cp = parameters.get('cp')
    trestbps = parameters.get('trestbps')
    chol = parameters.get('chol')
    fbs = parameters.get('fbs')
    restecg = parameters.get('restecg')
    thalach = parameters.get('thalach')
    exang = parameters.get('exang')
    oldpeak = parameters.get('oldpeak')
    slope = parameters.get('slope')
    ca = parameters.get('ca')
    thal = parameters.get('thal')
    data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

    data_float=[]
    for i in data:
        data_float.append(float(i))

    result=rfc.predict([data_float])[0]
    if result == 1:
        return jsonify({'result':1})
    else:
        return jsonify({'result':0})

if __name__ == "__main__":
    app.run(debug=True, port="5300")

#Endpointes
#http://127.0.0.1:5300/api/predict/
#http://127.0.0.1:5300/api/predict/
