# Dextraflix

## To run application

On root folder, create a `.env` file like bellow:

```bash
FLASK_APP=main.py
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
