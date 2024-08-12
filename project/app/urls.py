from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 
router = routers.DefaultRouter()
router.register(r'users', Studentviewset, basename='user')


urlpatterns =[
    path('',include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
    path('api-token-auth/',obtain_auth_token)
]