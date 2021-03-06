"""Provide Flask application.

Compatible with tiangolo/meinheld-gunicorn:python3.8 Docker image.
"""
import os


__version__ = '0.2.0'
development = os.environ.get('DEVELOPMENT') is not None
