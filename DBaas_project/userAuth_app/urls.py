from django.contrib import admin

from django.urls import path,include

from userAuth_app.views import  UserAuthViewSet, LoginViewSet,AddRoleViewset,LDAPLoginView

from .views import get_user_role

from rest_framework import routers
from .views import user_roles_api , get_ADgroup_users , list_ad_groups_with_members , get_group_roles
# from .views import LDAPGroupList
from . import views  # Import the views module from your app




# from . import views
 
 
router = routers.DefaultRouter()

router.register(r'users', UserAuthViewSet, basename="register")
 
router.register(r'login', LoginViewSet, basename='login')

router.register(r'add_roles_to_user', AddRoleViewset, basename='add_roles_to_user')
# router.register(r'assign-role', AddRoleViewset, basename='assignRoles')

 
 
urlpatterns = [

    path("", include(router.urls)), 

    path('get_user_role/<int:user_id>/', get_user_role, name='get_user_role'),

    path('ldap-login/', LDAPLoginView.as_view(), name='ldap-login'),  # Add this line for LDAP login
    path('user-roles/', user_roles_api, name='user_roles_api'),
    path('assign-role/', AddRoleViewset.as_view({'post': 'create'}), name='assign-role'), 

    path('ad-groups/', get_ADgroup_users, name='get_ADgroup_users'),
    path('list-gmember/', list_ad_groups_with_members, name='list_ad_groups_with_members'),

    path('adgroup-role/', views.assign_roles_to_group_members, name='assign_roles_to_group_members'),
    path('group-roles/<str:group_name>/', get_group_roles, name='get_group_roles'),

]


    
