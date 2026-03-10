import requests
from api.endpoints import BASE_URL

class APIClient:

    def get(self, endpoint):
        return requests.get(BASE_URL + endpoint)

    def post(self, endpoint, payload):
        return requests.post(BASE_URL + endpoint, json=payload)

    def delete(self, endpoint):
        return requests.delete(BASE_URL + endpoint)