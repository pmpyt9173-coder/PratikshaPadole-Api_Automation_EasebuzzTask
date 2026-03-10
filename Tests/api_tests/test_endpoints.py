import pytest

from api.api_clients import APIClient
from api.endpoints import POSTS, COMMENTS, USERS

client = APIClient()


@pytest.mark.parametrize("endpoint",
[
POSTS,
COMMENTS,
USERS
])

def test_multiple_endpoints(endpoint):

    response = client.get(endpoint)

    assert response.status_code == 200