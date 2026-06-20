import logging

# FUSEKI PARAMETERS
FUSEKI_URL = "http://10.0.0.6:3030/"
FUSEKI_DB_NAME = 'name1'

# DIRECOTIRES
PREPROCESSED_TABLES = "data/output/Pre-processing/"
POSTPROCESSED_TABLE = "data/output/Post-processing/"
VOLUME_PATH = './data/'

# LOGGING CONFIG
LOGGING_CONFIG = logging.basicConfig(level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[logging.StreamHandler()])

# ONTOP
ONTOP_DIRECTORY = "./ontop-cli-5.0.2"
ONTOP_SH_CLINICAL_DATA = "/ontop_materialize_clinical_data.sh"
ONTOP_SH_LOCAL_DIC = "/ontop_materialize_local_dic.sh"
ONTOP_SH_MAPPINGS = "/ontop_materialize_mappings.sh"
ONTOP_SH_STANDARD_DIC = "/ontop_materialize_standard_dic.sh"


