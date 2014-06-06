from generic_pipeline.apis import *
import endpoints

app = endpoints.api_server([
    BigDataLab
],restricted=False)
