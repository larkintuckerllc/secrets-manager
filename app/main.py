"""Provide Flask application."""
from flask import Flask
# from kubernetes import client, config
from kubernetes import client
from kubernetes.client import rest
from pprint import pprint


authorization = 'ya29.a0AfH6SMC9mMDaGseqPWJq-dVOiWmq45i5gqDzW6bYf-IN8liWtSLExHokcXNmkXCBwX8_MnSMUcDoLjq3nkYjcWC5Lo7WNimQanpql0f-jdg7dx1ZpjvL9Dte1njDMvgdOrRwPHjCiZI7SQvYK14gSWQh3zldUa_AGGU52VjVCJfz'  # TODO: FIX
ssl_ca_cert = '/home/sckmkny/cert.pem'
configuration = client.Configuration()
configuration.api_key['authorization'] = authorization
configuration.api_key_prefix['authorization'] = 'Bearer'
configuration.ssl_ca_cert = ssl_ca_cert
configuration.host = "https://35.247.94.9"  # TODO: CHANGE

with client.ApiClient(configuration) as api_client:
    api_instance = client.AdmissionregistrationApi(api_client)
    try:
        api_response = api_instance.get_api_group()
        pprint(api_response)
    except rest.ApiException as e:
        print("Exception when calling AdmissionregistrationApi->get_api_group: %s\n" % e)

# config.load_kube_config()
# v1 = client.CoreV1Api()
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Implement placeholder Flask route."""
    # ret = v1.list_pod_for_all_namespaces(watch=False)
    # for i in ret.items:
    #     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace,
    #                           i.metadata.name))
    return 'Hello, World!'
