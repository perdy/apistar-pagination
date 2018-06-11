import typing

from apistar.http import JSONResponse


class PageNumberResponse(JSONResponse):
    """
    Response paginated based on a page number and a page size.

    First 10 elements:
        /resource?page=1

    Third 10 elements:
        /resource?page=3

    First 20 elements:
        /resource?page=1&page_size=20
    """

    default_page_size = 10

    def __init__(self, page: typing.Optional[int] = None, page_size: typing.Optional[int] = None, **kwargs):
        self.page_number = int(page) if page is not None else 1
        self.page_size = int(page_size) if page_size is not None else self.default_page_size
        super().__init__(**kwargs)

    def render(self, content: typing.Sequence):
        init = (self.page_number - 1) * self.page_size
        end = self.page_number * self.page_size
        return super().render(content[init:end])


class LimitOffsetResponse(JSONResponse):
    """
    Response paginated based on a limit of elements and an offset.

    First 10 elements:
        /resource?offset=0&limit=10

    Elements 20-30:
        /resource?offset=20&limit=10
    """

    default_limit = 10

    def __init__(self, offset: typing.Optional[int] = None, limit: typing.Optional[int] = None, **kwargs):
        self.offset = int(offset) if offset is not None else 0
        self.limit = int(limit) if limit is not None else self.default_limit
        super().__init__(**kwargs)

    def render(self, content: typing.Sequence):
        init = self.offset
        end = self.offset + self.limit
        return super().render(content[init:end])