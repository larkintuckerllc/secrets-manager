"""Provide Flask application."""
from flask import Flask
# from kubernetes.client import rest
# from pprint import pprint

from app import kubernetes_api


# TODO: WORRY ABOUT UPDATED SECRET
# TODO: MOVE TO CORRECT API CALL
api_instance = kubernetes_api.get_instance()
# try:
#     api_response = api_instance.get_api_group()
#     pprint(api_response)
# except rest.ApiException as e:
#     print("Exception when calling AdmissionregistrationApi->get_api_group: %s\n" % e)

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Implement placeholder Flask route."""
    return 'Hello, World 2!'
