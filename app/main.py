"""Provide Flask application."""
from flask import Flask
from kubernetes import client
from kubernetes.client import rest
from pprint import pprint

from app import development


# TODO: MOVE TO MODULE
if (development):
    ssl_ca_cert_file = 'ca.pem'
    authorization_file = 'authorization.txt'
    with open('host.txt', 'r') as f:
        host = f.read().strip()
else:  # TODO FIX
    ssl_ca_cert_file = 'ca.pem'
    authorization_file = 'authorization.txt'
    host = 'https://35.247.94.9'
with open(authorization_file, 'r') as f:
    authorization = f.read().strip()
configuration = client.Configuration()
configuration.api_key['authorization'] = authorization
configuration.api_key_prefix['authorization'] = 'Bearer'
configuration.ssl_ca_cert = ssl_ca_cert_file
configuration.host = host
with client.ApiClient(configuration) as api_client:
    api_instance = client.AdmissionregistrationApi(api_client)
    try:
        api_response = api_instance.get_api_group()
        pprint(api_response)
    except rest.ApiException as e:
        print("Exception when calling AdmissionregistrationApi->get_api_group: %s\n" % e)

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Implement placeholder Flask route."""
    return 'Hello, World 2!'
