import os
import requests

def load_owl_fuseki(fuseki_url, ontologies_folder, new_dataset_name):
    dataset_url = f'{fuseki_url}{new_dataset_name}/data?default'

    # Filter OWL and TTL files
    ontology_files = [os.path.join(ontologies_folder, f) 
                      for f in os.listdir(ontologies_folder) if f.endswith(('.owl', '.ttl'))]

    for file_path in ontology_files:
        # Determine content type based on file extension
        if file_path.endswith('.owl'):
            content_type = 'application/rdf+xml; charset=utf-8'
        elif file_path.endswith('.ttl'):
            content_type = 'text/turtle; charset=utf-8'
        else:
            continue  # This should not happen, but kept for safety

        # Read the file and send it to Fuseki
        with open(file_path, 'r', encoding='utf-8') as f:
            ontology_data = f.read()
            dataset_url = f'{fuseki_url}{new_dataset_name}'
            response = requests.post(dataset_url, data=ontology_data.encode('utf-8'),
                                     headers={'Content-Type': content_type})

            # Check server response
            if response.status_code == 200:
                print(f"File {file_path} loaded successfully into {dataset_url}")
            else:
                print(f"Error loading {file_path}: {response.status_code} - {response.text}")
