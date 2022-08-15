import numpy as np
import sys
import os
from dotenv import load_dotenv
from pathlib import Path


env_path = "D:\ML_DL_CV\Windows_Batch\.env"
load_dotenv(dotenv_path=env_path)

project_name = str(sys.argv[1])
prog_lang = str(sys.argv[2])
dir_path = Path(os.getenv('PROJECT_PATH'))
token = os.getenv('GITHUB_TOKEN')


def create_local_repo():
    proj_path = dir_path / project_name
    if os.path.exists(proj_path):
        print("Directory created")
    else:
        os.makedirs(proj_path)
    os.chdir(proj_path)
    os.system('git init')
    os.system(f'echo # {project_name} > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')
    os.system('code .')
    

def create_remote_repo():
    pass


if __name__ == "__main__":
    if len(sys.argv) == 4:
        create_remote_repo()
        print("initialising remote repo")
    
    create_local_repo()
