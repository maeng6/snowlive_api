from django.urls import path
from user_app.api.views import logout_view, RegisterView

urlpatterns = [
    # path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
]