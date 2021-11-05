from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/never")
def never():
    return render_template("never.html")

@app.route("/html")
def html():
    return render_template("html.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/web")
def web():
    return render_template("web.html")
    
@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/contact',methods=['POST','GET'])
def result():
    if request.method=='POST':
        contact=request.form
        return render_template('contact.html',result=result)

if __name__=="__main__":
    app.run(debug=True)