# Dextraflix

## To run application

On root folder

```bash
docker-compose up -d
export FLASK_APP=main.py
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