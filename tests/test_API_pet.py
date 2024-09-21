from src.actions.actions import *
from src.actions.fixtures import *
from src.Variables.TestVariables import *

test_obj = 'pet'


class TestPetAPInoParam:
    def test_get_not_exst_pet(self):
        response = get_req(test_obj, '1')
        assert response.status_code == 404


@pytest.mark.parametrize('create_obj', [test_obj], indirect=True)
class TestPetAPI:
    def test_create_pet(self, create_obj):
        req_params = params_to_check[test_obj]
        for i_param in req_params:
            assert create_obj[i_param] == payload[test_obj][i_param]

    def test_get_pet_by_id(self, create_obj):
        response = get_req(test_obj, create_obj['id']).json()
        assert response == create_obj

    def test_update_pet(self, create_obj):
        payload_updt[test_obj]['id'] = create_obj['id']
        response = put_reg(test_obj).json()
        assert response == payload_updt[test_obj]

    def test_delete_pet(self, create_obj):
        del_req(test_obj, create_obj["id"])
        response = get_req(test_obj, create_obj["id"])
        assert response.status_code == 404

    def test_get_pet_by_status(self, create_obj):
        pet_list = get_req_param(
            test_obj,
            'findByStatus',
            {'status': create_obj['status']}
        ).json()
        assert pet_list != []

        is_present = False
        for i_pet in pet_list:
            assert i_pet['status'] == create_obj['status']

            if i_pet['id'] == create_obj['id']:
                is_present = True
                req_params = ['name', 'photoUrls', 'status']
                for i_param in req_params:
                    assert create_obj[i_param] == payload[test_obj][i_param]

        assert is_present
