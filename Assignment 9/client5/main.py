# get the Flask class imported
from flask import Flask, request
import pickle

# create an application of Flask
app = Flask(__name__)


@app.route("/")
def root():
    return """
    <html>
        <body>
            <h1>Welcome to my Machine Learning Application</h1>
            <p>This is a machine learning application to predict the 
            test result of a hearing test based on age and physical score.</p>
            <form action="/predict" method="POST">
                <div>
                    <label>Hair</label>
                    <input type="number" name="Hair">
                </div>
                <div>
                    <label>Feathers</label>
                    <input type="number" name="Feathers">
                </div>
                <div>
                    <label>Eggs</label>
                    <input type="number" name="Eggs">
                </div>
                <div>
                    <label>Milk</label>
                    <input type="number" name="Milk">
                </div>
                <div>
                    <label>Airborne</label>
                    <input type="number" name="Airborne">
                </div>
                <div>
                    <label>Aquatic</label>
                    <input type="number" name="Aquatic">
                </div>
                <div>
                    <label>Predator</label>
                    <input type="number" name="Predator">
                </div>
                <div>
                    <label>Toothed</label>
                    <input type="number" name="Toothed">
                </div>
                <div>
                    <label>Backbone</label>
                    <input type="number" name="Backbone">
                </div>
                <div>
                    <label>Breathes</label>
                    <input type="number" name="Breathes">
                </div>
                <div>
                    <label>Venomous</label>
                    <input type="number" name="Venomous">
                </div>
                <div>
                    <label>fins</label>
                    <input type="number" name="fins">
                </div>
                <div>
                    <label>legs</label>
                    <input type="number" name="legs">
                </div>
                <div>
                    <label>tail</label>
                    <input type="number" name="tail">
                </div>
                <div>
                    <label>domestic</label>
                    <input type="number" name="domestic">
                </div>
                <div>
                    <label>catsize</label>
                    <input type="number" name="catsize">
                </div>
                <div>
                    <input type="submit" value="Predict">
                </div>
            </form>
        </body>
    </html>
    """


@app.route("/predict", methods=["POST"])
def predict():
    hair = request.form['Hair']
    feathers = request.form['Feathers']
    eggs = request.form['Eggs']
    milk = request.form['Milk']
    airborne = request.form['Airborne']
    aquatic = request.form['Aquatic']
    predator = request.form['Predator']
    toothed = request.form['Toothed']
    breathes = request.form['Breathes']
    backbone = request.form['Backbone']
    venomous = request.form['Venomous']
    fins = request.form['fins']
    legs = request.form['legs']
    tail = request.form['tail']
    domestic = request.form['domestic']
    catsize = request.form['catsize']

    # load the model from model.pkl file
    with open('./model.pkl', 'rb') as file:
        model = pickle.load(file)

    # get the prediction using model
    prediction = model.predict([[hair,feathers,eggs,milk,airborne,aquatic,predator,toothed,backbone,breathes,venomous,fins,legs,tail,domestic,catsize]])
    print(f"prediction = {prediction}")

    # if prediction[0] == 1:
    #     result = "Pass"
    # else:
    #     result = "Fail"
    #
    # print(f"age = {age}, score = {score}")
    return f"""
    <html>
        <body>
            <h1>Prediction Result</h1>
            <p>Based on your age and physical score, we have predicted
            your hearing test result as: {prediction}</p>
        </body>
    </html> 
    """


# start the application
app.run(host="0.0.0.0", port=4000, debug=True)