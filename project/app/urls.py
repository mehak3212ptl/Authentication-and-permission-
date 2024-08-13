from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()
router.register(r'users', Studentviewset, basename='user')


urlpatterns =[
    path('',include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))--------------------------session 
    # path('api-token-auth/',obtain_auth_token) ---------------------------------3rd way to create
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]