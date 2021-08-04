# Useage
    json_config_file_path = os.path.join(
        os.getcwd(),
        'example',
        'api_params.json'
    )
    client = ApiClient(json_config_file_path)
    data = client.make_request('example1')

    # make_request(
    #   name_of_config_in_json_file: str,
    #   extra_headers_of_request: Dict,
    #   extra_parameter_of_request: Dict
    # )
    #


# To develop 

