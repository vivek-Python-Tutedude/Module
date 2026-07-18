# IMPORTING
from flask import Flask, render_template
import os

# INTERACTION
app = Flask(__name__)  # Creating the object of class Flask # passing any constructor 

# MAPPING
@app.route('/')

#INPUTS
def first(): 
    return render_template("index.html")   
    
# index template is inherit the property of base tempale

# MAIN
if __name__ == '__main__' :
    app.run()
    
# http://127.0.0.1:5000/ == http://127.0.0.1:5000/home
# http://localhost:5000/home == 127.0.0.1:5000/home
# it means 127.0.0.1 == localhost
# folder name of the templates it must be same for storing the template