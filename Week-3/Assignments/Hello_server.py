import os, json
from flask import Flask, request, render_template, redirect, url_for, make_response
from werkzeug.wrappers import response

template_dir = os.path.abspath('../static')
app = Flask(__name__, template_folder=template_dir)
tempCookieValue =0

@app.route('/')
def hello_world():
    return 'Hello, My Server!'
    
@app.route('/sum.html')
def sum():
    return render_template("sum.html")

@app.route('/data', methods=['GET'])
def number():
        try:
            number = request.args.get('number',type = int)
            if number is None:
                return "Lack of Parameter"
            sum = 0
            for item in range (1,number+1):
                sum+=item
            return str(sum)
        except TypeError:
            return "Wrong Parameter"

@app.route('/myName', methods = ['POST','GET'])
def myName():
    nameCheck = request.cookies.get('userID')
    if nameCheck is not None:
        return "welcome"+str(nameCheck)
    else:
        if request.method == "POST":
            userNM = request.form["nm"]
            response = make_response("cookies.html")
            response.set_cookie("username", userNM)
            page = request.args.get('name', default='*',type=str)
            return redirect(url_for("user", name= userNM))
            
        else:
            return render_template('cookies.html')

@app.route("/trackName", methods=["GET","POST"])
def user():
        response = make_response("cookies.html")
        response.set_cookie("username",  )
        return response
        
    

if __name__ == '__main__':
    app.run(debug = True,host='localhost', port=3000)