from utils.config_utils import ONTOP_SH_CLINICAL_DATA, ONTOP_SH_LOCAL_DIC, ONTOP_SH_MAPPINGS, ONTOP_SH_STANDARD_DIC
from flask import Flask, render_template, request
from flask_cors import CORS
from utils.RDB2RDF_utils import execute_ontop_materialize, create_properties_file
from utils.models import execute_chosen_model

# Initialize Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

@app.route('/home', methods=['GET',])
def index():
    return render_template('index.html')

# creating the properties file
@app.route('/create_properties_file', methods=['POST'])
def run_execute_ontop_materialize():
        jdbc_name = request.form['jdbc_name']
        jdbc_url = request.form['jdbc_url']
        jdbc_user = request.form['jdbc_user']
        jdbc_password = request.form['jdbc_password']
        create_properties_file(jdbc_name, jdbc_url, jdbc_user, jdbc_password)           
        return render_template('success_properties.html')  

@app.route('/ontop/<connection_type>', methods = ['GET', 'POST'])

def ontop_connection(connection_type):
    ontop_files = {
        "clinical": ONTOP_SH_CLINICAL_DATA,
        "local_dic": ONTOP_SH_LOCAL_DIC, 
        "standard_dic": ONTOP_SH_STANDARD_DIC,
        "mappings": ONTOP_SH_MAPPINGS
    }
    try:
        execute_ontop_materialize(ontop_files[connection_type])
        return render_template("transformation_success.html")
    except Exception as e:
        return render_template("error_ontop.html", error_message = f"An error occurred: {str(e)}")

@app.route('/execute_chosen_model', methods=['POST'])
def create_final_tables():
    chosen_model = request.form['chosen_model']
    execute_chosen_model(chosen_model)
    return render_template("transformation_success.html")




