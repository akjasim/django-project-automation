@echo off
make_directory.py "%~1" "%~2"
if %ERRORLEVEL% NEQ 200 (
    EXIT /B 1
)
D:
cd %~2\%~1_project
echo Creating virtual environment...
virtualenv venv
django-admin startproject %~1
cd %~1
make_repository.py "%~1" "%~3"
if %ERRORLEVEL% NEQ 200 (
    EXIT /B 1
)
git init
git remote add origin https://github.com/%github_user%/%~1.git
git add .
git commit -m "first commit"
git push -u origin master
call ../venv/Scripts/activate
pip install django
echo !!! Happy Coding !!!
echo Have a look at https://jasim.tech/
start chrome 127.0.0.1:8000
python manage.py runserver
