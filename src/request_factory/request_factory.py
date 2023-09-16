import requests


class ApiRequestFactory:
    def __init__(self):
        self.session = requests.Session()
        # You can configure session here, such as headers or auth tokens

    def send_request(self, method, url, params=None, data=None, headers=None, auth=None):
        """
        Send a generic API request.

        Args:
            method (str): HTTP method ('GET', 'POST', 'PUT', 'DELETE', etc.).
            url (str): The URL of the API endpoint.
            params (dict): Query parameters to include in the request.
            data (dict): Request data (for POST or PUT requests).
            headers (dict): Custom headers to include in the request.
            auth (tuple): Authentication credentials (username, password).

        Returns:
            requests.Response: The response object from the API request.
        """
        try:
            response = self.session.request(
                method,
                url,
                params=params,
                data=data,
                headers=headers,
                auth=auth
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response
        except requests.exceptions.RequestException as e:
            # Handle request errors here
            raise e
