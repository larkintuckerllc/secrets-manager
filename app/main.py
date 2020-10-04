"""Provide Flask application."""
from flask import Flask
from kubernetes import client, config


config.load_kube_config()
v1 = client.CoreV1Api()
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Implement placeholder Flask route."""
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace,
                              i.metadata.name))
    return 'Hello, World!'
