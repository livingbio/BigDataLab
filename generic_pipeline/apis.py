import endpoints
from .models import *
from protorpc import remote
from lib.endpoints_restful import *

MyApi = EndpointRestBuilder(GPCode).build(name="MyApi", version="v1", description="My Little Api")
