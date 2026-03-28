from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('breast_cancer_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    raw_input = request.form.get('features')

    try:
        values = [float(x) for x in raw_input.replace(',', ' ').split()]

        if len(values) != 31:
            return render_template('index.html',
                                   prediction_text="❌ Enter exactly 31 values")

        data = np.array(values).reshape(1, -1)
        data = scaler.transform(data)

        prediction = model.predict(data)[0]

        # adjust if needed
        result = "Malignant (Cancer)" if prediction == 1 else "Benign (Not Cancer)"

        return render_template('index.html',
                               prediction_text=f"Result: {result}")

    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)