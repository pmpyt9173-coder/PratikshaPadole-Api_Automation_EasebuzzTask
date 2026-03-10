import time
from jsonschema import validate
import os

from api.api_clients import APIClient
from api.endpoints import  POSTS
from schemas.post_schema import post_schema
from Utility.file_reader import save_json

client = APIClient()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def test_fetch_posts():

    start = time.time()

    response = client.get(POSTS)

    end = time.time()

    assert response.status_code == 200
    assert (end - start) < 2

    posts = response.json()

    for post in posts:
        validate(instance=post, schema=post_schema)

    file_path = os.path.join(BASE_DIR, "TestData", "posts.json")
    save_json(posts[:5], file_path)
