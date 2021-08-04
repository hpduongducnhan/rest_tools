from ndd_rest_tools.main import ApiClient
from ndd_rest_tools.models import RequestResponse
import os


def run():
    client = ApiClient(
        os.path.join(
            os.getcwd(),
            'example',
            'api_params.json'
        )
    )

    data = client.make_request('example1')
    print(data)