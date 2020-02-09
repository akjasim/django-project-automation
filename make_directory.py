import sys
import os

# Fetching project name and concatenating with '_project'.
# Say argument provided be 'foo', project_name would be foo_project.
project = sys.argv[1]
if not project:
    print("Please ensure that the project name is provided as the first argument. Also ensure that the project name doesn't contain spaces.")
    sys.exit()
project_name = project + '_project'

# Fetching path.
path = sys.argv[2]
if not path:
    path = False

# Creating directory.    
try:
    if path:
        exact_path = os.path.join(path, project_name)
    else:
        exact_path = os.path.join(os.getcwd(), project_name)
    os.mkdir(exact_path)
    print(f'Created Directory {exact_path}')
    sys.exit(200)
except FileExistsError:
    print('Directory already exists')
    sys.exit()
except OSError:
    print('Please re-check the path. If path contains space, mention the whole path in double quotes.')
    sys.exit()
