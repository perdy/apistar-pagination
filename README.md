# API Star Pagination
[![Build Status](https://travis-ci.org/PeRDy/apistar-pagination.svg?branch=master)](https://travis-ci.org/PeRDy/apistar-pagination)
[![codecov](https://codecov.io/gh/PeRDy/apistar-pagination/branch/master/graph/badge.svg)](https://codecov.io/gh/PeRDy/apistar-pagination)
[![PyPI version](https://badge.fury.io/py/apistar-pagination.svg)](https://badge.fury.io/py/apistar-pagination)

* **Version:** 0.1.0
* **Status:** Production/Stable
* **Author:** José Antonio Perdiguero López

Pagination tools for API Star.

## Features
* Page number pagination.
* Limit-offset pagination.

## Quick start
Install API star Pagination:

```bash
pip install apistar-pagination
```

Use paginated response in your views:

### Page number pagination

```python
from apistar_pagination import PageNumberResponse

def page_number(page: http.QueryParam, page_size: http.QueryParam) -> typing.List[int]:
    collection = ...  # Get your whole collection

    return PageNumberResponse(page=page, page_size=page_size, content=collection)
```

### Limit-offset pagination

```python
from apistar_pagination import LimitOffsetResponse

def limit_offset(offset: http.QueryParam, limit: http.QueryParam) -> typing.List[int]:
    collection = ...  # Get your whole collection

    return LimitOffsetResponse(offset=offset, limit=limit, content=collection)
```
