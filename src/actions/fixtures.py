import requests
import pytest

from src.Variables.TestVariables import *



@pytest.fixture()
def create_obj(request):
    response = requests.post(
        'https://petstore.swagger.io/v2/{}'.format(obj_links[request.param]),
        json=payload[request.param]
    )
    assert response.status_code == 200
    yield response.json()
    if request.param == 'user':
        requests.delete(
            'https://petstore.swagger.io/v2/{obj_link}/{obj_id}'.format(
                obj_link=obj_links[request.param],
                obj_id=payload[request.param]['username']
            )
        )
    else:
        requests.delete(
            'https://petstore.swagger.io/v2/{obj_link}/{obj_id}'.format(
                obj_link=obj_links[request.param],
                obj_id=response.json()["id"]
            )
        )
