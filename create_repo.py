import os
from pathlib import Path
import shutil
from subprocess import Popen, check_call

from github import Github


def create_project_dir(root, dir_path, project_name, prog_lang):
    '''
    create local project directory
    '''

    # concatenate project path and project name to get full path
    proj_path = dir_path / project_name

    # create project directory
    if os.path.exists(proj_path):
        print("Directory created")
    else:
        os.makedirs(proj_path)
    
    # set path to .gitignore file
    dst = proj_path / '.gitignore'
    # check type of prog_lang and copy .gitignore file
    if prog_lang in ['python', 'py', 'p']:
        src = root / "gitignores/python.gitignore"
        shutil.copy(src, dst)
    elif prog_lang in ['unity', 'un', 'u']:
        src = root / "gitignores/unity.gitignore"
        shutil.copy(src, dst)


def _check_and_format_path(path):
    '''
    check if path contains any spaces and if it does,
    enclose it in double quotes
    '''

    if ' ' in path:
        path = path.split('\\')
        path = '/'.join(path)
        path = f'"{path}"'
    return path


def _check_and_open_app(proj_path, prog_lang):
    # check type of prog_lang and open the application
    if prog_lang in ['python', 'py', 'p']:
        # open VS Code for python project
        Popen('code .', shell=True)
    elif prog_lang in ['unity', 'un', 'u']:
        # get path to Unity editor application from .env file
        unity_path = _check_and_format_path(os.getenv('UNITY_PATH'))
        p_path = _check_and_format_path(str(proj_path))
        if unity_path != None:
            # open Unity editor for project
            Popen(f'{unity_path} -createProject {p_path}', shell=True)
        else:
            print("Please provide the path to Unity Editor")


def create_local_repo(dir_path, project_name, prog_lang):
    '''
    create local repo
    '''

    # concatenate project path and project name to get full path
    proj_path = dir_path / project_name    
    # change directory to project directory
    os.chdir(proj_path)

    commands = [
        f'echo # {project_name} > README.md',
        'git init',
        'git add .',
        'git commit -m "Initial commit"',
    ]
    # create README file and initial commit
    for c in commands:
        check_call(c, shell=True)

    _check_and_open_app(proj_path, prog_lang)


def create_remote_repo(token, dir_path, project_name, prog_lang):
    '''
    create remote repo
    '''

    # concatenate project path and project name to get full path
    proj_path = dir_path / project_name    
    # change directory to project directory
    os.chdir(proj_path)

    # initialize Github instance
    g = Github(token)
    user = g.get_user()
    login = user.login
    # create repository
    repo = user.create_repo(project_name, private=True)

    commands = [
        f'echo # {repo.name} > README.md',
        'git init',
        f'git remote add origin https://github.com/{login}/{project_name}.git',
        'git add .',
        'git commit -m "Initial commit"',
        'git push -u origin master'
    ]
    # create README file and initial commit
    for c in commands:
        check_call(c, shell=True)
    
    _check_and_open_app(proj_path, prog_lang)
