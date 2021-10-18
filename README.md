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