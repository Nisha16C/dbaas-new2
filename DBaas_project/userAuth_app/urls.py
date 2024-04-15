from django.contrib import admin

from django.urls import path,include

from userAuth_app.views import  UserAuthViewSet, LoginViewSet,AddRoleViewset,LDAPLoginView

from .views import get_user_role

from rest_framework import routers
from .views import user_roles_api


# from . import views
 
 
router = routers.DefaultRouter()

router.register(r'users', UserAuthViewSet, basename="register")
 
router.register(r'login', LoginViewSet, basename='login')

router.register(r'add_roles_to_user', AddRoleViewset, basename='add_roles_to_user')
 
 
urlpatterns = [

    path("", include(router.urls)),

    path('get_user_role/<int:user_id>/', get_user_role, name='get_user_role'),

    path('ldap-login/', LDAPLoginView.as_view(), name='ldap-login'),  # Add this line for LDAP login
    path('user-roles/', user_roles_api, name='user_roles_api'),


]