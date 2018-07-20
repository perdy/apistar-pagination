import typing

import pytest
from apistar import App, ASyncApp, Route, TestClient, http

from apistar_pagination import LimitOffsetResponse, PageNumberResponse


def limit_offset(offset: http.QueryParam, limit: http.QueryParam) -> typing.List[int]:
    return LimitOffsetResponse(offset=offset, limit=limit, content=list(range(25)))


def page_number(page: http.QueryParam, page_size: http.QueryParam) -> typing.List[int]:
    return PageNumberResponse(page=page, page_size=page_size, content=list(range(25)))


routes = [
    Route("/limit_offset", "GET", limit_offset, "limit_offset", documented=False),
    Route("/page_number", "GET", page_number, "page_number", documented=False),
]
app = App(routes=routes, static_dir=None, docs_url=None, schema_url=None)
async_app = ASyncApp(routes=routes, static_dir=None, docs_url=None, schema_url=None)


@pytest.fixture(params=[app, async_app])
def client(request):
    return TestClient(request.param)


class TestLimitOffsetResponse:
    def test_default_params(self, client):
        response = client.get("/limit_offset")
        assert response.status_code == 200
        assert response.json() == {"meta": {"limit": 10, "offset": 0, "count": 25}, "data": list(range(10))}

    def test_default_offset_explicit_limit(self, client):
        response = client.get("/limit_offset", params={"limit": 5})
        assert response.status_code == 200
        assert response.json() == {"meta": {"limit": 5, "offset": 0, "count": 25}, "data": list(range(5))}

    def test_default_limit_explicit_offset(self, client):
        response = client.get("/limit_offset", params={"offset": 5})
        assert response.status_code == 200
        assert response.json() == {"meta": {"limit": 10, "offset": 5, "count": 25}, "data": list(range(5, 15))}

    def test_explicit_params(self, client):
        response = client.get("/limit_offset", params={"offset": 5, "limit": 20})
        assert response.status_code == 200
        assert response.json() == {"meta": {"limit": 20, "offset": 5, "count": 25}, "data": list(range(5, 25))}


class TestPageNumberResponse:
    def test_default_params(self, client):
        response = client.get("/page_number")
        assert response.status_code == 200
        assert response.json() == {"meta": {"page": 1, "page_size": 10, "count": 25}, "data": list(range(10))}

    def test_default_page_explicit_size(self, client):
        response = client.get("/page_number", params={"page_size": 5})
        assert response.status_code == 200
        assert response.json() == {"meta": {"page": 1, "page_size": 5, "count": 25}, "data": list(range(5))}

    def test_default_size_explicit_page(self, client):
        response = client.get("/page_number", params={"page": 2})
        assert response.status_code == 200
        assert response.json() == {"meta": {"page": 2, "page_size": 10, "count": 25}, "data": list(range(10, 20))}

    def test_explicit_params(self, client):
        response = client.get("/page_number", params={"page": 4, "page_size": 5})
        assert response.status_code == 200
        assert response.json() == {"meta": {"page": 4, "page_size": 5, "count": 25}, "data": list(range(15, 20))}
