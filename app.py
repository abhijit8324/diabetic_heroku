from flask import Flask, render_template, request
import joblib


app = Flask(__name__)

# business logic
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/predict', methods=['post'])
def predict():
        
    # load the prediction model
    
    model = joblib.load('dibatic_80.pkl')
    
    # Convert form data to numeric values
    preg = int(request.form.get('preg'))
    plas = int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age = int(request.form.get('age'))
    
    
    print([preg, plas, pres, skin, test, mass, pedi, age])
    
    output = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    
    if output[0] == 0:
        print('person is not diabatic')
        return render_template('nodiabetic.html')
    else:
        print("person is diabatic! Eat healthy and stay healthy! Avoid Sugar")
        return render_template('diabteic.html')
    
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/blackbox")
def blackbox():
    return render_template("blackbox.html")

@app.route("/courses")
def course():
    return render_template("courses.html")

@app.route("/reviews")
def reviews():
    return "Welcome to review page"

@app.route("/blog")
def blog():
    return "Welcome to blog page"

@app.route("/stories")
def stories():
    return "Welcome to stories page-horror"

# run application code(always at end)
