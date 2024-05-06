import requests
import os
import logging

# Configure logging to write informational and error messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_owl_fuseki(fuseki_url, ontologies_folder, new_dataset_name):
    """
    This function creates a new dataset in Apache Fuseki and uploads OWL files from a specified directory.
    Parameters:
        fuseki_url (str): The URL to the Fuseki server.
        ontologies_folder (str): Folder path containing OWL files.
        new_dataset_name (str): The name for the new dataset.
    """

    # Build URL for dataset creation and define the dataset properties
    create_dataset_url = f'{fuseki_url}/datasets'
    dataset_details = {
        'dbName': new_dataset_name,
        'dbType': 'mem'  # Memory store, not persistent
    }

    # Attempt to create the dataset on the Fuseki server
    try:
        response = requests.post(create_dataset_url, data=dataset_details)
        logging.info(f"Response URL: {response.url}")
        logging.info(f"Request Body: {response.request.body}")
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Text: {response.text}")
        if response.status_code in [201, 200]:
            logging.info(f"Dataset '{new_dataset_name}' successfully created on Fuseki.")
        else:
            logging.error(f"Failed to create dataset. Status code: {response.status_code}, {response.text}")
    except Exception as e:
        logging.error(f"Error creating dataset on Fuseki: {e}")

    # Find all OWL files in the specified folder
    owl_files = [f for f in os.listdir(ontologies_folder) if f.endswith('.owl')]
    if not owl_files:
        logging.info("No .owl files found in the specified folder.")
        return

    # Upload each OWL file to the newly created dataset on Fuseki
    for file in owl_files:
        owl_file_path = os.path.join(ontologies_folder, file)
        try:
            with open(owl_file_path, 'r', encoding='utf-8') as f:
                owl_data = f.read()
                dataset_url = f'{fuseki_url}/{new_dataset_name}/data?default'
                response = requests.post(dataset_url, data=owl_data.encode('utf-8'), headers={'Content-Type': 'application/rdf+xml; charset=utf-8'})
                if response.status_code == 200:
                    logging.info(f"File {file} successfully uploaded to Fuseki.")
                else:
                    logging.error(f"Failed to upload file {file}. Status code: {response.status_code}, {response.text}")
        except Exception as e:
            logging.error(f"Failed to read or upload file {file}: {e}")
