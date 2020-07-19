from flask import Flask, render_template, request
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/")

def index():
    #return("Welcome to Python Programming")
    return render_template("login.html")

@app.route("/linear",methods=['GET','POST'])
def linearmodel():
    if request.method == 'POST':
        data = request.form
        model = joblib.load("performanceModel.sav")
        value1 = float(data['value1'])
        value2 = float(data['value2'])
        value3 = float(data['value3'])
        prediction = model.predict([[value1,value2,value3]])
        result = "Employee performance rating will be: " + str(prediction[0][0])
        data = {
            'satisfaction': value1,
            'salHike': value2,
            'lastProm': value3,
            'perRating':prediction[0][0]
        }

        return render_template("ans.html",
                               data=data)

if __name__ == "__main__":
    app.run()
