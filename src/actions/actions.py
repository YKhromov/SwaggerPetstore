import requests

from src.Variables.TestVariables import *


def get_req(test_obj, link_param):
    response = requests.get('/'.join([test_link, obj_links[test_obj], str(link_param)]))
    return response


def get_req_param(test_obj, link_param, req_param):
    response = requests.get(
        '/'.join([test_link, obj_links[test_obj], str(link_param)]),
        params=req_param
    )
    return response


def put_reg(test_obj):
    response = requests.put(
        '/'.join([test_link, obj_links[test_obj], '']),
        json=payload_updt[test_obj]
    )
    return response


def del_req(test_obj, link_param):
    requests.delete('/'.join([test_link, obj_links[test_obj], str(link_param)]))
