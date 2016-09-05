# flake8: noqa
from .api import APIClient, AutoVersionAPIClient
from .client import Client, from_env
from .version import version, version_info

__version__ = version
__title__ = 'docker-py'
