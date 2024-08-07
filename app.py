from flask import Flask, render_template,request, flash
from flask_sqlalchemy import SQLAlchemy
import datetime
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] ='123'
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))



@app.route("/",methods=["GET","POST"])
def index():
    print(request.method)
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        date = request.form.get("date")
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        occupation = request.form.get("occupation")
        
        form = Form(first_name=first_name,last_name=last_name,email=email,date=date,occupation=occupation)
        db.session.add(form)
        db.session.commit()
        flash(f"{first_name}, your form was submitted","success")
    
        print(first_name,last_name,email,date,occupation)
       
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)