from typing import List, Optional
from ninja import Schema
from datetime import datetime

class BlogResponse(Schema):
    id: int
    title: str
    content: str
    publish_datetime: Optional[datetime] = None

    @staticmethod
    def build(blog) -> "BlogResponse":
        return BlogResponse(
            id=blog.id,
            title=blog.title,
            content=blog.content,
            publish_datetime=blog.publish_datetime
        )

class ListBlogResponse(Schema):
    blogs: List[BlogResponse]

    @staticmethod
    def build(blogs: List) -> "ListBlogResponse":
        return ListBlogResponse(
            blogs=[BlogResponse.build(blog) for blog in blogs]
        )

class ErrorMessageResponse(Schema):
    detail: str

def error_response(detail: str) -> ErrorMessageResponse:
    return ErrorMessageResponse(detail=detail)

def response(data) -> Schema:
    return data
