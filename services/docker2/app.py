import glob  # For file path pattern matching
import rdflib  # RDF library to manipulate RDF graphs
import logging  # For logging info, warnings, and errors

# Configure logging level
logging.basicConfig(level=logging.INFO)

def rdf_to_owl():
    # Log the beginning of the RDF to OWL conversion process
    logging.info('Starting RDF to OWL conversion process')
    
    # Globbing to find all Turtle (.ttl) files in the 'data' directory
    rdf_files = glob.glob('./data/*.ttl')
    logging.info(f'Found {len(rdf_files)} RDF files.')
    
    # Globbing to find all OWL files in the specified ontology directory
    owl_files = glob.glob('./data/Ontologies/OMOP_5.3/*.owl')
    logging.info(f'Found {len(owl_files)} OWL files.')

    # Create an empty graph using rdflib to aggregate our RDF data
    total_graph = rdflib.Graph()
    logging.info('Created a new empty RDF graph.')

    # Loop over each OWL file path and parse them into the graph
    for path in owl_files:
        total_graph.parse(path, format='xml')
        logging.info(f'Parsed OWL file: {path}')
    
    # Log the completion of OWL file parsing
    logging.info('All OWL files have been added to the graph.')

    # Loop over each RDF file path and parse them into temporary graphs
    for path in rdf_files:
        graph_rdf = rdflib.Graph()
        graph_rdf.parse(path, format='ttl')
        logging.info(f'Parsed RDF file: {path}')
        
        # Merge the temporary RDF graph into the main graph
        for subject, predicate, obj in graph_rdf:
            total_graph.add((subject, predicate, obj))
        logging.info(f'Merged graph of {path} into the main graph.')

    # Log the completion of RDF file parsing and merging
    logging.info('All RDF data has been added to the graph.')

    # Serialize and save the graph to an OWL file
    total_graph.serialize("./data/Ontologies/OMOP_5.3/reg_datanex_test.owl", format="xml")
    logging.info('Graph serialization complete. Output file created.')

    # Final completion log
    logging.info('RDF to OWL conversion process finished.')

def owl_to_ttl(input_path, output_path):
    try:
        # Load the OWL file into an RDF graph
        graph = rdflib.Graph()
        graph.parse(input_path, format='xml')
        logging.info(f'Loaded OWL file: {input_path}')

        # Serialize the graph to Turtle format and save to file
        graph.serialize(destination=output_path, format='turtle')
        logging.info(f'Converted OWL file saved to TTL format at: {output_path}')

    except Exception as e:
        logging.error(f'An error occurred: {e}')