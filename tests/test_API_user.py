from src.actions.actions import *
from src.actions.fixtures import *
from src.Variables.TestVariables import *

test_obj = 'user'


@pytest.mark.parametrize('create_obj', [test_obj], indirect=True)
class TestUserAPI:
    def test_get_user(self, create_obj):
        response = get_req(test_obj, payload[test_obj]['username']).json()
        req_params = params_to_check[test_obj]
        for i_param in req_params:
            assert response[i_param] == payload[test_obj][i_param]

    def test_delete_user(self, create_obj):
        del_req(test_obj, payload[test_obj]['username'])
        response = get_req(test_obj, payload[test_obj]['username'])
        assert response.status_code == 404

    def test_login(self, create_obj):
        response = get_req_param(
            test_obj,
            'login',
            {
                'username': payload[test_obj]['username'],
                'password': payload[test_obj]['username']
            }
        )
        assert response.status_code == 200
        assert 'logged in user session' in response.json()['message']


class TestUserAPInoParam:
    def test_create_user(self):
        response = requests.post(
            'https://petstore.swagger.io/v2/user',
            json=payload['user']
        )
        assert response.status_code == 200
        assert response.json()['message'] > '0'
        del_req(test_obj, payload[test_obj]['username'])

    def test_create_user_list(self):
        test_obj = 'user_list'
        response = requests.post(
            'https://petstore.swagger.io/v2/user/createWithList',
            json=payload[test_obj]
        )
        assert response.status_code == 200
        for i_user in payload[test_obj]:
            del_req('user', i_user['username'])
