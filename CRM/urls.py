from django.contrib import admin
from django.urls import path, include
from app.views import zer0Point

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", zer0Point, name="zer0Point"),
    path('app/', include('app.urls')),
]
