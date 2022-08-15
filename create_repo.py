import os
from pathlib import Path
import shutil
from subprocess import Popen, check_call


def check_and_format_path(path):
    '''
    check if path contains any spaces and if it does,
    enclose it in double quotes
    '''
    if ' ' in path:
        path = path.split('\\')
        path = '/'.join(path)
        path = f'"{path}"'
    return path


def create_local_repo(root, dir_path, project_name, prog_lang):
    ''' create local repo '''

    # concatenate project path and project name to get full path
    proj_path = dir_path / project_name

    # create project directory
    if os.path.exists(proj_path):
        print("Directory created")
    else:
        os.makedirs(proj_path)
    
    # change directory to project directory
    os.chdir(proj_path)

    # set path to .gitignore file
    dst = proj_path / '.gitignore'
    # check type of prog_lang and copy .gitignore file
    if prog_lang in ['python', 'py', 'p']:
        src = root / "gitignores/python.gitignore"
        shutil.copy(src, dst)
        # open VS Code for python project
        Popen('code .', shell=True)
    elif prog_lang in ['unity', 'un', 'u']:
        src = root / "gitignores/unity.gitignore"
        shutil.copy(src, dst)

        # get path to Unity editor application from .env file
        unity_path = check_and_format_path(os.getenv('UNITY_PATH'))
        p_path = check_and_format_path(str(proj_path))
        if unity_path != None:
            # open Unity editor for project
            check_call(f'{unity_path} -createProject {p_path}', shell=True)
        else:
            print("Please provide the path to Unity Editor")
    
    # create README file and initial commit
    Popen(f'echo # {project_name} > README.md', shell=True)
    check_call('git init', shell=True)
    check_call('git add .', shell=True)
    check_call('git commit -m "first commit"', shell=True)


def create_remote_repo():
    pass