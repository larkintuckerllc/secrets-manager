"""Provide Flask application."""
import json

from flask import abort, Flask
from kubernetes.client import rest

from app import kubernetes_api


app = Flask(__name__)


@app.route('/')
def hello_world():
    """Execute health check."""
    return 'healthy'


# READ CONFIGMAPS

def item_to_configmap(item):
    """Parse item into ConfigMap."""
    return ({
        'name': item.metadata.name,
        'data': item.data,
    })


def api_to_configmaps(api_instance):
    """API to ConfigMaps."""
    response = api_instance.list_namespaced_config_map('default')
    configmaps = list(map(item_to_configmap, response.items))
    return configmaps


@app.route('/configmaps')
def get_configmaps():
    """Read ConfigMaps."""
    api_instance = kubernetes_api.get_instance()
    try:
        configmaps = api_to_configmaps(api_instance)
        return json.dumps(configmaps)
    except rest.ApiException:
        kubernetes_api.refresh_instance()
        api_instance = kubernetes_api.get_instance()
        try:
            configmaps = api_to_configmaps(api_instance)
            return json.dumps(configmaps)
        except rest.ApiException:
            abort(500)

# DELETE CONFIGMAPS

# TODO: Implement

# CREATE CONFIGMAPS

# TODO: Implement
