from .config_utils import ONTOP_DIRECTORY
import logging
import subprocess

def create_properties_file(jdbc_name, jdbc_url, jdbc_user, jdbc_password):

    properties_content = f"""
jdbc.name={jdbc_name}
jdbc.url={jdbc_url}
jdbc.user={jdbc_user}
jdbc.password={jdbc_password}
    """
    with open('data/ontobridge.properties', 'w') as file:
        file.write(properties_content)
        
def execute_ontop_materialize(ontop_sh_file):
    logging.info('EXECUTING THE ONTOP MATERIALIZE COMMAND:')
    try:
        logging.info('Setting read/write permissions for the ONTOP directory.')
        subprocess.run(['chmod', '-R', '777', ONTOP_DIRECTORY], check=True)
        logging.info('Permissions set successfully.')

        logging.info('List of the contents of the data/ directory:')
        subprocess.run(['ls', 'data/'], check=True)

        logging.info(f'Executing ONTOP script: {ontop_sh_file}')
        subprocess.run(['sh', ONTOP_DIRECTORY + ontop_sh_file], check=True)

    except subprocess.CalledProcessError as e:
        error_message = f'Error executing a command: {e.stderr or e}'
        logging.error(error_message)
        raise Exception(error_message) 
    except Exception as e:
        error_message = f'Unexpected error: {e}'
        logging.error(error_message)
        raise Exception(error_message) 
