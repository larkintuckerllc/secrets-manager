"""Manage Kubernetes API instance.

Development mode, i.e., DEVELOPMENT environment variable set, requires
the following files:

- ca.crt: CA Certificate
- token: access token
- host: Kubernetes API URL
"""
from kubernetes import client

from app import development


if (development):
    _ssl_ca_cert_file = 'ca.crt'
    _authorization_file = 'token'
    with open('host', 'r') as _f:
        _host = _f.read().strip()
else:
    _ssl_ca_cert_file = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
    _authorization_file = '/var/run/secrets/kubernetes.io/serviceaccount/token'
    _host = 'https://kubernetes.default'
_instance = None


def refresh_instance():
    """Refresh Kubernetes API instance."""
    global _instance
    with open(_authorization_file, 'r') as f:
        authorization = f.read().strip()
    configuration = client.Configuration()
    configuration.api_key['authorization'] = authorization
    configuration.api_key_prefix['authorization'] = 'Bearer'
    configuration.ssl_ca_cert = _ssl_ca_cert_file
    configuration.host = _host
    with client.ApiClient(configuration) as api_client:
        _instance = client.CoreV1Api(api_client)


def get_instance():
    """Return Kubernetes API instance."""
    if _instance is not None:
        return _instance
    refresh_instance()
    return _instance
