"""Provide Flask application."""
from flask import Flask
from kubernetes.client import rest

from app import kubernetes_api
import pprint


app = Flask(__name__)


@app.route('/')
def hello_world():
    """Execute health check."""
    return 'healthy'


# READ CONFIGMAPS

def test(item):
    """TODO."""
    return ({
        'name': item.metadata.name,
        'data': item.data,
    })


def ph(api_instance):
    """TODO."""
    response = api_instance.list_namespaced_config_map('default')
    configmaps = list(map(test, response.items))
    pprint.pprint(configmaps)


@app.route('/configmaps')
def get_configmaps():
    """Read ConfigMaps."""
    api_instance = kubernetes_api.get_instance()
    try:
        ph(api_instance)
        return 'success'
    except rest.ApiException:
        kubernetes_api.refresh_instance()
        api_instance = kubernetes_api.get_instance()
        try:
            ph(api_instance)
            return 'success'
        except rest.ApiException as e:
            return ("%s" % e)
