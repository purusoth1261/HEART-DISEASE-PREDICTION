from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) # Initialize the flask App
model = pickle.load(open('herat.pkl', 'rb')) # Load the trained model

@app.route('/') # Homepage
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age_var = float(request.form['age'])
    sex_var = float(request.form['sex'])
    bp_var = float(request.form['bp'])
    col_var = float(request.form['cholesterol'])
    prediction =model.predict([[age_var,sex_var,bp_var,col_var]])  # this returns a list e.g. [127.20488798], so pick first element [0]
    print("prediction is ",prediction)
    if prediction == 1:
        res = "1"
    else:
        res = "0"
    return render_template('output.html', predict=f'Age for person: {age_var} and sex is :{sex_var} and blood preasure :{ bp_var}  and colostral is:{col_var} the result is{res}')
  
    

if __name__ == "__main__":
    app.run(debug=True)
