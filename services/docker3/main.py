# IMPORTS 
from flask import Flask
from flask_cors import CORS, cross_origin
import logging
from src.preprocessing.send_query import get_query
from src.postprocessing.post_omop import post_omop
from src.Load_owl_fuseki import load_owl_fuseki

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])

@app.route('/')
def querys_and_postpro():   

    fuseki_url = "http://10.0.0.6:3030/"
    ONTOLOGY_FOLDER = "data/Ontologies/OMOP_5.3"
    new_dataset_name = 'name1'

    READ_FOLDER = "data/output/Pre-processing/"
    WRITE_FOLDER = "data/output/Post-processing/"

    load_owl_fuseki(fuseki_url, ONTOLOGY_FOLDER, new_dataset_name)
    
    get_query(READ_FOLDER)
    post_omop(READ_FOLDER, WRITE_FOLDER)

    return 'Query_docker'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('adhoc'))
