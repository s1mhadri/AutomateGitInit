# Project creation and github upload automation 

### Setup: 
```bash
git clone "https://github.com/simhadri-hs/AutomateGitInit.git"
cd AutomateGitInit
pip install -r requirements.txt

path:
Add "AutomateGitInit" folder directory to PATHS

create env vars :
> projects directory as    - "PROJECT_PATH"
> Github token as          - "GITHUB_TOKEN"
> (optional) unity path as - "UNITY_PATH"
```

### Usage:
```
Command to run the program type

'projinit <project_name> <project_type> <r>' - for remote repository
'projinit <project_name> <project_type>'     - for local repository
```
**Note**: ```<project_type>``` - python/py/p or unity/un/u
