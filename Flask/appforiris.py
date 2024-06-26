import pickle
import os
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open(r'randomf.pkl', 'rb'))  

@app.route('/')  
def home():
    return render_template('index.html')

@app.route('/submit', methods=["POST", "GET"])
def submit():
    
    try:
        SepalLengthCm = float(request.form['SepalLengthCm'])
        SepalWidthCm = float(request.form['SepalWidthCm'])
        PetalLengthCm = float(request.form['PetalLengthCm'])
        PetalWidthCm = float(request.form['PetalWidthCm'])
    except ValueError:  
        return render_template("index.html", result="Please enter valid numerical values.")

    input_data = {
        'SepalLengthCm': SepalLengthCm,
        'SepalWidthCm': SepalWidthCm,
        'PetalLengthCm': PetalLengthCm,
        'PetalWidthCm': PetalWidthCm
    }

    input_features = [input_data['SepalLengthCm'], input_data['SepalWidthCm'],
                       input_data['PetalLengthCm'], input_data['PetalWidthCm']]

    prediction = model.predict([input_features])
    print(prediction)

    result = prediction[0]

    if result == "Iris-setosa":
        result = "Iris setosa"
    elif result == "Iris-versicolor":
        result = "Iris versicolor"
    else:
        result = "Iris virginica"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False)
