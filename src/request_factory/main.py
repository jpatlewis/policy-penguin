from request_factory import ApiRequestFactory\

# Example usage:
if __name__ == '__main__':

    api_factory = ApiRequestFactory()

    # Example GET request
    response = api_factory.send_request(
        method='GET',
        url='https://api.example.com/resource',
        params={'param1': 'value1', 'param2': 'value2'}
    )

    # Example POST request
    response = api_factory.send_request(
        method='POST',
        url='https://api.example.com/resource',
        data={'key1': 'value1', 'key2': 'value2'},
        headers={'Content-Type': 'application/json'},
        auth=('username', 'password')
    )

    # Handle the response as needed
    print(response.status_code)
    print(response.json())
