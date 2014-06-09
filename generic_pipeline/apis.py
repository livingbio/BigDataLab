import endpoints
from .models import *
from protorpc import remote
from endpoints_proto_datastore_rest import *

BigDataLab = EndpointRestBuilder(GPCode).build(
    api_name="BigDataLab",
    name="bigdatalab",
    version="v1",
    description="My Little Api"
)
