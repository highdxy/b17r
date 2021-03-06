from django.conf.urls import url
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register('activities', views.ActivitiesViewSet)
routers.register('molecules', views.MoleculeViewSet)
routers.register('scaffold-activities', views.ScaffoldActivitiesViewSet)
routers.register('scaffolds', views.ScaffoldViewSet)
# routers.register('target-interactions', views.TargetInteractionViewSet)
# routers.register('target-scaffold-interactions', views.TargetScaffoldInteractionViewSet)
routers.register('targets', views.TargetViewSet)
routers.register('mmps', views.MMPViewSet)
routers.register('kegg-disease-classes', views.KEGGDiseaseClassViewSet)
routers.register('kegg-diseases', views.KEGGDiseaseViewSet)
routers.register('target-network', views.TargetNetworkViewSet)
routers.register('icd', views.ICDViewSet)
routers.register('target-scaffold-network', views.TargetScaffoldNetworkViewSet)
routers.register('molecule-network', views.MoleculeInteractionViewSet)
# routers.register('target-network', views.TargetInteractionViewSet.as_view, base_name='target-network')

urlpatterns = routers.urls
urlpatterns += [
    # url(
    #     r'^target-network/(?P<tid>[0-9]+)',
    #     views.TargetNetworkViewSet.as_view()
    # ),
    # url(
    #     r'^target-scaffold-network/(?P<tid>[0-9]+)',
    #     views.TargetScaffoldNetworkViewSet.as_view()
    # ),
    url(r'^related-targets/(?P<target_id>[0-9]+)', views.get_related_target),
    url(r'^related-targets-list/', views.get_related_target_list)
]
