from flask import Flask
from cliente import cliente  

app = Flask(__name__)


app.register_blueprint(cliente) 

@app.route('/', methods=['GET'])
def hello():
    return 'Hola mundo'

if __name__ == "__main__": 
    app.run(host = 'localhost', debug = True, port = 5003)  
