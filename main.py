import sys
import os
from dotenv import load_dotenv
from pathlib import Path

from create_repo import create_local_repo, create_remote_repo

root = Path(os.getcwd())
env_path = root / '.env'
load_dotenv(dotenv_path=env_path)

project_name = str(sys.argv[1])
prog_lang = str(sys.argv[2])
# path to projects directory in .env file
dir_path = Path(os.getenv('PROJECT_PATH'))
# github token stored in .env file
token = os.getenv('GITHUB_TOKEN')


def main():
    # check if project to create is local or remote
    # if number of arguments is 3, create remote repo
    if len(sys.argv) == 4:
        create_remote_repo()
        print("initialising remote repo")
    else:
        create_local_repo(root, dir_path, project_name, prog_lang)


if __name__ == "__main__":
    main()
