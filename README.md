# Dextraflix

## To run application

On root folder, create a `.env` file like bellow:

```bash
FLASK_APP=main.py
FLASK_ENV=development
PYTHONPATH=$(pwd)
```

after that, execute the following:

```bash
docker-compose up -d
flask run
```

## Testing application

To test application install pytest on your venv.

```bash
pip install pytest coverage
```

to test:

```bash
pytest
```

to code coverage

```bash
coverage run -m pytest
coverage report
```

or

```bash
coverage run -m pytest
coverage html
```

and access: htmlcov/index.html

## Using it with docker-compose

If you are yelling "GIMME THAT SERVICE ALREADY!", fear not - there might be a
treat for you. You can use docker compose to build and start a fresh instance
of DextraFlix! Just execute:

```bash
docker-compose build
docker-compose start
```

And voilà! You are good to go! (except if there is any process using TCP port
5000 or another MongoDB instance already running or if you don't have Docker
installed in your machine - in this case you should check what you've done so
far, including thinking twice before yelling at friends for petty things, you
spoiled brat).
