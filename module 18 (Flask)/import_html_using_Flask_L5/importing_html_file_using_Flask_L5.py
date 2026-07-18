# IMPORTING
from flask import Flask, render_template, request # flask is module and Flask class

# INTERACTION
web = Flask(__name__) # Creating the object of class Flask # passing any constructor 

# MAPPING
@web.route('/')
@ web.route('/register') 

# INPUT
def homepage() :
    return render_template('register.html')

@web.route("/confirmation", methods = ['POST', 'GET'])
# INPUTS
def register() :
    if request.method == "POST" :
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('Ph_no')
        return render_template('confirm.html', name = n, city = c, Ph_no = p )

# MAIN
if __name__ == "__main__" :
    web.run(debug=True) # debug will automaticaly reload the page
    
# http://127.0.0.1:5000/ == http://127.0.0.1:5000/home
# http://localhost:5000/home == 127.0.0.1:5000/home
# it means 127.0.0.1 == localhost
# folder name of the templates it must be same for storing the template