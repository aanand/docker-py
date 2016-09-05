# flake8: noqa
from .version import version, version_info

__version__ = version
__title__ = 'docker-py'

from .api import APIClient, AutoVersionAPIClient
