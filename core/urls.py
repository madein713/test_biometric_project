from django.contrib import admin
from django.urls import path

from core.views import Other

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', Other.as_view())
]
