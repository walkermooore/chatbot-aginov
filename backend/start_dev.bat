@echo off
setlocal
cd /d "%~dp0"
call .venv\Scripts\activate
python manage.py migrate
python manage.py seed_knowledge
python manage.py runserver 0.0.0.0:8000
