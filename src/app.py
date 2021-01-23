# flask_ngrok_example.py
from flask import Flask
from test import test_one
from test import test_new
from main import model

app = Flask(__name__)


testData, test_label, pred_label, number = test_one(model)



@app.route("/")
def welcome():
    output = "<h1>Welcome!</h1><br>Please add '/predict' to your browser line to see a test sample."
    return output
    
@app.route("/predict")
def predict():
    output = "<h1>Welcome!</h1><br>Please find below an overview of the testing.<br><br>An image has been selected for you with the following image number out of the CIFAR 10 test dataset: " + str(number) + "<br><br>Please add in your browser URL '/yourimage' to see your test image, out of the CIFAR 10 test dataset." + "<br><br>The model predicted the following category of the picture: " + str(pred_label) + "<br><br>The following category is the correct one: " + str(test_label)
    return output

@app.route("/enternumber")
def enternumber():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("<form action='#' method='post'><p>Enter a number:</p><p><input type='number' name='nm' /></p></form>")

@app.route("/<usr>")
def user(usr):
    testData, test_label, pred_label, number = test_new(model, int(usr))
    output = "<h1>Welcome!</h1><br>Please find below an overview of the testing.<br><br>An image that you have selected with the following image number out of the CIFAR 10 test dataset: " + str(number) + "<br><br>Please add in your browser URL '/yourimage' to see your test image, out of the CIFAR 10 test dataset." + "<br><br>The model predicted the following category of the picture: " + str(pred_label) + "<br><br>The following category is the correct one: " + str(test_label)
    return output

#working:
#@app.route("/newpredict")
#def newpredict():
#    testData, test_label, pred_label, number = test_new(model, 30)
#    output = "<h1>Welcome!</h1><br>Please find below an overview of the testing.<br><br>An image has been selected for you (randomly) with the following image number out of the CIFAR 10 test dataset: " + str(number) + "<br><br>Please add in your browser URL '/yourimage' to see your test image, out of the CIFAR 10 test dataset." + "<br><br>The model predicted the following category of the picture: " + str(pred_label) + "<br><br>The following category is the correct one: " + str(test_label)
#    return output
 
#Not working
#@app.route("/newpredict")
#def newpredict():
#    usernumber = 30
#    testData, test_label, pred_label, usernumber = test_new(model, usernumber)
#    output = "<h1>Welcome!</h1>><brYou selected: " + str(usernumber) + "<br><br>Please add in your browser URL '/yourimage' to see your test image, out of the CIFAR 10 test dataset." + "<br><br>The model predicted the following category of the picture: " + str(pred_label) + "<br><br>The following category is the correct one: " + str(test_label)
#    return output
     
                            

from flask import send_file

@app.route('/predict/yourimage')
def get_image():
    filename = 'test.png'
    return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
