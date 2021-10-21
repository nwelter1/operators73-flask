# Day 1

## Topics Covered
- Basic Flask Setup/Config
- Blueprints
- Templates
- Routes
- Dynamic Routes
- Static files

## Start Flask App
- Creating/Activating virtualenv:
    - Windows
        - `pyton -m venv <nameofvenv>`
        - `<nameofvenv>\Scripts\activate`
    - Mac
        - `python -m venv <nameofvenv>`
        - `source <nameofvenv>/bin/activate`
- Installing Flask into virtualenv
    - `pip install flask`
- Add flask environment variables:
    - Windows
        - `set FLASK_ENV=development`
        - `set FLASK_APP=<NAME-OF-PROJECT>(ie drone_inventory)`
    - Mac
        - `export FLASK_ENV=development`
        - `export FLASK_APP=<NAME-OF-PROJECT>(ie drone_inventory)`

[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/ "Main Flask Docs")

[Flask Blueprint Docs](https://flask.palletsprojects.com/en/1.1.x/blueprints/ "Flask Blueprint Docs")

# Day 2
Topics Covered:
- Flask Forms with Flask-WTF
- Getting Data from a form
- Rendering a form to HTML
- Creating Models
- Migrating Models
- Using Environment variables with `.env`

## Flask-Migrate Commands
- Initialize an empty migrations repo: `flask db init`
- Stage new model changes: `flask db migrate -m "<message>"`
- 'Push' changes to create new tables: `flask db upgrade`

## Python Packages
Flask-WTF: `pip install Flask-WTF`
Flask SQLAlchemy: `pip install Flask-SQLAlchemy`
Flask Migrate: `pip install Flask-Migrate`
Python-dotenv: `pip install python-dotenv`
psycopg2: `pip install psycopg2` (or for mac: `pip install psycopg2-binary==2.8.6`)
Email_Validator: `pip install email_validator`


# Day 3

## Topics Covered
- User authentication
- Protected Routes
- User sessions
- Flash Messaging
- Conditional formatting (Jinja 'if' statements)

## Python Packages
- Flask Login: `pip install flask-login`

# Day 4

## Topics Covered
- Token validation
- Creating custom wrappers (decorators)
- Helper functions
- Data marshalling

- CRUD Operations (Request Methods)
    - CREATE (POST)
    - RETRIEVE (GET)
    - UPDATE (POST, PUT)
    - DELETE (DELETE)

## Python Packages
- Flask Marshmallow: `pip install Flask-Marshmallow`
- Flask-Cors: `pip install Flask-Cors`