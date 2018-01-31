import falcon
from falcon import testing
import pytest

from things.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_list_images(client):
    doc = {
        'images': [
            {
                'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
            }
        ]
    }

    response = client.simulate_get('/images')

    assert response.status == falcon.HTTP_OK
