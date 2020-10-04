"""Provide Flask application."""
from flask import Flask
from kubernetes.client import rest

from app import kubernetes_api


# TODO: MOVE TO CORRECT API CALL
# TODO: REMOVE DEBUGGING
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Implement placeholder Flask route."""
    api_instance = kubernetes_api.get_instance()
    try:
        api_instance.get_api_group()
        return 'Success'
    except rest.ApiException:
        api_instance = kubernetes_api.refresh_instance()
        try:
            api_instance.get_api_group()
            return 'Success'
        except rest.ApiException as e:
            return ("%s" % e)
