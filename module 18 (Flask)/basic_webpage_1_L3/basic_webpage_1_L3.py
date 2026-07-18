from flask import Flask # flask is module and Flask class

web = Flask(__name__) # Creating the object of class Flask # passing any constructor 

@web.route('/')

def home() :
    return "welcome"

if __name__ == "__main__" :
    web.run(debug=True) # debug will automaticaly reload the page