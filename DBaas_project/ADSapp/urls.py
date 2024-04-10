from django.urls import path , include
# from .views import update_ldap_settings
from ADSapp.views import FormViewSet
# from .views import ActiveUserListView
from rest_framework import routers
from .views import LDAPAuthenticatedUserListView 
router = routers.DefaultRouter()
 
router.register(r'update_ldap_settings', FormViewSet, basename='update_ldap_settings')
router.register(r'reset_ldap_settings', FormViewSet, basename='reset_ldap_settings')
 
urlpatterns = [
    # path('active-users/', ActiveUserListView.as_view(), name='active_users'),
    path('ldap-authenticated-users/', LDAPAuthenticatedUserListView.as_view(), name='ldap_authenticated_users'),
 
 
    path("", include(router.urls)),
]