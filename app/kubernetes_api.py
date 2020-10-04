"""Return Kubernetes API instance."""
from kubernetes import client

from app import development


if (development):
    _ssl_ca_cert_file = 'ca.pem'
    _authorization_file = 'authorization.txt'
    with open('host.txt', 'r') as _f:
        _host = _f.read().strip()
else:  # TODO FIX
    _ssl_ca_cert_file = 'ca.pem'
    _authorization_file = 'authorization.txt'
    _host = 'https://35.247.94.9'
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
        # TODO: MOVE TO CORRECT CALL
        _instance = client.AdmissionregistrationApi(api_client)


def get_instance():
    """Return Kubernetes API instance."""
    if _instance is not None:
        return _instance
    refresh_instance()
    return _instance
