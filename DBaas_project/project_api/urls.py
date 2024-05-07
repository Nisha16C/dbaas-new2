from django.contrib import admin
from django.urls import path, include
from project_api.views import FlavorList, ProjectViewSet,ComputeOfferingsAPIView ,ContentByClusterName, ClusterViewSet, ClusterDeleteViewSet, get_projects_by_user, display_artifacts, ContentByClusterNameView, display_clusters, get_backup_method_by_cluster_name
 
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register(r'cluster', ClusterViewSet, basename="cluster")
router.register(r'deletecluster', ClusterDeleteViewSet, basename="cluster1")
router.register(r'project', ProjectViewSet, basename='project')
 
urlpatterns = [
    
 
    path('api/v2/project/user/<int:user_id>/', get_projects_by_user, name='get_projects_by_user'),
    path('display_clusters/', display_clusters, name='display_clusters'),
   
    path('get_pipeline_status/', ClusterViewSet.as_view({'post': 'get_pipeline_status'}), name='get-pipeline-status'),
    path('get_dele_pipeline_status/', ClusterViewSet.as_view({'post': 'get_dele_pipeline_status'}), name='get-del-pipeline-status'),
    path('display_artifacts/', display_artifacts, name='display_artifacts'),
 
    path('get_backup_method/<str:cluster_name>/', get_backup_method_by_cluster_name, name='get_backup_method_by_cluster_name'),
    path('result/content/<str:username>/<str:cluster_name>/', ContentByClusterNameView.as_view(), name='content-by-cluster-name'),
    path('result/content/<str:cluster_name>/', ContentByClusterName.as_view(), name='content-by-cluster-name'),


 
    path('api/v2/cluster/check_cluster_exists/', ClusterViewSet.as_view({'get': 'check_cluster_exists'}), name='check-cluster-exists'),
    path("api/v2/project/<int:pk>/rename/", ProjectViewSet.as_view({'put': 'rename_project'}), name='rename-project'),
    path('compute_offerings/', ComputeOfferingsAPIView.as_view(), name='compute-offerings'),
 
    path('flavors/', FlavorList.as_view(), name='flavor-list'),
    path("", include(router.urls)),
]
 