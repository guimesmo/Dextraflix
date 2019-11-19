from flask import Flask
import os
import tempfile
import pytest

from Dextraflix.views.categoria import categorias_bp

def test_empty_category_list():
    app = Flask(__name__)
    app.register_blueprint(categorias_bp)
    client = app.test_client()
    response = client.get('/categorias/')

    assert 200 == response.status_code
    assert [] == response.get_json()
