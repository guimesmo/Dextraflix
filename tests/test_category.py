from flask import Flask
import os
import tempfile
import pytest
import json

from Dextraflix.views.categoria import categorias_bp

def test_category_list():
    app = Flask(__name__)
    app.register_blueprint(categorias_bp)
    client = app.test_client()
    response = client.get('/categorias/')

    assert 200 == response.status_code

def test_not_found_category():
    app = Flask(__name__)
    app.register_blueprint(categorias_bp)
    client = app.test_client()

    response = client.get('/categorias/notfound')

    assert 404 == response.status_code

def test_add_category():
    app = Flask(__name__)
    app.register_blueprint(categorias_bp)
    client = app.test_client()

    request_data = {
        'nome': 'unittest1',
        'descricao': 'Unit Test 1'
    }

    request_headers = {
        'Content-Type': 'application/json'
    }

    response = client.put('/categorias/', data=json.dumps(request_data), headers=request_headers)

    assert 200 == response.status_code

def test_update_category():
    app = Flask(__name__)
    app.register_blueprint(categorias_bp)
    client = app.test_client()

    request_data = {
        'nome': 'unittest1-updated',
        'descricao': 'Unit Test 1 - updated'
    }

    request_headers = {
        'Content-Type': 'application/json'
    }

    response = client.post('/categorias/unittest1', data=json.dumps(request_data), headers=request_headers)

    assert 200 == response.status_code

def test_delete_category():
    app = Flask(__name__)
    app.register_blueprint(categorias_bp)
    client = app.test_client()

    response = client.delete('/categorias/unittest1-updated')

    assert 200 == response.status_code