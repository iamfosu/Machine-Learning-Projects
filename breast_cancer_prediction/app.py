import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

model = pickle.load(open('breast_cancer_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction_text="", image_file=None)

@app.route('/predict', methods=['POST'])
def predict():
    raw_input = request.form.get('features')

    try:
        values = [float(x) for x in raw_input.replace(',', ' ').split()]

        if len(values) != 31:
            return render_template('index.html',
                                   prediction_text="❌ Enter exactly 31 values",
                                   image_file=None)

        data = np.array(values).reshape(1, -1)
        data = scaler.transform(data)

        prediction = model.predict(data)[0]

        if prediction == 1:
            result = "Cancerous"
            image_file = "sad.jpg"
        else:
            result = "Not Cancerous"
            image_file = "happy.jpg"

        return render_template('index.html',
                               prediction_text=f"Result: {result}",
                               image_file=image_file)

    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: {str(e)}",
                               image_file=None)


if __name__ == "__main__":
    app.run(debug=True)