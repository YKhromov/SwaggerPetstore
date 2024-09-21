from src.actions.actions import *
from src.actions.fixtures import *
from src.Variables.TestVariables import *

test_obj = 'order'

@pytest.mark.parametrize('create_obj', ['pet'], indirect=True)
class TestStoreAPI:
    def test_store_inventory_status(self, create_obj):
        test_obj = 'pet'
        response = requests.get('https://petstore.swagger.io/v2/store/inventory').json()
        cur_stat_amount = response[payload[test_obj]['status']]
        cur_updt_stat_amount = response.get(payload_updt[test_obj]['status'])
        if cur_updt_stat_amount is None:
            cur_updt_stat_amount = 0

        payload_updt[test_obj]['id'] = create_obj['id']
        put_reg(test_obj)
        new_response = requests.get('https://petstore.swagger.io/v2/store/inventory').json()
        new_updt_stat_amount = new_response[payload_updt[test_obj]['status']]
        new_stat_amount = new_response.get(payload[test_obj]['status'])
        if new_stat_amount is None:
            new_stat_amount = 0
        assert new_stat_amount == cur_stat_amount - 1
        assert new_updt_stat_amount == cur_updt_stat_amount + 1

@pytest.mark.parametrize('create_obj', [test_obj], indirect=True)
class TestOrderAPI:
    def test_create_order(self, create_obj):
        req_params = params_to_check[test_obj]
        for i_param in req_params:
            assert create_obj[i_param] == payload[test_obj][i_param]

    def test_get_order_by_id(self, create_obj):
        response = get_req(test_obj, create_obj['id']).json()
        assert response == create_obj

    def test_delete_order(self, create_obj):
        del_req(test_obj, create_obj['id'])
        response = get_req(test_obj, create_obj['id'])
        assert response.status_code == 404
