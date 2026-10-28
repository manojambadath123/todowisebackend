

from django.urls import path

from api.views import SignUpView
from api.views import TodoListCreateView
from api.views import TodoUpdateDeleteView
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    path("signup/",SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("todos/",TodoListCreateView.as_view()),
    path("todos/<int:pk>/",TodoUpdateDeleteView.as_view()),
    path("jwt/token/",TokenObtainPairView.as_view()),
    path("jwt/token/refresh/",TokenRefreshView.as_view()),
    
]
