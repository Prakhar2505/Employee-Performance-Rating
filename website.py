from flask import Flask , render_template, request
from sklearn.externals import joblib

app = Flask(__name__) # initialization

@app.route("/")

def index():
    #return("Welcome to Python Programming")
    return render_template("index.html")

@app.route("/linear",methods=['GET','POST'])
def linearmodel():
    if request.method == 'POST':
        data=request.form
        model = joblib.load("gdp_model.sav")
        value = float(data['value'])
        prediction = model.predict([[value]])
        result = "Life satisafaction is: " + str(prediction[0][0])
        #return model loaded successfully
        return result
    else:
        return "No value found"

if __name__ == "__main__":
    app.run()
