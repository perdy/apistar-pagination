from apistar import types, validators


class PageNumberMeta(types.Type):
    page = validators.Integer(title="page", description="Current page number")
    page_size = validators.Integer(title="page_size", description="Page size")
    count = validators.Integer(title="count", description="Total number of items")


class PageNumberSchema(types.Type):
    data = validators.Array()
    meta = PageNumberMeta


class LimitOffsetMeta(types.Type):
    limit = validators.Integer(title="limit", description="Number of retrieved items")
    offset = validators.Integer(title="offset", description="Collection offset")
    count = validators.Integer(title="count", description="Total number of items")


class LimitOffsetSchema(types.Type):
    data = validators.Array()
    meta = LimitOffsetMeta
