import sys
from github import Github
import os

username = os.environ.get('github_user')
password = os.environ.get('github_pass')

project = sys.argv[1]
access = sys.argv[2]

try:
    user = Github(username, password).get_user()
    if access == 'private':
        repo = user.create_repo(project, private=True)
    else:
        repo = user.create_repo(project)
except:
    print('Repository creation failed. Please make sure you enter the correct credentials and also check whether a repository with this name already exists.')
    sys.exit()

print(f"Succesfully created repository {project}")
sys.exit(200)
