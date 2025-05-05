from flask import *
from flask_mail import*
from random import *

app=Flask(__name__)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'codingaltestmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'ojoukrigdwnofixq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

code=randint(101010,280469)

@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]
    msg = Message('OTP', sender='anyone@gmail.com', recipients=[email])
    msg.body = (mail)
    mail.send(msg)
    return render_template('page.html')
@app.route('/validate', methods=["POST"])
def validate():
    user_otp = request.form["otp"]
    if mail == int(user_otp):
        return "<h4>Email verification successful</h4>"
    else:
        return "<h4>VERIFICATION FAILED</h4>"
    
@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080, debug=True)