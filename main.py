import sys
import os
from dotenv import load_dotenv
from pathlib import Path

import create_repo as cr


root = Path(os.getcwd())
env_path = root / '.env'
load_dotenv(dotenv_path=env_path)

# python main.py <project_name> <prog_lang> <remote>
project_name = str(sys.argv[1])
prog_lang = str(sys.argv[2])
# path to projects directory in .env file
dir_path = Path(str(sys.argv[3]))
# github token stored in .env file
token = os.getenv('GITHUB_TOKEN')


def main():
    cr.create_project_dir(root, dir_path, project_name, prog_lang)
    # check if project to create is local or remote
    # if number of arguments is 3, create remote repo
    if len(sys.argv) == 5:
        print("Initialising remote repo")
        cr.create_remote_repo(token, dir_path, project_name, prog_lang)
    else:
        cr.create_local_repo(dir_path, project_name, prog_lang)


if __name__ == "__main__":
    main()
