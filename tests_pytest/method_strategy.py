from abc import ABC, abstractmethod


class Method:

    def __init__(self, method):
        self._method = method

    def get_response(self, client, route, headers, json, params):
        return self._method.make_request(
            client, route, headers, json, params
        )


class MethodStrategy(ABC):

    @abstractmethod
    def make_request(self, client, route, headers, json, params):
        pass


class Get(MethodStrategy):

    def make_request(self, client, route, headers, json, params):
        return client.get(route, headers=headers, query_string=params)


class Post(MethodStrategy):

    def make_request(self, client, route, headers, json, params):
        return client.post(route, headers=headers, json=json)
