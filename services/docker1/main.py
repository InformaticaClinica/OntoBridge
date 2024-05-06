# Import Libreries
from flask import Flask
from flask_cors import CORS, cross_origin
from app import execute_ontop_materialize

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def ontop_docker(): # function that is executed when making the request https://localhost:5002/

    execute_ontop_materialize() # function that runs the ontop_materialize.sh in the ontop-cli-5.0.2 directory
    
    return 'Ontop Docker' # Control Return

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('adhoc'))
