# IMPORTING
from flask import Flask, render_template
import os

# INTERACTION
app = Flask(__name__)  # Creating the object of class Flask # passing any constructor 

picfolder = os.path.join("static")

app.config['upload_folder'] = picfolder

# MAPPING
@app.route('/')

#INPUTS
def first(): 
    pic = os.path.join(app.config['upload_folder'], 'waterfall.jpg')
    return render_template("home.html", user_image = pic)        
    
"""def first(): 
    return render_template("home.html")        
"""
"""@app.route('/second')

#INPUTS
def second(): 
    return "Welcome to the second page"
        """
@app.route('/second')
#INPUTS
def second(): 
    return render_template("second.html")
        
# MAIN
if __name__ == '__main__' :
    app.run()
    
# http://127.0.0.1:5000/ == http://127.0.0.1:5000/home
# http://localhost:5000/home == 127.0.0.1:5000/home
# it means 127.0.0.1 == localhost
# folder name of the templates it must be same for storing the template