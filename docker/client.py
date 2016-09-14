from .api.client import APIClient
from .models.containers import ContainerCollection
from .models.images import ImageCollection
from .models.networks import NetworkCollection
from .models.nodes import NodeCollection
from .models.services import ServiceCollection
from .models.swarm import Swarm
from .models.volumes import VolumeCollection
from .utils import kwargs_from_env


class Client(object):
    """
    A client for a Docker server.
    """
    def __init__(self, *args, **kwargs):
        self.api = APIClient(*args, **kwargs)

    @classmethod
    def from_env(cls, **kwargs):
        """
        Return a client configured with the standard set of Docker environment
        variables. For example, `DOCKER_HOST`, `DOCKER_CERT_PATH`, etc.
        """
        return cls(**kwargs_from_env(**kwargs))

    # Resources
    @property
    def containers(self):
        return ContainerCollection(client=self)

    @property
    def images(self):
        return ImageCollection(client=self)

    @property
    def networks(self):
        return NetworkCollection(client=self)

    @property
    def nodes(self):
        return NodeCollection(client=self)

    @property
    def services(self):
        return ServiceCollection(client=self)

    @property
    def swarm(self):
        return Swarm(client=self)

    @property
    def volumes(self):
        return VolumeCollection(client=self)

    # Top-level methods
    def events(self, *args, **kwargs):
        return self.api.events(*args, **kwargs)

    def info(self, *args, **kwargs):
        return self.api.info(*args, **kwargs)

    def login(self, *args, **kwargs):
        return self.api.login(*args, **kwargs)

    def ping(self, *args, **kwargs):
        return self.api.ping(*args, **kwargs) == 'OK'

    def version(self, *args, **kwargs):
        return self.api.version(*args, **kwargs)

from_env = Client.from_env
