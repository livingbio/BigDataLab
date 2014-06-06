import endpoints
from .models import *
from protorpc import remote
from lib.endpoints_restful import *

BigDataLab = EndpointRestBuilder(GPCode).build(name="BigDataLab", version="v1", description="My Little Api")
