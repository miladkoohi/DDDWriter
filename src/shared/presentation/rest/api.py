from django.contrib import admin
from django.http import HttpRequest
from django.urls import path
from ninja import NinjaAPI
from blog.presentation.rest.api import router as blog_router
from user.presentation.rest.api import router as user_router

api = NinjaAPI(
    title="Django-DDD(DDDWriter)",
    description="This is a demo API with dynamic OpenAPI info section.",
)


@api.get("health-check/")
def health_check(request: HttpRequest):
    return {"status": "ok"}


api.add_router("blog/", blog_router)
api.add_router("users/", user_router)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]