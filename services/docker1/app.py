import subprocess
def execute_ontop_materialize():

    
    subprocess.run(['chmod', '777', './ontop-cli-5.0.2'])
    subprocess.run(['ls', 'data/'])
    script_path = './ontop-cli-5.0.2/ontop_materialize.sh'
    subprocess.run(['sh', script_path])
