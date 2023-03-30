# Flask
Учебный проект на базе framework Flask «блог с возможностью регистрации и публикации статей».

Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий
набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых
микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих
лишь самые базовые возможности.

## Стек

- Python = 3.8.10
  - isort, black, autoflake
  - Django < 3.2.8   
  - Flsk = 2.2.3
- VSCode
- SQLite 3

## Лицензия 

MIT

## Install 
1. Create new virtual env

python3 -m venv ./venv

2. copy `example.env` to `.env` and set `SECRET_KEY`
3. activate virtual env

source venv/bin/activate

4. install dependencies

5. Run command for init db and create user

flask init-db
flask create-init-user

6. Run flask application

flask run
