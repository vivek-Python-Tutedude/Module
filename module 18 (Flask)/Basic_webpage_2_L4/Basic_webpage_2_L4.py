# IMPORTING
from flask import Flask # flask is module and Flask class

# INTERACTION
web = Flask(__name__) # Creating the object of class Flask # passing any constructor 

# MAPPING
@web.route('/')
@ web.route('/home') # we can use /home it will gives same result

# INPUT
def home() :
    return "Hii Everyone!!!"

# MAIN
if __name__ == "__main__" :
    web.run(debug=True) # debug will automaticaly reload the page
    
# http://127.0.0.1:5000/ == http://127.0.0.1:5000/home
# http://localhost:5000/home == 127.0.0.1:5000/home
# it means 127.0.0.1 == localhost