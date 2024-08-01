from typing import List

from ninja import Router
from shared.domain.exception import JWTKeyParsingException
from shared.infrastructure.authentication import auth_bearer
from shared.presentation.rest.containers import auth_service
from shared.presentation.rest.response import (
    ErrorMessageResponse,
    ObjectResponse,
    error_response,
    response,
)
from blog.domain.entity import BlogPost
from blog.domain.exception import BlogPostNotFoundException
from blog.presentation.rest.containers import blog_command, blog_query
from blog.presentation.rest.request import PatchBlogRequestBody, PostBlogRequestBody
from blog.presentation.rest.response import ListBlogResponse, BlogResponse

router = Router(tags=["blogs"], auth=auth_bearer)

@router.get(
    "/{blog_id}",
    response={
        200: ObjectResponse[BlogResponse],
        401: ObjectResponse[ErrorMessageResponse],
        404: ObjectResponse[ErrorMessageResponse],
    },
)
def get_blog_handler(request, blog_id: int):
    try:
        user_id: int = auth_service.get_user_id_from_token(token=request.auth)
    except JWTKeyParsingException as e:
        return 401, error_response(str(e))

    try:
        blog: BlogPost = blog_query.get_blog_of_user(user_id=user_id, blog_id=blog_id)
    except BlogPostNotFoundException as e:
        return 404, error_response(str(e))

    return 200, response(BlogResponse.build(blog=blog))

@router.get(
    "",
    response={
        200: ObjectResponse[ListBlogResponse],
        401: ObjectResponse[ErrorMessageResponse],
    },
)
def get_blog_list_handler(request):
    try:
        user_id: int = auth_service.get_user_id_from_token(token=request.auth)
    except JWTKeyParsingException as e:
        return 401, error_response(str(e))

    blogs: List[BlogPost] = blog_query.get_blogs_of_user(user_id=user_id)
    return 200, response(ListBlogResponse.build(blogs=blogs))

@router.post(
    "",
    response={
        201: ObjectResponse[BlogResponse],
        401: ObjectResponse[ErrorMessageResponse],
        404: ObjectResponse[ErrorMessageResponse],
    },
)
def post_blog_handler(request, body: PostBlogRequestBody):
    try:
        user_id: int = auth_service.get_user_id_from_token(token=request.auth)
    except JWTKeyParsingException as e:
        return 401, error_response(str(e))

    try:
        user: User = user_query.get_user(user_id=user_id)
    except UserNotFoundException as e:
        return 404, error_response(str(e))

    blog: BlogPost = blog_command.create_blog(user=user, title=body.title, content=body.content)
    return 201, response(BlogResponse.build(blog=blog))

@router.patch(
    "/{blog_id}",
    response={
        200: ObjectResponse[BlogResponse],
        401: ObjectResponse[ErrorMessageResponse],
        404: ObjectResponse[ErrorMessageResponse],
    },
)
def patch_blog_handler(request, blog_id: int, body: PatchBlogRequestBody):
    try:
        user_id: int = auth_service.get_user_id_from_token(token=request.auth)
    except JWTKeyParsingException as e:
        return 401, error_response(str(e))

    try:
        blog: BlogPost = blog_query.get_blog_of_user(user_id=user_id, blog_id=blog_id)
    except BlogPostNotFoundException as e:
        return 404, error_response(str(e))

    blog: BlogPost = blog_command.update_blog(blog=blog, title=body.title, content=body.content)
    return 200, response(BlogResponse.build(blog=blog))

@router.delete(
    "/{blog_id}",
    response={
        204: None,
        401: ObjectResponse[ErrorMessageResponse],
        404: ObjectResponse[ErrorMessageResponse],
    },
)
def delete_blog_handler(request, blog_id: int):
    try:
        user_id: int = auth_service.get_user_id_from_token(token=request.auth)
    except JWTKeyParsingException as e:
        return 401, error_response(str(e))

    try:
        blog_command.delete_blog_of_user(user_id=user_id, blog_id=blog_id)
    except BlogPostNotFoundException as e:
        return 404, error_response(str(e))

    return 204, None
