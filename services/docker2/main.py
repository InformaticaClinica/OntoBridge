# Import Libreries
from flask import Flask
from flask_cors import CORS, cross_origin
from app import rdf_to_owl, owl_to_ttl
import logging
from flask import jsonify


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Configura el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])



@app.route('/')
def rdf_to_owl_docker():
    try:
        rdf_to_owl()  # Function that creates the reg ontology with all clinical data

        input_owl = './data/Ontologies/OMOP_5.3/reg_datanex_test.owl'
        output_ttl = './data/Ontologies/OMOP_5.3/reg_datanex_test.ttl'

        owl_to_ttl(input_owl, output_ttl)

        # Return a success message
        logging.info('Conversion successful')

    except Exception as e:
        # Log the error
        logging.error(f"An error occurred: {e}")
        # Return an error message
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('adhoc'))
