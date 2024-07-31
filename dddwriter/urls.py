
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.presentation.urls')),
    path('api/user/', include('user.presentation.urls')),
]
