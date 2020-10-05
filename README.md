# Secrets Manager

A demonstration of running a web application on a Kubernetes cluster managing Kubernetes objects, in this case ConfigMaps in the *default* namespace.

**note**: The first plan was to manage Secrets, thus the name of the repository.  At the last minute, switched to ConfigMaps as to not have to deal with the secrets associated with service accounts.

## Infrastructure

The infrastructure supporting the web application is managed using Terraform configuration files in the *tf* folder. The managed resources:

- Service Account
- ClusterRole
- RoleBinding
- Deployment
- Service

The deployment is configured to ignore changes to the container image as to allow for deploying new versions of the web application outside of the Terraform configuration.

## Web Application

The web application is a Flask (Python) web application bundled into a Docker image. The code is delivered as a Python package in the *app* folder. The application is also has auto-generated [documentation](https://larkintuckerllc.github.io/secrets-manager/).
