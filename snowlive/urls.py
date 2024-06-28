from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-snowlive134/', admin.site.urls),
    path('api/accounts/', include('user_app.api.urls')),
]
