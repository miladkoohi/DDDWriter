from datetime import datetime
from ninja import Schema


class PostBlogRequestBody(Schema):
    title: str
    content: str
    publish_datetime: datetime | None = None


class PatchBlogRequestBody(Schema):
    title: str | None
    content: str | None
    publish_datetime: datetime | None = None
